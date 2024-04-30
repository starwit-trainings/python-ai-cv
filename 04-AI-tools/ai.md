---
marp: true
paginate: hide
theme: default 
header: ![h:35](imgs/starwit.png)
footer: 'Starwit Technologies GmbH | IT Foundations | Overview'
---

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

<!-- _class: lead -->
# Chapter 4 - AI tool chain: training & running models
---
# Overview
* CV example 
  * Yolov8 detection, segmentation, poses
  * train/execute custom model
* PyTorch
  * Introduction
  * NIST OCR example
  * build custom net
* Netron to visualize networks
* Model file architectures (ONNX, PyTorch)
* Introduction SAE
  * run on every computer
  * video source
* Examples 
  * Video sample from Carmel
  * Live footage Aalen?
---