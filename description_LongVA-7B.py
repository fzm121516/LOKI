import torch
import os
import random
import json
from tqdm import tqdm
import numpy as np
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

# 设置随机种子
seed = 42
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False



from longva.model.builder import load_pretrained_model
from longva.mm_utils import tokenizer_image_token, process_images
from longva.constants import IMAGE_TOKEN_INDEX
from PIL import Image
from decord import VideoReader, cpu
import torch
import numpy as np


model_path = "/root/zgp2/fanzheming/LVLM/LongVA-7B"
# image_path = "local_demo/assets/lmms-eval.png"
# video_path = "local_demo/assets/dc_demo.mp4"
max_frames_num = 16 # you can change this to several thousands so long you GPU memory can handle it :)
gen_kwargs = {"do_sample": False, "num_beams": 1, "use_cache": True, "max_new_tokens": 1024}
tokenizer, model, image_processor, _ = load_pretrained_model(model_path, None, "llava_qwen", device_map="cuda:0")

prompt_part0 = "You are shown a video."
prompt_part1 = "Please describe the content of this video in detail."


@torch.inference_mode()
def generate_description(video_path):
    #video input
    prompt = "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<image>\nYou are shown a video. Please describe the content of this video in detail.<|im_end|>\n<|im_start|>assistant\n"
    input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors="pt").unsqueeze(0).to(model.device)
    vr = VideoReader(video_path, ctx=cpu(0))
    total_frame_num = len(vr)
    uniform_sampled_frames = np.linspace(0, total_frame_num - 1, max_frames_num, dtype=int)
    frame_idx = uniform_sampled_frames.tolist()
    frames = vr.get_batch(frame_idx).asnumpy()
    video_tensor = image_processor.preprocess(frames, return_tensors="pt")["pixel_values"].to(model.device, dtype=torch.float16)
    with torch.inference_mode():
        output_ids = model.generate(input_ids, images=[video_tensor],  modalities=["video"], **gen_kwargs)
    outputs = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0].strip()
    print(outputs)

    
    return outputs





def process_videos(json_path):
    # 读取JSON文件
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # 为每个视频生成描述
    for item in tqdm(data, desc="Processing videos"):
        video_path = item.get("video_path")
        if video_path:
            try:
                description = generate_description(video_path)
                item["description"] = description
                print(f"Processed {video_path}: {description[:50]}...")  # 打印前50个字符作为预览
            except Exception as e:
                print(f"Error processing {video_path}: {str(e)}")
                item["description"] = f"Error: {str(e)}"
    
    # 保存回JSON文件
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Descriptions saved to {json_path}")

if __name__ == "__main__":
    json_path = "one_path_longva.json"
    process_videos(json_path)