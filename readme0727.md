CUDA_VISIBLE_DEVICES=5 python process_videos.py \
  --input_dir ./media_data/video \
  --output_dir ./media_data/video_noise \
  --transform noise \
  --sigma 10 



CUDA_VISIBLE_DEVICES=5 python process_videos.py \
  --input_dir ./media_data/video_ori \
  --output_dir ./media_data/video_blur_33 \
  --transform blur \
  --ksize 3 \
  --sigmaX 1 


|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.7520941398114406|
|CogVideoX                                            |  88|0.7500000000000000|
|keling                                               | 242|0.7320075757575757|
|Lumiere                                              | 136|0.9191176470588236|
|Sora                                                 | 240|0.6251604621309370|
|open-sora                                            | 156|0.8111320754716982|
|Photorealistic Video Generation with Diffusion Models| 264|0.8048780487804879|
|runway                                               | 146|0.7233333333333334|

|                        Type                         |Num|     Accuracy      |
|-----------------------------------------------------|--:|------------------:|
|total_accuracy                                       |428|0.78037383177570100|
|CogVideoX                                            | 36|0.86111111111111120|
|keling                                               | 66|0.69696969696969700|
|Lumiere                                              | 68|0.91176470588235290|
|Sora                                                 | 76|0.48684210526315785|
|open-sora                                            | 50|0.84000000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.89024390243902430|
|runway                                               | 50|0.86000000000000000|


CUDA_VISIBLE_DEVICES=5 python process_videos.py \
  --input_dir ./media_data/video \
  --output_dir ./media_data/video_resize \
  --transform resize \
  --scale 0.25 

|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.7545977073265370|
|CogVideoX                                            |  88|0.6527777777777778|
|keling                                               | 242|0.7130681818181819|
|Lumiere                                              | 136|0.9338235294117647|
|Sora                                                 | 240|0.6132862644415917|
|open-sora                                            | 156|0.8252830188679245|
|Photorealistic Video Generation with Diffusion Models| 264|0.8231707317073171|
|runway                                               | 146|0.7922916666666666|

|                        Type                         |Num|     Accuracy     |
|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.7873831775700935|
|CogVideoX                                            | 36|0.9444444444444444|
|keling                                               | 66|0.7272727272727273|
|Lumiere                                              | 68|0.8970588235294117|
|Sora                                                 | 76|0.5000000000000000|
|open-sora                                            | 50|0.8200000000000001|
|Photorealistic Video Generation with Diffusion Models| 82|0.8658536585365854|
|runway                                               | 50|0.8800000000000000|





CUDA_VISIBLE_DEVICES=5 python process_videos.py \
  --input_dir ./media_data/video \
  --output_dir ./media_data/video_compressed \
  --transform compressed \
  --bitrate 300k 


CUDA_VISIBLE_DEVICES=5 python run.py --model_config_path configs/models/saa2_qwen2.config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

CUDA_VISIBLE_DEVICES=6 python run.py --model_config_path configs/models/saa2_qwen2.config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1