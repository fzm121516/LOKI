import json

with open('true_or_false.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if 'question' in item:
        video_tag_pos = item['question'].find('<video>\n')
        if video_tag_pos != -1:
            insert_pos = video_tag_pos + len('<video>\n')
            
            # 使用固定提示语替代 description
            fixed_prompt = "Do not consider the video semantics."
            
            new_question = (
                item['question'][:insert_pos] + 
                fixed_prompt + "\n" +  # 这里加 \n
                item['question'][insert_pos:]
            )
            item['question'] = new_question
        


with open('true_or_false_ssp.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("处理完成")