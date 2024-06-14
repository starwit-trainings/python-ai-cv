#!/usr/bin/env python

# Example for:
# 

import argparse
import logging
import os
import signal

import cv2
from ultralytics import YOLO

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

running = True

task_suffixes = {
    'detect': '',
    'segment': '-seg',
    'classify': '-cls',
    'pose': '-pose',
}

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

def model_name(size, task):
    suffix = task_suffixes[task]
    return f'yolov8{size}{suffix}.pt'

def do_inferencing(source, model_size, task, preview, class_list):
    global running
    # use USB camera
    if source.isdigit():
        source = int(source)
    # get video source
    cap         = cv2.VideoCapture(source)
    # get details from video source
    width       = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height      = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps         = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    logger.info("start inferencing")

    # instanciate yolo model
    model = YOLO(model_name(model_size, task))

    # live preview window?
    if preview:
        cv2.namedWindow("output", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("output", 800, 600)

    while cap.isOpened() and running:
        ret, frame = cap.read()
        if ret == True:
            prediction = model.predict(frame, verbose=False, tracker='bytetrack.yaml')
            res_plotted = prediction[0].plot()
            
            if preview:
                cv2.imshow('output', res_plotted)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break 
        else:
            logger.error("couldn't read next frame")
            break  

    # be nice to your operating system
    cap.release()
    cv2.destroyAllWindows()
    logger.info("Stopped inferencing")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('videosource', help='any video source opencv understands, e.g. 0,1,... for usb cams, "rtsp://..." for RTSP streams, /path/video.mp4 for video file')
    arg_parser.add_argument('-m', '--model-size', choices=['n', 's', 'm', 'l', 'x'], default='n', help='the size of the model to use (nano, small, medium, large, xlarge); defaults to "nano"')
    arg_parser.add_argument('-t', '--task', choices=['detect', 'segment', 'classify', 'pose'], default='detect', help='the task to perform; defaults to "detect"')
    arg_parser.add_argument('-p', '--preview', default=True, action='store_true', help='whether to show a live preview window, reduces performance slightly. If the window is in focus, press "q" to exit.')
    args = arg_parser.parse_args()

    # shutdown script properly
    def signal_handler(signum, _):
        signame = signal.Signals(signum).name
        logger.warning(f'Received {signame}. Exiting...')
        global running
        running = False

    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)    

    do_inferencing(args.videosource, args.model_size, args.task, args.preview, COCO_CLASSES)


# Tasks
# 1. create video output with inferenced data
# 2. create inferencing statistics with time breakdown preprocess, inference, postprocess