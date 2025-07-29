import os
import cv2
import argparse
import numpy as np
from tqdm import tqdm

# ==== 变换函数 ====

def add_noise(frame, sigma):
    noise = np.random.normal(0, sigma, frame.shape).astype(np.int16)
    noisy = np.clip(frame.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return noisy

def apply_blur(frame, ksize, sigmaX):
    return cv2.GaussianBlur(frame, ksize, sigmaX=sigmaX)

def resize_distort(frame, scale):
    h, w = frame.shape[:2]
    small = cv2.resize(frame, (int(w * scale), int(h * scale)))
    return cv2.resize(small, (w, h))

def compress_video_ffmpeg(temp_input, output_path, bitrate):
    os.system(f'ffmpeg -y -i "{temp_input}" -b:v {bitrate} -loglevel error "{output_path}"')
    os.remove(temp_input)

# ==== 单视频处理函数 ====

def process_video(input_path, output_path, transform_type, args):
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    filename = os.path.basename(input_path)
    temp_path = os.path.join(output_path, filename)

    if transform_type != 'compressed':
        writer = cv2.VideoWriter(temp_path, fourcc, fps, (w, h))

    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if transform_type == 'noise':
            out_frame = add_noise(frame, sigma=args.sigma)
            writer.write(out_frame)

        elif transform_type == 'blur':
            out_frame = apply_blur(frame, ksize=(args.ksize, args.ksize), sigmaX=args.sigmaX)
            writer.write(out_frame)

        elif transform_type == 'resize':
            out_frame = resize_distort(frame, scale=args.scale)
            writer.write(out_frame)

        elif transform_type == 'compressed':
            frames.append(frame)

    cap.release()
    if transform_type != 'compressed':
        writer.release()

    if transform_type == 'compressed':
        temp_raw = os.path.join(output_path, 'temp_input.mp4')
        raw_writer = cv2.VideoWriter(temp_raw, fourcc, fps, (w, h))
        for f in frames:
            raw_writer.write(f)
        raw_writer.release()
        compress_video_ffmpeg(temp_raw, temp_path, bitrate=args.bitrate)

# ==== 批处理入口 ====

def process_all_videos(input_dir, output_dir, transform_type, args):
    os.makedirs(output_dir, exist_ok=True)
    for file in tqdm(os.listdir(input_dir)):
        if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            input_path = os.path.join(input_dir, file)
            process_video(input_path, output_dir, transform_type, args)

# ==== 命令行参数 ====

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch video transformation tool")

    parser.add_argument("--input_dir", type=str, required=True, help="Input directory of videos")
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory for processed videos")
    parser.add_argument("--transform", type=str, required=True, choices=["noise", "blur", "resize", "compressed"], help="Transformation type")

    # noise
    parser.add_argument("--sigma", type=float, default=15.0, help="Noise standard deviation (for 'noise')")

    # blur
    parser.add_argument("--ksize", type=int, default=5, help="Kernel size for Gaussian blur (must be odd)")
    parser.add_argument("--sigmaX", type=float, default=1.5, help="SigmaX for Gaussian blur")

    # resize
    parser.add_argument("--scale", type=float, default=0.25, help="Resize scale (e.g. 0.25 for 25%)")

    # compressed
    parser.add_argument("--bitrate", type=str, default="500k", help="Target bitrate for compression")

    args = parser.parse_args()

    # validate blur kernel size
    if args.transform == 'blur' and args.ksize % 2 == 0:
        raise ValueError("ksize must be an odd number for Gaussian blur.")

    process_all_videos(args.input_dir, args.output_dir, args.transform, args)
