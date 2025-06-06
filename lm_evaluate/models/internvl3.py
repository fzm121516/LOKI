import copy
import json
import re
import sys

import torch
import transformers

import numpy as np

from collections import Counter
from typing import List, Union, Optional
from copy import deepcopy
from datetime import timedelta
from packaging import version

from lm_evaluate.api.model import LMM
from lm_evaluate.api.registry import register_model

from decord import VideoReader, cpu
from accelerate import Accelerator, DistributedType
from accelerate.utils import InitProcessGroupKwargs
from accelerate.state import AcceleratorState
from loguru import logger as eval_logger
try:
    from transformers import AutoModelForCausalLM, AutoProcessor,AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig,InternVLForConditionalGeneration
    from transformers import Qwen2_5_VLForConditionalGeneration, AutoTokenizer, AutoProcessor
    from qwen_vl_utils import process_vision_info
except Exception as e:
    eval_logger.debug(f"Upgrade transformers to use qwen2_5_vl. {e}")
from PIL import Image

if version.parse(transformers.__version__) < version.parse("4.43.0"):
    eval_logger.debug("Please upgrade transformers to use Phi-3.5-Vision")


@register_model("internvl3")
class InternVL3(LMM):
    supported_modalities = ["video", "image", "text"]
    support_batching = True
    def __init__(
        self,
        model_version: str = "/root/zgp2/fanzheming/LVLM/InternVL3-8B-hf",
        device: str = "cuda",
        device_map: str = "cuda",
        dtype: Optional[Union[str, torch.dtype]] = "auto",
        attn_implementation: Optional[str] ='flash_attention_2',
        truncation: bool = True
    ):
        self.model_version = model_version
        
        if isinstance(dtype, str) and dtype != "auto":
            dtype = getattr(torch, dtype)
        
        self._device = device
        self.device_map = device_map
        self.dtype = dtype
            
        self.attn_implementation = attn_implementation
        self.truncation = truncation
        
        
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
        
        self._model = AutoModelForImageTextToText.from_pretrained(self.model_version, device_map=self.device_map, torch_dtype=self.dtype, attn_implementation=self.attn_implementation)
        self._model.eval()
        
        self.processor = AutoProcessor.from_pretrained(self.model_version)
        # self.processor.tokenizer.padding_side = "left"
        
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
    def device(self):
        return self._device
    

    def generate(
        self, 
        visuals: Union[Image.Image, str, List[Union[Image.Image, str]]],
        contexts: str,
        **kwargs
    ) -> str:
        """
            Call qwen2_5_vl for response with visuals and contexts. Visuals can be a list of strings(representing video paths), or a list of PIL.Image.Image or a combination of both. Returns a piece of response text.
            
            Args:
                visuals: Media objects. Visuals can be one image, one video path, or a list of them. 
                contexts: Prompt text.
                kwargs: Generation kwargs. Currently we only support greedy decoding. # TODO: Support diverse decoding strategy.
            Return:
                A piece of response text
        """
        
        images = []
        videos = []
        
        num_videos = 0
        num_images = 0
        # four scenarios:
        # visuals is a list of string or PIL image
        # visuals is a string
        # visuals is a PIL Image
        # visuals is None
        if isinstance(visuals, list):
            for visual in visuals:
                if isinstance(visual, str):
                    videos.append(visual)
                elif isinstance(visual, Image.Image):
                    images.append(visual)
                    num_images += 1
                else:
                    error_msg = f"Expected visual type to be Image.Image or str. Got: {type(visual)}"
                    eval_logger.error(TypeError(error_msg))
        elif isinstance(visuals, str):
            videos.append(visuals)
        elif isinstance(visuals, Image.Image):
            images.append(visuals)
            num_images += 1
        
        # Segment the text according to video and image token
        
        
        if num_images > contexts.count('<image>'):
            eval_logger.warning(f"<image> tokens num is less than actual number of images. Appending {num_images - contexts.count('<image>')} <image> at the front.")
            contexts = "<image> " * (num_images - contexts.count("<image>")) + contexts

        if num_videos > contexts.count("<video>"):
            eval_logger.warning(f"<video> tokens num is less than actual number of images. Appending {num_videos - contexts.count('video')} <video> at the front.")
            contexts = "<video> " * (num_videos - contexts.count("<video>")) + contexts
        
        # First replace <video> token with <image> * num_frames
        contexts = re.split(r"(<video>|<image>)", contexts)
        contexts = [context for context in contexts if context]
        
        messages = [
            {
                "role": "user",
                "content": []
            }
        ]
        video_idx = 0
        image_idx = 0
        for i, context in enumerate(contexts):
            if context == "<video>":
                messages[0]["content"].append(
                    {
                        "type": "video",
                        "url": videos[video_idx],

                    }
                )
                video_idx += 1
            elif context == "<image>":
                messages[0]["content"].append(
                    {
                        "type": "image",
                        "image": images[image_idx]
                    }
                )
                image_idx += 1
        
            else:
                messages[0]["content"].append(
                    {
                        "type": "text",
                        "text": context
                    }
                )
        print(messages)



        inputs = self.processor.apply_chat_template(
            messages,
            padding=True,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(self.model.device, dtype=torch.bfloat16)

        outputs = self.model.generate(**inputs, max_new_tokens=25)

        decoded_outputs = self.processor.batch_decode(outputs, skip_special_tokens=True)
        result = decoded_outputs[0].split('assistant\n')[-1]
        print(result)  

        return result

        
        