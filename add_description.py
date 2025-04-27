import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def merge_descriptions(main_json, desc_json):
    # 创建video_path到描述的映射字典
    desc_map = {item['video_path']: item.get('description', '') for item in desc_json}
    
    # 更新主JSON中的条目
    for item in main_json:
        video_path = item['video_path']
        item['description'] = desc_map.get(video_path, '')
    
    return main_json

if __name__ == "__main__":
    # 输入文件路径
    main_json_path = "true_or_false.json"  # 第一个JSON文件路径
    desc_json_path = "one_path_mplug.json"  # 第二个JSON文件路径
    output_json_path = "true_or_false_with_description_mplug.json"  # 输出文件路径
    
    # 加载JSON文件
    main_json = load_json(main_json_path)
    desc_json = load_json(desc_json_path)
    
    # 合并描述
    merged_json = merge_descriptions(main_json, desc_json)
    
    # 保存结果
    save_json(merged_json, output_json_path)
    print(f"处理完成，结果已保存到 {output_json_path}")