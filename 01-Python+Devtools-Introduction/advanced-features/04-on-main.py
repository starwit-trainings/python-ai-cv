#!/usr/bin/env python

# Example for:
# make script executable
# "implement" main
# parse parameters

import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('videosource', help='any video source opencv understands, e.g. 0,1,... for usb cams, "rtsp://..." for RTSP streams, /path/video.mp4 for video file')
    arg_parser.add_argument('-m', '--model-size', choices=['n', 's', 'm', 'l', 'x'], default='n', help='the size of the model to use (nano, small, medium, large, xlarge); defaults to "nano"')
    arg_parser.add_argument('-t', '--task', choices=['detect', 'segment', 'classify', 'pose'], default='detect', help='the task to perform; defaults to "detect"')
    arg_parser.add_argument('-p', '--preview', action='store_true', help='whether to show a live preview window, reduces performance slightly. If the window is in focus, press "q" to exit.')
    arg_parser.add_argument('-l', '--log-classes', type=lambda s: s.split(','), dest='class_list', help='for every frame, log detected objects of these comma-delimited classes (class name must match a class in "yolov8_classes.json") into a sidecar .csv file')
    args = arg_parser.parse_args()

    for key,value in args._get_kwargs():
        print(key, ":", value)

# Task
# run script and try all parameters