CUDA_VISIBLE_DEVICES=5


CUDA_VISIBLE_DEVICES=0 python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml  --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1


025-04-13 18:46:47.346 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-13 18:46:47.346 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-13 18:46:47.346 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-13 18:46:47.346 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8333333333333334
2025-04-13 18:46:47.346 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.3076923076923077
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 1.0
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.16477272727272727
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9117647058823529
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.23529411764705882
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9210526315789473
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.24390243902439024
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-13 18:46:47.347 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.88
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.1792452830188679
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8902439024390244
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.35714285714285715
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.94
2025-04-13 18:46:47.348 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.3958333333333333
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 340817.34it/s]
2025-04-13 18:46:47.413 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
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



CUDA_VISIBLE_DEVICES=0 python run.py --model_config_path configs/models/qwen2_vl_config.yaml  --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

025-04-13 19:07:31.334 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-13 19:07:31.334 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8611111111111112
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.2692307692307692
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9545454545454546
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.17045454545454544
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9264705882352942
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.27941176470588236
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9078947368421053
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.2804878048780488
2025-04-13 19:07:31.335 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.14150943396226415
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8780487804878049
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.44505494505494503
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.92
2025-04-13 19:07:31.336 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.375
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 353321.50it/s]
2025-04-13 19:07:31.393 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.5978657539506300|
|CogVideoX                                            |  88|0.5651709401709402|
|keling                                               | 242|0.5625000000000000|
|Lumiere                                              | 136|0.6029411764705883|
|Sora                                                 | 240|0.5941912708600771|
|open-sora                                            | 156|0.5207547169811321|
|Photorealistic Video Generation with Diffusion Models| 264|0.6615518627713750|
|runway                                               | 146|0.6475000000000000|



Total number of questions:  1307
Accuracy is 86.2
Accuracy on fake videos: 98.8
Accuracy on real videos: 73.5
----------------------------------------------------------------------------------------------------
Accuracy: 86.2
F1 Score: 87.8
Yes rate: 62.8
(torch) root@myrwyxgjhppiblne-wind-7c45878684-sqlbb:/data/Impossible-Videos# 


Total number of questions:  1307
Accuracy is 72.6
Accuracy on fake videos: 49.8
Accuracy on real videos: 95.7
----------------------------------------------------------------------------------------------------
Accuracy: 72.6
F1 Score: 64.6
Yes rate: 27.2
(loki) root@2ac0fc1f0849:~/zgp2/fanzheming/Impossible-Videos# 

Total number of questions:  1307
Accuracy is 72.5
Accuracy on fake videos: 49.3
Accuracy on real videos: 96.0
----------------------------------------------------------------------------------------------------
Accuracy: 72.5
F1 Score: 64.3
Yes rate: 26.8
(torch) root@myrwyxgjhppiblne-wind-7c45878684-sqlbb:/data/Impossible-Videos# 


CUDA_VISIBLE_DEVICES=1 python evalqwen2vl.py

qwen2vl-ipv

Total number of questions:  1307
Accuracy is 76.2
Accuracy on fake videos: 58.4
Accuracy on real videos: 94.2
----------------------------------------------------------------------------------------------------
Accuracy: 76.2
F1 Score: 71.2
Yes rate: 32.3
(loki) root@2ac0fc1f0849:~/zgp2/fanzheming/Impossible-Videos# 

CUDA_VISIBLE_DEVICES=1 python evalqwen2.5vl.py






CUDA_VISIBLE_DEVICES=0 /root/zgp1/miniconda3/envs/lf/bin/python run.py --model_config_path configs/models/qwen2_vl_sft1000_config.yaml  --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1