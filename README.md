

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


python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml --task_config_path configs/tasks/image/image_tf_loki.yaml --batch_size 1





python run.py --model_config_path configs/models/qwen2.5_vl_sft_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1


025-04-09 00:35:40.880 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.3333333333333333
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7115384615384616
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.45454545454545453
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5227272727272727
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-09 00:35:40.881 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5147058823529411
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6176470588235294
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.4473684210526316
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7195121951219512
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.52
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5943396226415094
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7527472527472527
2025-04-09 00:35:40.882 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-09 00:35:40.883 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 00:35:40.883 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-09 00:35:40.883 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5
2025-04-09 00:35:40.883 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7291666666666666
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 319508.61it/s]
2025-04-09 00:35:40.941 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy      |
|-----------------------------------------------------|---:|------------------:|
|total_accuracy                                       |1272|0.56802236634239630|
|CogVideoX                                            |  88|0.52243589743589750|
|keling                                               | 242|0.48863636363636365|
|Lumiere                                              | 136|0.56617647058823530|
|Sora                                                 | 240|0.58344030808729140|
|open-sora                                            | 156|0.55716981132075470|
|Photorealistic Video Generation with Diffusion Models| 264|0.62637362637362640|
|runway                                               | 146|0.61458333333333330|


python run.py --model_config_path configs/models/qwen2.5_vl_sft1200_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1


025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5277777777777778
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6818181818181818
2025-04-09 00:51:17.641 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.3352272727272727
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6617647058823529
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.4117647058823529
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.618421052631579
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5426829268292683
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.66
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.42452830188679247
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-09 00:51:17.642 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-09 00:51:17.643 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6585365853658537
2025-04-09 00:51:17.643 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6098901098901099
2025-04-09 00:51:17.643 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-09 00:51:17.643 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-09 00:51:17.643 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-09 00:51:17.643 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.66
2025-04-09 00:51:17.643 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6041666666666666
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 325870.67it/s]
2025-04-09 00:51:17.701 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.5705208267847209|
|CogVideoX                                            |  88|0.5138888888888888|
|keling                                               | 242|0.5085227272727273|
|Lumiere                                              | 136|0.5367647058823529|
|Sora                                                 | 240|0.5805519897304237|
|open-sora                                            | 156|0.5422641509433963|
|Photorealistic Video Generation with Diffusion Models| 264|0.6342133476279819|
|runway                                               | 146|0.6320833333333333|






