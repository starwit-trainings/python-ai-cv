# 0. Make sure that you have ffmpeg installed on your machine
# 1. Export project from labelstudio
# 1a. Export labels from labelstudio using the "JSON" export format
# 1b. Save the project video
# 2. Run 03a-convert-labelstudio-export-to-yolo-dataset.py to convert the label studio export (and pass the files from 1a and 1b, see script parameters)
# 3. Create a dataset.yaml with a similar format as https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml
'''e.g.:

path: ./custom
train: train
val: val

# COCO classes
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