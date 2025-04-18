import json

# 1. 从本地读取原始JSON文件
input_file = 'true_or_false.json'  # 替换为你的输入文件路径
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. 对video_path去重并提取
unique_videos = []
seen_paths = set()

for item in data:
    path = item["video_path"]
    if path not in seen_paths:
        seen_paths.add(path)
        unique_videos.append({"video_path": path})

# 3. 保存到新的JSON文件
output_file = 'one_path.json'  # 替换为你想要的输出文件路径
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(unique_videos, f, indent=2, ensure_ascii=False)

print(f"处理完成！共找到 {len(unique_videos)} 个唯一视频路径，已保存到 {output_file}")