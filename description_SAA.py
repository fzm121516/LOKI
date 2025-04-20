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

# 加载模型
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "/root/zgp2/fanzheming/LLaMA-Factory/saves/Qwen2-VL-7B-Instruct/lora/trainDVFmc3_2025-04-16-18-27-79/checkpoint-900",
    torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
    device_map="auto",
)

# 加载处理器
processor = AutoProcessor.from_pretrained("/root/zgp2/fanzheming/LLaMA-Factory/saves/Qwen2-VL-7B-Instruct/lora/trainDVFmc3_2025-04-16-18-27-79/checkpoint-900")

# 参数设置
max_pixels = 360 * 420
fps = 1.0
prompt_part0 = "You are shown a video."
prompt_part1 = "Please describe the content of this video in detail."

@torch.inference_mode()
def generate_description(video_path):
    # 构造消息
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_part0},
                {
                    "type": "video",
                    "video": video_path,
                    "max_pixels": max_pixels,
                    "fps": fps,
                },
                {"type": "text", "text": prompt_part1},
            ],
        }
    ]

    # 准备输入
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
        **video_kwargs,
    )
    inputs = inputs.to("cuda")

    # 生成参数
    generation_args = { 
        "max_new_tokens": 1000, 
        "temperature": 0.0, 
        "do_sample": False, 
    }
    
    # 生成描述
    generated_ids = model.generate(**inputs, **generation_args)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    
    return output_text

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
    json_path = "one_path_SAA.json"
    process_videos(json_path)