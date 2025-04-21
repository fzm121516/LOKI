import json

with open('true_or_false_with_description_qwen2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if 'description' in item and 'question' in item:
        video_tag_pos = item['question'].find('<video>\n')
        if video_tag_pos != -1:
            insert_pos = video_tag_pos + len('<video>\n')
            
            # 确保 description 是字符串，并在后面加 \n
            description = item['description']
            if isinstance(description, list):
                description = " ".join(description)  # 或者 "".join(description)
            
            new_question = (
                item['question'][:insert_pos] + 
                description + "\n" +  # 这里加 \n
                item['question'][insert_pos:]
            )
            item['question'] = new_question
        
        del item['description']

with open('true_or_false_with_description_qwen2_test.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("处理完成，结果已保存到 true_or_false_modified.json")

