pip install -e .

pip install transformers==4.55.2

pip install flash-attn --no-build-isolation

pip install qwen_vl_utils

pip install peft

CUDA_VISIBLE_DEVICES=7 python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml  --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

CUDA_VISIBLE_DEVICES=7 python run.py --model_config_path configs/models/qwen2_vl_final_config.yaml  --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1