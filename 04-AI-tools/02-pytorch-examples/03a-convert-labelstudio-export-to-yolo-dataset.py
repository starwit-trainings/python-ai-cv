import argparse
import json
import os
from pathlib import Path
from ffmpeg import FFmpeg

COCO_CLASSES = {
    'person': 0,
    'bicycle': 1,
    'car': 2,
    'motorcycle': 3,
    'airplane': 4,
    'bus': 5,
    'train': 6,
    'truck': 7,
    'boat': 8,
    'traffic light': 9,
    'fire hydrant': 10,
    'stop sign': 11,
    'parking meter': 12,
    'bench': 13,
    'bird': 14,
    'cat': 15,
    'dog': 16,
    'horse': 17,
    'sheep': 18,
    'cow': 19,
    'elephant': 20,
    'bear': 21,
    'zebra': 22,
    'giraffe': 23,
    'backpack': 24,
    'umbrella': 25,
    'handbag': 26,
    'tie': 27,
    'suitcase': 28,
    'frisbee': 29,
    'skis': 30,
    'snowboard': 31,
    'sports ball': 32,
    'kite': 33,
    'baseball bat': 34,
    'baseball glove': 35,
    'skateboard': 36,
    'surfboard': 37,
    'tennis racket': 38,
    'bottle': 39,
    'wine glass': 40,
    'cup': 41,
    'fork': 42,
    'knife': 43,
    'spoon': 44,
    'bowl': 45,
    'banana': 46,
    'apple': 47,
    'sandwich': 48,
    'orange': 49,
    'broccoli': 50,
    'carrot': 51,
    'hot dog': 52,
    'pizza': 53,
    'donut': 54,
    'cake': 55,
    'chair': 56,
    'couch': 57,
    'potted plant': 58,
    'bed': 59,
    'dining table': 60,
    'toilet': 61,
    'tv': 62,
    'laptop': 63,
    'mouse': 64,
    'remote': 65,
    'keyboard': 66,
    'cell phone': 67,
    'microwave': 68,
    'oven': 69,
    'toaster': 70,
    'sink': 71,
    'refrigerator': 72,
    'book': 73,
    'clock': 74,
    'vase': 75,
    'scissors': 76,
    'teddy bear': 77,
    'hair drier': 78,
    'toothbrush': 79,
}

def extract_video_frames(video_path: Path, output_path: Path):
    os.makedirs(output_path, exist_ok=True)
    (FFmpeg()
        .input(video_path)
        .output(
            f'{output_path}/frame_%06d.jpg',
            {'q:v': '2'}
        )
        .execute())
    

def labelstudio_labels_to_yolo(labelstudio_labels_json_path: str, output_dir_path: str, index_video: int = 0) -> None:
    ls_project = json.load(open(labelstudio_labels_json_path))[index_video]

    # every box stores the frame count of the whole video, so we get it from the first box
    frames_count = ls_project['annotations'][0]['result'][0]['value']['framesCount']
    yolo_labels = [[] for _ in range(frames_count)]
    for instance in ls_project['annotations'][0]['result']:
        class_id = COCO_CLASSES.get(instance['value']['labels'][0], -1)
        # iterate through keypoints (we omit the last keypoint because no interpolation after that)
        for i, keypoint in enumerate(instance['value']['sequence'][:-1]):
            start_point = keypoint
            end_point = instance['value']['sequence'][i + 1]
            start_frame = start_point['frame']
            end_frame = end_point['frame']

            n_frames_between = end_frame - start_frame
            delta_x = (end_point['x'] - start_point['x']) / n_frames_between
            delta_y = (end_point['y'] - start_point['y']) / n_frames_between
            delta_width = (end_point['width'] - start_point['width']) / n_frames_between
            delta_height = (end_point['height'] - start_point['height']) / n_frames_between

            # In YOLO, x and y are in the center of the box. In Label Studio, x and y are in the corner of the box.
            x = start_point['x'] + start_point['width'] / 2
            y = start_point['y'] + start_point['height'] / 2
            width = start_point['width']
            height = start_point['height']
            # iterate through frames between two keypoints
            for frame in range(start_frame, end_frame):
                yolo_labels[frame].append([class_id, x / 100, y / 100, width / 100, height / 100])
                x += delta_x + delta_width / 2
                y += delta_y + delta_height / 2
                width += delta_width
                height += delta_height
            # Make sure that the loop works as intended
            epsilon = 1e-5
            assert (x - end_point['x'] - end_point['width'] / 2) <= epsilon, f'x does not match: {x} vs {end_point["x"] + end_point["width"] / 2}'
            assert (y - end_point['y'] - end_point['height'] / 2) <= epsilon, f'y does not match: {y} vs {end_point["y"] + end_point["height"] / 2}'
            assert (width - end_point[
                'width']) <= epsilon, f'width does not match: {width} vs {end_point["width"]}'
            assert (height - end_point[
                'height']) <= epsilon, f'height does not match: {height} vs {end_point["height"]}'

        # Handle last keypoint
        last_keypoint = instance['value']['sequence'][-1]
        yolo_labels[last_keypoint['frame']].append([class_id, last_keypoint['x'] / 100, last_keypoint['y'] / 100, last_keypoint['width'] / 100, last_keypoint['height'] / 100])

    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
        print(f'Directory did not exist. Created {output_dir_path}')
    for frame, frame_labels in enumerate(yolo_labels):
        if frame % 1000 == 0:
            print(f'Writing labels for frame {frame}')
        padded_frame_number = str(frame).zfill(6)
        file_path = Path(output_dir_path) / f'frame_{padded_frame_number}.txt'
        text = ''
        for label in frame_labels:
            text += ' '.join(map(str, label)) + '\n'
        with open(file_path, 'w') as f:
            f.write(text)
    os.remove(Path(output_dir_path) / f'frame_000000.txt')
    print(f'Done. Wrote labels for {frame + 1} frames.')

def split_train_val(output_path: Path, ratio: float = 0.8):
    os.makedirs(output_path / 'train' / 'images')
    os.makedirs(output_path / 'train' / 'labels')
    os.makedirs(output_path / 'val' / 'images')
    os.makedirs(output_path / 'val' / 'labels')
    img_files = sorted([f for f in os.listdir(output_path / 'frames') if f.endswith('.jpg')])
    lbl_files = sorted([f for f in os.listdir(output_path / 'frames') if f.endswith('.txt')])
    count_train = round(len(img_files) * ratio)
    for file in img_files[:count_train]:
        os.rename(output_path / 'frames' / file, output_path / 'train' / 'images' / file)
    for file in img_files[count_train:]:
        os.rename(output_path / 'frames' / file, output_path / 'val' / 'images' / file)
    for file in lbl_files[:count_train]:
        os.rename(output_path / 'frames' / file, output_path / 'train' / 'labels' / file)
    for file in lbl_files[count_train:]:
        os.rename(output_path / 'frames' / file, output_path / 'val' / 'labels' / file)
    os.rmdir(output_path / 'frames')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--label-studio-json-export', help='Path to label-studio project export in JSON format', required=True)
    parser.add_argument('-v', '--video-file', help='Path to video file associated with project export', required=True)
    parser.add_argument('-o', '--output-folder', help='Path to output folder', required=True)
    args = parser.parse_args()

    EXPORT_PATH = Path(args.label_studio_json_export)
    VIDEO_PATH = Path(args.video_file)
    OUTPUT_PATH = Path(args.output_folder)

    extract_video_frames(VIDEO_PATH, OUTPUT_PATH / 'frames')
    labelstudio_labels_to_yolo(EXPORT_PATH, OUTPUT_PATH / 'frames')
    split_train_val(OUTPUT_PATH)
