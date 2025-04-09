

python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1


025-04-09 01:05:25.917 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8333333333333334
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.3076923076923077
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 1.0
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.16477272727272727
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-09 01:05:25.918 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9117647058823529
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.23529411764705882
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9210526315789473
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.24390243902439024
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.88
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.1792452830188679
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8902439024390244
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.35714285714285715
2025-04-09 01:05:25.919 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-09 01:05:25.920 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 01:05:25.920 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-09 01:05:25.920 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.94
2025-04-09 01:05:25.920 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.3958333333333333
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 346191.34it/s]
2025-04-09 01:05:25.978 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.5929682198792554|
|CogVideoX                                            |  88|0.5705128205128205|
|keling                                               | 242|0.5823863636363636|
|Lumiere                                              | 136|0.5735294117647058|
|Sora                                                 | 240|0.5824775353016688|
|open-sora                                            | 156|0.5296226415094340|
|Photorealistic Video Generation with Diffusion Models| 264|0.6236933797909407|
|runway                                               | 146|0.6679166666666666|




python run.py --model_config_path configs/models/qwen2.5_vl_sft2800_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1


python run.py --model_config_path configs/models/qwen2.5_vl_sft_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

025-04-09 18:14:58.990 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-09 18:14:58.990 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8333333333333334
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.4230769230769231
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8181818181818182
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.3409090909090909
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7941176470588235
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.4117647058823529
2025-04-09 18:14:58.991 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7631578947368421
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.47560975609756095
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.74
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.4056603773584906
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7560975609756098
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.489010989010989
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 18:14:58.992 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-09 18:14:58.993 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.78
2025-04-09 18:14:58.993 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.53125
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 323342.71it/s]
2025-04-09 18:14:59.050 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6092541375401281|
|CogVideoX                                            |  88|0.6282051282051282|
|keling                                               | 242|0.5795454545454546|
|Lumiere                                              | 136|0.6029411764705882|
|Sora                                                 | 240|0.6193838254172015|
|open-sora                                            | 156|0.5728301886792453|
|Photorealistic Video Generation with Diffusion Models| 264|0.6225542749932994|
|runway                                               | 146|0.6556250000000000|