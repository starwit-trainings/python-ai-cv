---
marp: true
paginate: hide
theme: default 
header: ![h:35](imgs/starwit.png)
footer: 'Starwit Technologies GmbH | Predictive Analytics | Overview'
---

<!-- _class: lead -->
# Introduction to the Python programming language
---
# Chapters

Each of the next sections can be worked with individually, so no particular order is required. However it is recommandable to follow the intended order.

---
## Chapter 01 - Setup & Language introduction
* Setting up your development environment
  * Access Github/SSH
  * Checkout code
  * Install Python
* Write first program in Python
* Quick review of Python's most important features
* Virtual environments and dependency management
* Advanced features
[Jump to first chapter](01-Python+Devtools-Introduction/01-intro.md)
---
## Chapter 02 - Using libraries with Python
* Dependency Management
* Jupyter
* Libs to build software
* Libs to analyze data
[Jump to second chapter](02-Working-with-libraries/02-libraries.md)

---
## Chapter 03 - Eating & Analyzing Data
* work with CSV/JSON fiels
* visualize Plotly/Matplotlib/Seaborn
* openCV
  * Introduction
  * sample API functions
  * sample Images 
* Example: Trajectories Carmel
[Jump to third chapter](03-eating+analyzing-data/data.md)

---
## Chapter 04 - AI tool chain: training & running models 
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
[Jump to fourth chapter](04-AI-tools/ai.md)
---
## Chapter 05 - Running a computer vision pipeline 
* SAE architecture
  * ProtoBuf
  * Detection
  * Tracking
  * Mapping
* Custom modules
[Jump to fifth chapter](05-Computer-Vision-Pipeline/cv-pipeline.md)
---
## Chapter 06 - Cloud Technologies
* Kubernetes
* AWS Examples
[Jump to sixth chapter](06-Cloud/06-cloud.md)
---
# License

Code in this repository is property of [Starwit Technologies GmbH](https://starwit-technologies.de/) and is published under AGPL. So if you want to adapt it, any change needs to be published under AGPL as well. Please let us know, which changes you made. Same goes for errors and bugs.

License text can be cound [here](License)

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