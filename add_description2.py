import json

# 读取JSON文件
with open('true_or_false_with_description.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 处理每个条目
for item in data:
    if 'description' in item and 'question' in item:
        # 找到<video>\n的位置
        video_tag_pos = item['question'].find('<video>\n')
        if video_tag_pos != -1:
            # 在<video>\n后面插入description内容
            insert_pos = video_tag_pos + len('<video>\n')
            new_question = (item['question'][:insert_pos] + 
                           item['description'] + 
                           item['question'][insert_pos:])
            item['question'] = new_question
        
        # 删除description字段
        del item['description']

# 保存修改后的JSON文件
with open('true_or_false_modified.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("处理完成，结果已保存到true_or_false_modified.json")