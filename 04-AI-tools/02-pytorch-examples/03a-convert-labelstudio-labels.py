import argparse
import os

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

parser = argparse.ArgumentParser()
parser.add_argument('label_studio_export_path', help='Path to extracted label-studio YOLO export')
args = parser.parse_args()

EXPORT_PATH = args.label_studio_export_path
LABELS_PATH = os.path.join(EXPORT_PATH, 'labels')

with open(os.path.join(EXPORT_PATH, 'classes.txt'), 'r') as classes_file:
    classes = [line.strip() for line in classes_file.readlines()]

for cls in classes:
    assert cls in COCO_CLASSES, f'Did not find a match for class name {cls} in COCO classes. Aborting. No files have been changed.'

for labels_file in os.listdir(LABELS_PATH):
    with open(os.path.join(LABELS_PATH, labels_file), 'r') as lf:
        label_lines = [line.strip().split(' ') for line in lf.readlines()]
    for line in label_lines:
        class_name = classes[int(line[0])]
        coco_class_id = COCO_CLASSES[class_name]
        line[0] = str(coco_class_id)
    with open(os.path.join(LABELS_PATH, labels_file), 'w') as lf2:
        lf2.writelines([' '.join(line) + '\n' for line in label_lines])


        
        