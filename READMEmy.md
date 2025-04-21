


CUDA_VISIBLE_DEVICES=0 python description_Qwen2.5-VL-7B-Instruct.py







python run.py --model_config_path configs/models/qwen2.5_vl_config.yaml --task_config_path configs/tasks/image/image_tf_loki.yaml --batch_size 1





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



这下面都是qwen2vl


python run.py --model_config_path configs/models/qwen2_vl_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

025-04-10 21:24:54.328 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8611111111111112
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.2692307692307692
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9545454545454546
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.17045454545454544
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-10 21:24:54.329 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9264705882352942
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.27941176470588236
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9078947368421053
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.2804878048780488
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.14150943396226415
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8780487804878049
2025-04-10 21:24:54.330 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.44505494505494503
2025-04-10 21:24:54.331 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-10 21:24:54.331 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 21:24:54.331 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-10 21:24:54.331 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.92
2025-04-10 21:24:54.331 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.375
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 335438.84it/s]
2025-04-10 21:24:54.396 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
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

Model Responding: 100%|__________________________________________________________________________________________________________________________________________________________________________| 1272/1272 [11:32<00:00,  1.84it/s]
(loki) root@jwelueqgpocydvpx-wind-7db595f75c-6slhn:/data/LOKI# 




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




python run.py --model_config_path configs/models/qwen2_vl_pro2022_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7222222222222222
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5192307692307693
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8333333333333334
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5454545454545454
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-10 21:40:14.751 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7352941176470589
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6176470588235294
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.75
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.4024390243902439
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.8
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.4056603773584906
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6707317073170732
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5879120879120879
2025-04-10 21:40:14.752 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-10 21:40:14.753 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-10 21:40:14.753 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-10 21:40:14.753 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.58
2025-04-10 21:40:14.753 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6145833333333334
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 353719.73it/s]
2025-04-10 21:40:14.810 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6278290242618065|
|CogVideoX                                            |  88|0.6207264957264957|
|keling                                               | 242|0.6893939393939394|
|Lumiere                                              | 136|0.6764705882352942|
|Sora                                                 | 240|0.5762195121951219|
|open-sora                                            | 156|0.6028301886792453|
|Photorealistic Video Generation with Diffusion Models| 264|0.6293218976145806|
|runway                                               | 146|0.5972916666666667|

Model Responding: 100%|__________________________________________________________________________________________________________________________________________________________________________| 1272/1272 [13:00<00:00,  1.63it/s]
(loki) root@jwelueqgpocydvpx-wind-7db595f75c-6slhn:/data/LOKI# 



python run.py --model_config_path configs/models/qwen2_vl_pro2022_config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1


025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                           | 0/428 [00:00<?, ?it/s]
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 18
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 18
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5555555555555556
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7222222222222222
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 33
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 33
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5757575757575758
2025-04-10 21:54:52.342 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.42424242424242425
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 34
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 34
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5882352941176471
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7941176470588235
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 38
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 38
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5789473684210527
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5526315789473685
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.56
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.52
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 41
2025-04-10 21:54:52.343 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 41
2025-04-10 21:54:52.344 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6341463414634146
2025-04-10 21:54:52.344 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7073170731707317
2025-04-10 21:54:52.344 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-10 21:54:52.344 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-10 21:54:52.344 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-10 21:54:52.344 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.72
2025-04-10 21:54:52.344 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.88
Aggregating Results: 100%|_____________________________________________________________________________________________________________________________________________________________________| 428/428 [00:00<00:00, 156318.54it/s]
2025-04-10 21:54:52.400 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num|     Accuracy     |
|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.6261682242990654|
|CogVideoX                                            | 36|0.6388888888888888|
|keling                                               | 66|0.5000000000000000|
|Lumiere                                              | 68|0.6911764705882353|
|Sora                                                 | 76|0.5657894736842106|
|open-sora                                            | 50|0.5400000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.6707317073170731|
|runway                                               | 50|0.8000000000000000|

Model Responding: 100%|____________________________________________________________________________________________________________________________________________________________________________| 428/428 [10:46<00:00,  1.51s/it]
(loki) root@jwelueqgpocydvpx-wind-7db595f75c-6slhn:/data/LOKI# 




python run.py --model_config_path configs/models/qwen2.5_vl_sft2245_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1



025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5277777777777778
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7884615384615384
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-11 18:33:35.759 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.6363636363636364
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6818181818181818
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7352941176470589
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7352941176470589
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.618421052631579
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6036585365853658
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.82
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5283018867924528
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.4634146341463415
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.9340659340659341
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.62
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7291666666666666
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.82
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5283018867924528
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-11 18:33:35.760 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.4634146341463415
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.9340659340659341
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.62
2025-04-11 18:33:35.761 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7291666666666666
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 355179.73it/s]
2025-04-11 18:33:35.821 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6680372988688729|
|CogVideoX                                            |  88|0.6581196581196581|
|keling                                               | 242|0.6590909090909091|
|Lumiere                                              | 136|0.7352941176470589|
|Sora                                                 | 240|0.6110397946084725|
|open-sora                                            | 156|0.6741509433962264|
|Photorealistic Video Generation with Diffusion Models| 264|0.6987402841061378|
|runway                                               | 146|0.6745833333333333|

Model Responding: 100%|__________________________________________________________________________________________________________________________________________________________________________| 1272/1272 [11:15<00:00,  1.88it/s]
(loki) root@qjurrydgeijcrlxp-wind-56dc5c96dd-r2w4j:/data/LOKI# 



python run.py --model_config_path configs/models/qwen2.5_vl_sft2245_config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1




CUDA_VISIBLE_DEVICES=0 python run.py --model_config_path configs/models/qwen2_vl_sft900base_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                           | 0/428 [00:00<?, ?it/s]
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 18
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 18
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7777777777777778
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.6666666666666666
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 33
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 33
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.696969696969697
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.5757575757575758
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-15 06:28:34.145 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 34
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 34
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.9117647058823529
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.9117647058823529
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 38
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 38
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.631578947368421
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7105263157894737
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.68
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.76
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 41
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 41
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.7073170731707317
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.7804878048780488
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 25
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 25
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.68
2025-04-15 06:28:34.146 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.72
Aggregating Results: 100%|_____________________________________________________________________________________________________________________________________________________________________| 428/428 [00:00<00:00, 261342.57it/s]
2025-04-15 06:28:34.271 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num|     Accuracy     |
|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.7313084112149533|
|CogVideoX                                            | 36|0.7222222222222222|
|keling                                               | 66|0.6363636363636365|
|Lumiere                                              | 68|0.9117647058823529|
|Sora                                                 | 76|0.6710526315789473|
|open-sora                                            | 50|0.7200000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.7439024390243902|
|runway                                               | 50|0.7000000000000000|

CUDA_VISIBLE_DEVICES=1 python run.py --model_config_path configs/models/qwen2_vl_sft900base_config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1

025-04-15 06:30:20.591 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: CogVideoX                                                                                                          | 0/1272 [00:00<?, ?it/s]
2025-04-15 06:30:20.591 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 36
2025-04-15 06:30:20.591 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 52
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.1111111111111111
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 1.0
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: keling
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 66
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 176
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.25757575757575757
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.9886363636363636
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Lumiere
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 68
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 68
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5294117647058824
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 1.0
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Sora
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 76
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 164
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.23684210526315788
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.8414634146341463
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: open-sora
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 106
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.42
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 1.0
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: Photorealistic Video Generation with Diffusion Models
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 82
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 182
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.3170731707317073
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 1.0
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:609 - Type: runway
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:627 - Real Num: 50
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:628 - Fake Num: 96
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:630 - Real Acc: 0.5
2025-04-15 06:30:20.592 | INFO     | lm_evaluate.tasks.loki:aggregate_results:631 - Fake Acc: 0.9895833333333334
Aggregating Results: 100%|___________________________________________________________________________________________________________________________________________________________________| 1272/1272 [00:00<00:00, 544570.24it/s]
2025-04-15 06:30:20.650 | INFO     | lm_evaluate.tasks.loki:print_pretty_accuracy:669 - 
|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6464339653124643|
|CogVideoX                                            |  88|0.5555555555555556|
|keling                                               | 242|0.6231060606060606|
|Lumiere                                              | 136|0.7647058823529411|
|Sora                                                 | 240|0.5391527599486521|
|open-sora                                            | 156|0.7100000000000000|
|Photorealistic Video Generation with Diffusion Models| 264|0.6585365853658537|
|runway                                               | 146|0.7447916666666667|



CUDA_VISIBLE_DEVICES=2 python3 run.py --model_config_path configs/models/qwen2_vl_onlymerger900_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1




CUDA_VISIBLE_DEVICES=2 python3 run.py --model_config_path configs/models/qwen2_vl_vitandmerger_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1
