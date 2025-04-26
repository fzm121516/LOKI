import torch
import os
import random
import json
from tqdm import tqdm
import numpy as np


# 设置随机种子
seed = 42
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


prompt_part0 = "You are shown a video."
prompt_part1 = "Please describe the content of this video in detail."


import torch
from modelscope import AutoConfig, AutoModel
model_path = '/root/zgp2/fanzheming/LVLM/mPLUG-Owl3-7B-241101'
config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
print(config)
model = AutoModel.from_pretrained(model_path, attn_implementation='flash_attention_2', torch_dtype=torch.bfloat16, trust_remote_code=True)
_ = model.eval().cuda()
device = "cuda"


from PIL import Image
from modelscope import AutoTokenizer
from decord import VideoReader, cpu    # pip install decord
tokenizer = AutoTokenizer.from_pretrained(model_path)
processor = model.init_processor(tokenizer)
MAX_NUM_FRAMES=16

def encode_video(video_path):
    def uniform_sample(l, n):
        gap = len(l) / n
        idxs = [int(i * gap + gap / 2) for i in range(n)]
        return [l[i] for i in idxs]

    vr = VideoReader(video_path, ctx=cpu(0))
    sample_fps = round(vr.get_avg_fps() / 1)  # FPS
    frame_idx = [i for i in range(0, len(vr), sample_fps)]
    if len(frame_idx) > MAX_NUM_FRAMES:
        frame_idx = uniform_sample(frame_idx, MAX_NUM_FRAMES)
    frames = vr.get_batch(frame_idx).asnumpy()
    frames = [Image.fromarray(v.astype('uint8')) for v in frames]
    print('num frames:', len(frames))
    return frames
@torch.inference_mode()
def generate_description(video_path):
    # 构造消息



    messages = [
        {"role": "user", "content": """<|video|>
    You are shown a video. Please describe the content of this video in detail."""},
        {"role": "assistant", "content": ""}
    ]



    video_frames = [encode_video(video_path) ]
    inputs = processor(messages, images=None, videos=video_frames)

    inputs.to(device)
    inputs.update({
        'tokenizer': tokenizer,
        'max_new_tokens':100,
        'decode_text':True,
    })


    g = model.generate(**inputs)
    print(g)

    return g[0]

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
    json_path = "one_path_mplug.json"
    process_videos(json_path)