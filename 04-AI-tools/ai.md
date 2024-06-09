---
marp: true
paginate: hide
theme: default 
header: ![h:35](imgs/starwit.png)
footer: 'Starwit Technologies GmbH | Predictive Analytics | Overview'
---

<!-- _class: lead -->
# Chapter 4 - AI tool chain: training & running models
---
# Overview
This section provides fundamentals on how to label training data, how to run trainings and how to apply trained models. 
* CV example 
  * Intro to [openCV](01-introduction-example/01-opencv.py)
  * setup [RTSP server](01-introduction-example/01-rtsp-server/setup.md)
  * [Yolov8](02-pytorch-examples/01-intro.py) detection, segmentation, poses
* PyTorch
  * Introduction
  * NIST OCR example
  * build custom net
* Train custom model
* Netron to visualize networks
* Model file architectures (ONNX, PyTorch)

---
## Introduction openCV
* extensive library to work images/videos
* written in C/C++
* bindings in many other languages
* easy to use with Python
* features
  * read image/video formats
  * transform images, filtering
  * image stitching
  * various AI functions: face recognition, object detection, ...
* good hardware support - accelerated functions
* if it is image/video processing _always_ look here first: https://docs.opencv.org/4.9.0/
---
## Introduction Yolo
* You look only once
* Fast, precise & well supported
* General idea
  * Divide image in NxN cells
  * Classify for each cell and class, if object probability is >0
  * Intersection Over Unions with probability per cell -> bounding boxes
  * Non-Max Suppression to reduce bounding boxes
* Plenty of docs available [example](https://www.datacamp.com/blog/yolo-object-detection-explained)
* remember this is not an AI lecture :)
* Various implementations - we will use Yolov8 by [Ultralytics](https://docs.ultralytics.com/)
* Please note license agreement - AGPL!
---
## An application example Yolo & openCV
* [OpenCV](01-introduction-example/01-opencv.py)
* [Yolo](01-introduction-example/01-yolo-example.py)
---
## Introduction PyTorch
* Framework written in C++/Python
* Governed by Linux Foundation
* Tensor operations / Deep neural networks
* Tensors here are multi-dimensional arrays
* can push computation to GPUs (CUDA -> Nvidia, ROCm -> AMD)
* basis for many frameworks and algorithm implementations
---
### PyTorch examples & tasks
* NIST
* ...
---
## Introduction Label Studio
* Instance for this course: https://label.aitools.starwit-infra.de/ 
* If you want to install your own instance: https://labelstud.io/
* You get an invite link, to create a login
* We will lable videos
---
### Labeling Objectives


<style>
header {
  text-align: right;
  font-size: 0.7rem;
  color: #bbb;
  margin: 20px;
  left: 0px;
  right: 0px;
  padding-top: 5px;
}
footer {
  font-size: 0.7rem;
  color: #bbb;
}
section.lead {
  text-align: center;
  margin-bottom: 40px;
}
section {
  font-size: 1.2rem;
}
section.lead h1 {
  font-size: 2.5rem;
  font-weight: 600;
}
section.linked footer {
  display: none;
}
section.linked header {
  display: none;
}
section.quote {
  font-size: 1.0rem;
  text-align: center;
  font-style: italic;
  color: #555;
}

h1 {
  font-size: 2.5rem;
  font-weight: 500;
  color: #2B5A6A;
}
h2 {
  font-size: 1.8rem;
  font-weight: 400;
  color: #333;
  margin-top: 30px;
  margin-bottom: 15px;
  text-transform: uppercase;
}
a {
  color: #3A9FC1;
}
a:hover {
  color: #1E708B; 
  text-decoration: underline; 
}
ul {
  text-align: left
}

</style>