CUDA_VISIBLE_DEVICES=5 python process_videos.py \
  --input_dir ./media_data/video \
  --output_dir ./media_data/video_noise \
  --transform noise \
  --sigma 10 

|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.7113687360620177|
|CogVideoX                                            |  88|0.7222222222222222|
|keling                                               | 242|0.6856060606060606|
|Lumiere                                              | 136|0.9191176470588236|
|Sora                                                 | 240|0.5194159178433889|
|open-sora                                            | 156|0.8105660377358490|
|Photorealistic Video Generation with Diffusion Models| 264|0.7804878048780488|
|runway                                               | 146|0.6929166666666666|

|                        Type                         |Num|     Accuracy      |
|-----------------------------------------------------|--:|------------------:|
|total_accuracy                                       |428|0.76869158878504670|
|CogVideoX                                            | 36|0.91666666666666660|
|keling                                               | 66|0.71212121212121220|
|Lumiere                                              | 68|0.94117647058823530|
|Sora                                                 | 76|0.40789473684210525|
|open-sora                                            | 50|0.88000000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.86585365853658540|
|runway                                               | 50|0.78000000000000000|

CUDA_VISIBLE_DEVICES=5 python process_videos.py \
  --input_dir ./media_data/video_ori \
  --output_dir ./media_data/video_blur_33 \
  --transform blur \
  --ksize 3 \
  --sigmaX 1 


|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.7466141087701723|
|CogVideoX                                            |  88|0.6805555555555556|
|keling                                               | 242|0.7310606060606060|
|Lumiere                                              | 136|0.9411764705882353|
|Sora                                                 | 240|0.5827984595635430|
|open-sora                                            | 156|0.8352830188679246|
|Photorealistic Video Generation with Diffusion Models| 264|0.8048780487804879|
|runway                                               | 146|0.7445833333333334|

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

|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.7195459639929400|
|CogVideoX                                            |  88|0.6944444444444444|
|keling                                               | 242|0.6808712121212122|
|Lumiere                                              | 136|0.8529411764705883|
|Sora                                                 | 240|0.5813543003851090|
|open-sora                                            | 156|0.8205660377358490|
|Photorealistic Video Generation with Diffusion Models| 264|0.7439024390243902|
|runway                                               | 146|0.7879166666666667|


|                        Type                         |Num|     Accuracy     |
|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.7546728971962616|
|CogVideoX                                            | 36|0.8888888888888888|
|keling                                               | 66|0.7121212121212122|
|Lumiere                                              | 68|0.8676470588235294|
|Sora                                                 | 76|0.4605263157894737|
|open-sora                                            | 50|0.8400000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.8536585365853660|
|runway                                               | 50|0.7600000000000000|

CUDA_VISIBLE_DEVICES=5 python run.py --model_config_path configs/models/saa2_qwen2.config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

CUDA_VISIBLE_DEVICES=6 python run.py --model_config_path configs/models/saa2_qwen2.config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1





CUDA_VISIBLE_DEVICES=5 python process_videos.py \
  --input_dir ./media_data/video_ori \
  --output_dir ./media_data/video_crop_5 \
  --transform crop  \
  --crop_scale 5

|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6686289655862385|
|CogVideoX                                            |  88|0.5459401709401709|
|keling                                               | 242|0.6373106060606061|
|Lumiere                                              | 136|0.8161764705882353|
|Sora                                                 | 240|0.4849165596919127|
|open-sora                                            | 156|0.8000000000000000|
|Photorealistic Video Generation with Diffusion Models| 264|0.7256097560975610|
|runway                                               | 146|0.7487500000000000|

|                        Type                         |Num|     Accuracy     |
|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.7733644859813084|
|CogVideoX                                            | 36|0.8055555555555556|
|keling                                               | 66|0.8030303030303030|
|Lumiere                                              | 68|0.8235294117647058|
|Sora                                                 | 76|0.5263157894736843|
|open-sora                                            | 50|0.8200000000000001|
|Photorealistic Video Generation with Diffusion Models| 82|0.8536585365853660|
|runway                                               | 50|0.8400000000000000|






CUDA_VISIBLE_DEVICES=6 python process_videos.py \
  --input_dir ./media_data/video_ori \
  --output_dir ./media_data/video_crop_3 \
  --transform crop  \
  --crop_scale 3

|                        Type                         |Num |     Accuracy     |
|-----------------------------------------------------|---:|-----------------:|
|total_accuracy                                       |1272|0.6725301540368858|
|CogVideoX                                            |  88|0.5694444444444444|
|keling                                               | 242|0.6164772727272727|
|Lumiere                                              | 136|0.8897058823529411|
|Sora                                                 | 240|0.5338575096277278|
|open-sora                                            | 156|0.8000000000000000|
|Photorealistic Video Generation with Diffusion Models| 264|0.7073170731707317|
|runway                                               | 146|0.7075000000000000|


|                        Type                         |Num|     Accuracy      |
|-----------------------------------------------------|--:|------------------:|
|total_accuracy                                       |428|0.72196261682242990|
|CogVideoX                                            | 36|0.83333333333333330|
|keling                                               | 66|0.63636363636363650|
|Lumiere                                              | 68|0.83823529411764700|
|Sora                                                 | 76|0.39473684210526316|
|open-sora                                            | 50|0.84000000000000010|
|Photorealistic Video Generation with Diffusion Models| 82|0.80487804878048790|
|runway                                               | 50|0.84000000000000000|





CUDA_VISIBLE_DEVICES=6 python process_videos.py \
  --input_dir ./media_data/video_ori \
  --output_dir ./media_data/video_crop_7 \
  --transform crop  \
  --crop_scale 7


CUDA_VISIBLE_DEVICES=6 python run.py --model_config_path configs/models/saa2_qwen2.config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1
CUDA_VISIBLE_DEVICES=2 python run.py --model_config_path configs/models/saa2_qwen2.config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1




CUDA_VISIBLE_DEVICES=2 python run.py --model_config_path configs/models/qwen2_vl_config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1
|total_accuracy                                       |1272|0.5701664479852581|
|CogVideoX                                            |  88|0.5950854700854701|
|keling                                               | 242|0.5549242424242424|
|Lumiere                                              | 136|0.6323529411764706|
|Sora                                                 | 240|0.5024069319640565|
|open-sora                                            | 156|0.5298113207547170|
|Photorealistic Video Generation with Diffusion Models| 264|0.5599705172875904|
|runway                                               | 146|0.7202083333333333|

CUDA_VISIBLE_DEVICES=2 python run.py --model_config_path configs/models/qwen2_vl_config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1




CUDA_VISIBLE_DEVICES=5 python test_0803.py
CUDA_VISIBLE_DEVICES=2 python test_0803_real.py


CUDA_VISIBLE_DEVICES=5 python test_0803_text.py



saa01_qwen2.config.yaml

saaAB_qwen2.config.yaml


CUDA_VISIBLE_DEVICES=5 python run.py --model_config_path configs/models/saa01_qwen2.config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1
CUDA_VISIBLE_DEVICES=2 python run.py --model_config_path configs/models/saa01_qwen2.config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1
|total_accuracy                                       |1272|0.7201565177537532|
|CogVideoX                                            |  88|0.7756410256410255|
|keling                                               | 242|0.6619318181818181|
|Lumiere                                              | 136|0.8382352941176471|
|Sora                                                 | 240|0.5900192554557124|
|open-sora                                            | 156|0.8039622641509434|
|Photorealistic Video Generation with Diffusion Models| 264|0.8597560975609756|
|runway                                               | 146|0.5783333333333334|

|                        Type                         |Num|     Accuracy     |
|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.7009345794392523|
|CogVideoX                                            | 36|0.7222222222222222|
|keling                                               | 66|0.5303030303030303|
|Lumiere                                              | 68|0.8235294117647058|
|Sora                                                 | 76|0.4342105263157895|
|open-sora                                            | 50|0.8200000000000001|
|Photorealistic Video Generation with Diffusion Models| 82|0.9512195121951219|
|runway                                               | 50|0.6200000000000000|







CUDA_VISIBLE_DEVICES=5 python run.py --model_config_path configs/models/saaAB_qwen2.config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1
CUDA_VISIBLE_DEVICES=6 python run.py --model_config_path configs/models/saaAB_qwen2.config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1

|total_accuracy                                       |1272|0.7334316013900971|
|CogVideoX                                            |  88|0.7841880341880342|
|keling                                               | 242|0.7206439393939394|
|Lumiere                                              | 136|0.7794117647058824|
|Sora                                                 | 240|0.5287227214377407|
|open-sora                                            | 156|0.8033962264150943|
|Photorealistic Video Generation with Diffusion Models| 264|0.8841463414634146|
|runway                                               | 146|0.6835416666666666|

|-----------------------------------------------------|--:|-----------------:|
|total_accuracy                                       |428|0.7009345794392523|
|CogVideoX                                            | 36|0.7777777777777778|
|keling                                               | 66|0.6212121212121212|
|Lumiere                                              | 68|0.7500000000000000|
|Sora                                                 | 76|0.5526315789473684|
|open-sora                                            | 50|0.7400000000000000|
|Photorealistic Video Generation with Diffusion Models| 82|0.8292682926829269|
|runway                                               | 50|0.6599999999999999|


CUDA_VISIBLE_DEVICES=5 python run.py --model_config_path configs/models/saano_qwen2.config.yaml --task_config_path configs/tasks/video/video_mc_loki.yaml --batch_size 1
CUDA_VISIBLE_DEVICES=6 python run.py --model_config_path configs/models/saano_qwen2.config.yaml --task_config_path configs/tasks/video/video_tf_loki.yaml --batch_size 1
