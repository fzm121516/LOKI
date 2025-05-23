import copy
import json
import re

import torch
import av
import numpy as np

from typing import List, Union, Optional
from copy import deepcopy
from datetime import timedelta

from lm_evaluate.api.model import LMM
from lm_evaluate.api.registry import register_model


from accelerate import Accelerator, DistributedType
from accelerate.utils import InitProcessGroupKwargs
from accelerate.state import AcceleratorState
from decord import VideoReader, cpu
from loguru import logger as eval_logger
from PIL import Image

try:
    from transformers import MllamaForConditionalGeneration, AutoProcessor
except Exception as e:
    eval_logger.debug("Upgrade transformers to use Mantis's idefics model.\nError: %s" % e)


DEFAULT_IMAGE_TOKEN = "<image>"


@register_model("llama3-vision")
class Llama3Vision(LMM):
    supported_modalities = ["video", "image", "text"]
    def __init__(
        self,
        model_version: str = "meta-llama/Llama-3.2-11B-Vision",
        device: str = "cuda",
        device_map: str = "cuda",
        model_name: str = None,
        dtype: Optional[Union[str, torch.dtype]] = torch.bfloat16,
        attn_implementation: Optional[str] = (
            "sdpa" if torch.__version__ >= "2.1.2" else "eager"
        ),
        max_num_frames: Optional[int] = 32,
        truncation: bool = True,
        use_cache=True,
        **kwargs
    ):
        self.model_version = model_version
        
        # if isinstance(dtype, str) and dtype != "auto":
        #     dtype = getattr(torch, dtype)
        
        self._device = device
        self.device_map = device_map
        self.dtype = torch.float16
        self.attn_implementation = attn_implementation
        self.max_num_frames = max_num_frames
        self.model_name = model_name
        self.truncation = truncation
        
        self.max_num_frames = max_num_frames
        
        
        self.use_cache = use_cache
        
        self.prepare_model()
    
        
    def prepare_model(self):
        
        accelerator_kwargs = InitProcessGroupKwargs(timeout=timedelta(weeks=52))
        accelerator = Accelerator(kwargs_handlers=[accelerator_kwargs])
        if accelerator.num_processes > 1:
            self._device = torch.device(f"cuda:{accelerator.local_process_index}")
            self.device_map = f"cuda:{accelerator.local_process_index}"
        elif accelerator.num_processes == 1 and self.device_map == "auto":
            self._device = torch.device(self._device)
            self.device_map = self.device_map
        else:
            self._device = torch.device(f"cuda:{accelerator.local_process_index}")
            self.device_map = f"cuda:{accelerator.local_process_index}"
        
        
        
        # Here we load the "non-idefics" Mantis model.
        
        self._processor = AutoProcessor.from_pretrained(self.model_version)
        self._model = MllamaForConditionalGeneration.from_pretrained(self.model_version, device_map=self.device_map, torch_dtype=self.dtype)

        self._tokenizer = self._processor.tokenizer
        

        self._config = self._model.config
        self.model.eval()
        self.model.tie_weights()
        
        
        self.accelerator = accelerator
        if accelerator.num_processes > 1:
            assert accelerator.distributed_type in [DistributedType.FSDP, DistributedType.MULTI_GPU, DistributedType.DEEPSPEED], "Unsupported distributed type provided. Only DDP and FSDP are supported."
            # If you want to use DistributedType.DEEPSPEED, you have to run accelerate config before using the model
            # Also, you have to select zero stage 0 (equivalent to DDP) in order to make the prepare model works
            # I tried to set different parameters in the kwargs to let default zero 2 stage works, but it didn't work.
            if accelerator.distributed_type == DistributedType.DEEPSPEED:
                kwargs = {
                    "train_micro_batch_size_per_gpu": 1,
                    "train_batch_size": 1 * accelerator.num_processes,
                }
                AcceleratorState().deepspeed_plugin.deepspeed_config_process(must_match=True, **kwargs)
                eval_logger.info("Detected that you are using DistributedType.DEEPSPEED. Make sure you run `accelerate config` and set zero stage to 0")
            if accelerator.distributed_type == DistributedType.FSDP or accelerator.distributed_type == DistributedType.DEEPSPEED:
                self._model = accelerator.prepare(self.model)
            else:
                self._model = accelerator.prepare_model(self.model, evaluation_mode=True)
            
            if self.accelerator.is_local_main_process:
                eval_logger.info(f"Using {accelerator.num_processes} devices with data parallelism")
            self._rank = self.accelerator.local_process_index
            self._world_size = self.accelerator.num_processes
        elif accelerator.num_processes == 1 and self.device_map == "auto":
            eval_logger.info(f"Using {accelerator.num_processes} devices with tensor parallelism")
            self._rank = 0
            self._word_size = 1
        else:
            eval_logger.info(f"Using single device: {self._device}")
            self._model.to(self._device)
            self._rank = 0
            self._world_size = 1
        
        self.prepared = True
        
    
    @property
    def model(self):
        # returns the model, unwrapping it if using Accelerate
        if hasattr(self, "accelerator"):
            return self.accelerator.unwrap_model(self._model)
        else:
            return self._model
        
    
    @property
    def tokenizer(self):
        return self._tokenizer
    
    
    @property
    def config(self):
        return self._config
    
    @property
    def device(self):
        return self._device
    
    def encode_video(self, video_path):
        if type(video_path) == str:
            vr = VideoReader(video_path, ctx=cpu(0))
        else:
            vr = VideoReader(video_path[0], ctx=cpu(0))
        total_frame_num = len(vr)
        uniform_sampled_frames = np.linspace(0, total_frame_num - 1, self.max_num_frames, dtype=int)
        frame_idx = uniform_sampled_frames.tolist()
        sparse_frames = vr.get_batch(frame_idx).asnumpy()
        sparse_frames = [Image.fromarray(v.astype('uint8')) for v in sparse_frames]
        return sparse_frames  # (frames, height, width, channels)
        
    
    
    def generate(
        self, 
        visuals: Union[Image.Image, str, List[Union[Image.Image, str]]],
        contexts: str,
        **kwargs
    ) -> str:
        """
            Call mantis for response with visuals and contexts. Visuals can be a list of strings(representing video paths), or a list of PIL.Image.Image or a combination of both. Returns a piece of response text.
            
            Args:
                visuals: Media objects. Visuals can be one image, one video path, or a list of them. 
                contexts: Prompt text.
                kwargs: Generation kwargs. Currently we only support greedy decoding. # TODO: Support diverse decoding strategy.
            Return:
                A piece of response text
        """
        
        images = []
        
        num_image = 0
        video_frames = []
        # four scenarios:
        # visuals is a list of string
        # visuals is a list of PIL Images and strings
        # visuals is a string
        # visuals is a PIL Image
        # visuals is None
        
        # For mantis, we convert concat media objects (videos, images) together
        # Ensure images is 1D (type Image.Image as elements)
        if isinstance(visuals, list):
            for visual in visuals:
                if isinstance(visual, str):
                    frames = self.encode_video(visual)
                    images.extend(frames)
                    video_frames.append(len(frames))
                elif isinstance(visual, Image.Image):
                    images.append(visual)
                    num_image += 1
                else:
                    error_msg = f"Expected visual type to be Image.Image or str. Got: {type(visual)}"
                    eval_logger.error(TypeError(error_msg))
        elif isinstance(visuals, str):
            frames = self.encode_video(visuals)
            images.extend(frames)
            video_frames.append(len(frames))
        elif isinstance(visuals, Image.Image):
            images.append(visuals)
            num_image += 1
        
        # Segment the text according to video and image token
        
        if num_image > contexts.count("<image>"):
            eval_logger.warning("<image> tokens num is less than actual number of images. Appending <image> at the front.")
            contexts = "<image> " * (len(images) - contexts.count("<image>")) + contexts

        if len(video_frames) > contexts.count("<video>"):
            eval_logger.warning("<video> tokens num is less than actual number of images. Appending <video> at the front.")
            contexts = "<video> " * (len(video_frames) - contexts.count("<video>")) + contexts
        
        
        gen_kwargs = {}
        
        if "max_new_tokens" not in kwargs:
            gen_kwargs["max_new_tokens"] = 1024
        if "temperature" not in kwargs:
            gen_kwargs["temperature"] = 0
            
            
        # Segment the text according to video and image token
        contexts = re.split(r'(<video>|<image>)', contexts)
        contexts = [context for context in contexts if context]
        
        prompt = ""
        
        video_idx = 0
        
        messages = [
            {
                "role": "user", 
                "content": [
                    {"type": "text", "text": "If I had to write a haiku for this one, it would be: "}
                ]
            }
        ]
        
        for context in contexts:
            if context == "<video>":
                prompt += "<image>\n" * video_frames[video_idx]
                for _ in range(video_frames[video_idx]):
                    messages[0]['content'].append({"type": "image"})
                video_idx += 1
            elif context == "<image>":
                prompt += "<image>\n"
                messages[0]['content'].append({"type": "image"})
            else:
                prompt += "<|begin_of_text|>" + context
                messages[0]['content'].append({"type": "text", "text": context})
        
        
        gen_kwargs = {"max_new_tokens": 1024}
        # Follow the idefics implementation:            
        
        prompt = self._processor.apply_chat_template(messages, add_generation_prompt=True)
        
        inputs = self._processor(images=images if len(images) > 0 else None, text=prompt, return_tensors="pt", truncation=True)

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        output_ids = self.model.generate(**inputs, **gen_kwargs)
        
        input_ids = inputs["input_ids"]
        output_ids = output_ids[0][len(input_ids[0]):]
        
        response = self.tokenizer.decode(output_ids, skip_special_tokens=True)
        
        eval_logger.debug(response)
        
        return response
