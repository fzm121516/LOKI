import json
from collections import defaultdict
from tqdm import tqdm

def calculate_accuracy_by_model(json_file):
    """
    Calculate accuracy metrics from evaluation results JSON file.
    
    Args:
        json_file (str): Path to JSON file containing evaluation results
        
    Returns:
        dict: Dictionary containing accuracy metrics at different levels
    """
    # Load the JSON data
    with open(json_file, 'r') as f:
        results = json.load(f)
    
    # Initialize dictionaries to store accuracy metrics
    per_metric_accuracy = defaultdict(list)
    per_question_type_accuracy = defaultdict(list)
    fake_type_accuracy = defaultdict(list)
    real_type_accuracy = defaultdict(list)
    
    # Process each result
    for result in tqdm(results, desc="Calculating accuracy"):
        question_type = result['doc']['question_type']
        metric = result['doc']['metric']
        modality = result['doc']['modality']
        
        result_accuracy = result['accuracy']
        
        # Categorize by fake/real type
        if 'fake_ask' in question_type:
            # It's a question about fake stuff
            fake_type = question_type.split('_')[-1] if modality != 'text-only' else question_type.split('_')[-2]
            fake_type_accuracy[fake_type].append(result_accuracy)
        elif 'real_ask' in question_type:
            real_type = question_type.split("_")[-1]
            real_type_accuracy[real_type].append(result_accuracy)
        
        # Store per metric and per question type accuracy
        per_metric_accuracy[metric].append(result_accuracy)
        per_question_type_accuracy[question_type].append(result_accuracy)
    
    # Calculate aggregated metrics
    total_real_num = 0
    total_fake_num = 0
    total_accuracy = 0
    
    final_metrics = defaultdict(dict)
    
    # Process fake and real type accuracies
    for fake_key, fake_value in fake_type_accuracy.items():
        fake_accuracy = sum(fake_value) / len(fake_value)
        fake_num = len(fake_value)
        
        if fake_key not in real_type_accuracy.keys():
            real_num = 0
            real_accuracy = fake_accuracy
        else:
            real_value = real_type_accuracy[fake_key]
            real_accuracy = sum(real_value) / len(real_value) 
            real_num = len(real_value)

        total_real_num += real_num
        total_fake_num += fake_num
        
        final_metrics['per_metric'][fake_key] = {
            'accuracy': (fake_accuracy + real_accuracy) / 2, 
            'num': fake_num + real_num
        }
        
        total_accuracy += fake_num * (fake_accuracy + real_accuracy) / 2
    
    # Calculate total accuracy if there are fake questions
    if total_fake_num > 0:
        total_accuracy /= total_fake_num
    total_num = total_real_num + total_fake_num
    
    # Add total accuracy to metrics
    final_metrics['total'] = {
        "accuracy": total_accuracy,
        "num": total_num
    }
    
    # Calculate per-metric accuracy (original metrics)
    for metric, accuracies in per_metric_accuracy.items():
        final_metrics['original_metrics'][metric] = {
            'accuracy': sum(accuracies) / len(accuracies),
            'num': len(accuracies)
        }
    
    # Calculate per-question-type accuracy
    for q_type, accuracies in per_question_type_accuracy.items():
        final_metrics['per_question_type'][q_type] = {
            'accuracy': sum(accuracies) / len(accuracies),
            'num': len(accuracies)
        }
    
    return final_metrics

# 使用示例
json_file = 'qwen2_5_vl_lora_sft_5618_loki-video-tf_result.json'
accuracy_results = calculate_accuracy_by_model(json_file)
print(json.dumps(accuracy_results, indent=4, sort_keys=True))


