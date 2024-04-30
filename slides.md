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
# Analytics with Python

---
## Tools & Preparations

Here is an overview of tools and requirements you should install on your computer. So take your time preparing your work environment.

* Windows / Ubuntu installation
* Conda vs Pip
* Git
* Editor: Visual Studio Code

---
# Chapters

Each of the next sections can be worked with individually, so no particular order is required. You will, however, notice that certain topics, like modeling classes and map them to SQL structure, are recurring aspects.

---
## 01 - Development Environment & Language Introduction 
* Git Flow Example
* Python language overview
  * basic syntax
  * Hello World
  * functions, modules, packages
  * Lambda functions
  * Context manager as concept
  * Runtime / Binary bindings (CPython, PyPi, Jython)
* Pip / Virtual environments
* Poetry
* Basic Language Concepts
  * convert/parse JSON
  * read/write files
  * network IO
* Docker
  * Installation & Usage
  * Compose
---
## 02 - Important libraries & tools for Python
* Jupyter
  * how to run
  * how to version
  * how to use
* numpy/pandas
* https://www.sympy.org/en/index.html
* various math examples
  * compute standard distribution & values
  * matrix operations / slicing

---
## 03 - Eating & Analyzing Data
* work with CSV/JSON fiels
* visualize Plotly/Matplotlib/Seaborn
* openCV
  * Introduction
  * sample API functions
  * sample Images 
* Example: Trajectories Carmel

---
## 04 - AI tool chain: training & running models 
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
## 05 - Running a computer vision pipeline 
* SAE architecture
  * ProtoBuf
  * Detection
  * Tracking
  * Mapping
* Custom modules
* Advanced Topics
  * concurrency or the lack thereof
---
# License

Code in this repository is property of [Starwit Technologies GmbH](https://starwit-technologies.de/) and is published under AGPL. So if you want to adapt it, any change needs to be published under AGPL as well. Please let us know, which changes you made. Same goes for errors and bugs.

License text can be cound [here](License)