# 1. Export labels from labelstudio using the "YOLO" export format
# 1a. Run 03a-convert-labelstudio-labels.py to convert label-studio class ids to COCO class ids
# 2. Separate the image and label files into train and validation sets
# 2a. Create train.txt/val.txt that contain a list of images, paths are relative from file position
# 3. Create a dataset.yaml with a similar format as https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml
'''e.g.:

path: ./custom
train: train.txt
val: val.txt

names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
'''
# 4. Run this script and check the error message for the path where ultralytics expects the dataset directory to be located
#    (The logic behind this seems rather complex and system-dependent, so this is the most reliable option)

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model

# Train the model
results = model.train(data="dataset.yaml", epochs=100, imgsz=640)