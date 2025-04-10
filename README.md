

python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml --task_config_path configs/tasks/image/image_tf_loki.yaml --batch_size 1



python run.py --model_config_path configs/models/qwen2_vl_config.yaml   --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1


025-04-10 14:11:29.712 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                           | 0/428 [00:00<?, ?it/s]
2025-04-10 14:11:29.712 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 18
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 18
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6111111111111112
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 33
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 33
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.696969696969697
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5454545454545454
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 34
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 34
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7941176470588235
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6176470588235294
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 38
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 38
2025-04-10 14:11:29.713 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6578947368421053
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6578947368421053
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.68
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 41
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 41
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6097560975609756
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6097560975609756
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.76
2025-04-10 14:11:29.714 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6
Aggregating Results: 100%|_____________________________________________________________________________________________________________________________________________________________________| 428/428 [00:00<00:00, 149385.21it/s]
2025-04-10 14:11:29.774 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num|     Accuracy     |
|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.6425233644859814|
|CogVideoX                                            | 36|0.5555555555555556|
|keling                                               | 66|0.6212121212121212|
|Lumiere                                              | 68|0.7058823529411764|
|Sora                                                 | 76|0.6578947368421053|
|open-sora                                            | 50|0.6400000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.6097560975609756|
|runway                                               | 50|0.6799999999999999|



python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml   --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1

2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 18
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 18
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5555555555555556
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5555555555555556
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 33
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 33
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.36363636363636365
2025-04-10 13:20:19.553 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5454545454545454
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 34
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 34
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6176470588235294
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5882352941176471
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 38
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 38
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5789473684210527
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6578947368421053
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.68
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 41
2025-04-10 13:20:19.554 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 41
2025-04-10 13:20:19.555 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6829268292682927
2025-04-10 13:20:19.555 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5609756097560976
2025-04-10 13:20:19.555 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-10 13:20:19.555 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-10 13:20:19.555 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-10 13:20:19.555 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.72
2025-04-10 13:20:19.555 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.72
Aggregating Results: 100%|_____________________________________________________________________________________________________________________________________________________________________| 428/428 [00:00<00:00, 152701.78it/s]
2025-04-10 13:20:19.613 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num|     Accuracy      |
|-----------------------------------------------------|--:|------------------:|
|total_accuracy                                       |428|0.60046728971962620|
|CogVideoX                                            | 36|0.55555555555555560|
|keling                                               | 66|0.45454545454545453|
|Lumiere                                              | 68|0.60294117647058830|
|Sora                                                 | 76|0.61842105263157900|
|open-sora                                            | 50|0.64000000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.62195121951219520|
|runway                                               | 50|0.72000000000000000|

Model Responding: 100%|____________________________________________________________________________________________________________________________________________________________________________| 428/428 [09:29<00:00,  1.33s/it]
(loki) root@jwelueqgpocydvpx-wind-7db595f75c-6slhn:/data/LOKI# 


python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml  --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

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


python run.py --model_config_path configs/models/qwen2.5_vl_sft2245_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

python run.py --model_config_path configs/models/qwen2.5_vl_sft2245_config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1

025-04-10 12:53:22.207 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-10 12:53:22.207 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-10 12:53:22.207 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6666666666666666
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.8269230769230769
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6515151515151515
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6136363636363636
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7205882352941176
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.75
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-10 12:53:22.208 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5789473684210527
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5975609756097561
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.84
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.4528301886792453
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.4634146341463415
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.9010989010989011
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.66
2025-04-10 12:53:22.209 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6770833333333334
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 321685.54it/s]
2025-04-10 12:53:22.283 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6558188182280925|
|CogVideoX                                            |  88|0.7467948717948718|
|keling                                               | 242|0.6325757575757576|
|Lumiere                                              | 136|0.7352941176470589|
|Sora                                                 | 240|0.5882541720154044|
|open-sora                                            | 156|0.6464150943396226|
|Photorealistic Video Generation with Diffusion Models| 264|0.6822567676226213|
|runway                                               | 146|0.6685416666666667|

