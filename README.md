

python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml --task_config_path configs/tasks/image/image_tf_loki.yaml --batch_size 1


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






python run.py --model_config_path configs/models/qwen2.5_vl_sft1347_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1


025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6944444444444444
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.8076923076923077
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6212121212121212
2025-04-10 06:16:38.925 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6022727272727273
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6911764705882353
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7058823529411765
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6052631578947368
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.524390243902439
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.44339622641509435
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-10 06:16:38.926 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-10 06:16:38.927 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.47560975609756095
2025-04-10 06:16:38.927 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.8736263736263736
2025-04-10 06:16:38.927 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-10 06:16:38.927 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 06:16:38.927 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-10 06:16:38.927 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.72
2025-04-10 06:16:38.927 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6770833333333334
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 352271.69it/s]
2025-04-10 06:16:38.999 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6428842286427352|
|CogVideoX                                            |  88|0.7510683760683761|
|keling                                               | 242|0.6117424242424243|
|Lumiere                                              | 136|0.6985294117647058|
|Sora                                                 | 240|0.5648267008985879|
|open-sora                                            | 156|0.6216981132075472|
|Photorealistic Video Generation with Diffusion Models| 264|0.6746180648619673|
|runway                                               | 146|0.6985416666666666|


