---
marp: true
paginate: true
theme: default 
header: ![h:35](../imgs/starwit.png)
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
# Chapter 2 - Tools & Libraries
---
## Overview
In this chapter various helpful tools and libraries are introduced, that are essential, to make developing with Python easier.
* Pip with requirements
* Poetry https://python-poetry.org/
* Jupyter
  * how to run
  * how to version
  * how to use
* numpy/SciPy
* https://scipy.org/
* various math examples
  * compute standard distribution & values
  * matrix operations / slicing
---
## What is dependency management
* Collecting all libraries automatically
* Keep control on lib versions
* Enable automatic builds -> sine qua non releasing!
* Also for individual projects
* Makes your code usable for others
* Version control, documentation & dependency management - never without any of those!
* Python packages are listed here: https://pypi.org/
---

## Using pip for dependency management
* pip standard dependency management tool
* downloads and unpacks libraries
* Example requests: https://pypi.org/project/requests/
* Libs can be installed globally, per user or in virtual environments
* Recursive - dependencies of dependencies
* But: multiple versions of same library are not possible

---
### Pip requirements example
* Pip can download all packages listed in __requirements.txt__
* Fix version number/range for libs
  * numpy==1.26.4 vs requests>=2.31.0 
* Multiple calls result in same target state
* Run example
```bash
  cd depmanagement-pip
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt 
```
![](../imgs/venv04.jpg)

---
## Using poetry for dependency management
---
### Poetry example
* Run example
```bash
  cd depmanagement-pip
  TODO
```
---

## Jupyter
* Typical data exploration workflow:
  * load data
  * show sample data
  * write analysis code
  * show results
  * extend code
* Jupyter is a tool, that supports this workflow
* We use classic notebooks (intensively) for this course
* VSCode extension: Jupyter
* Note: Notebooks can and should be under version control
---
### Setting up Jupyter
Jupyter can be run as a browsable service like so:
```bash
  cd jupyter-example
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt 
  jupyter notebook
```

Last command will open a browser tab and you can start working with notebooks.

VSCode can run notebooks and that is the preferred usage for this course. Use the power of an IDE :)

---
### Running example

Running a notebook in VScode

![](../imgs/jupyter01.jpg)

---
### Virtual envs, VSCode & Jupyter
VSCode supports running Jupyter notebooks code in virtual environments:
![](../imgs/Jupyter+venvs.jpg)
* Keep in mind to manage your notebooks and virtual envs

---
# Selected Libraries

The following section introduces selected Python libraries, that are useful for data analytics and AI projects. It is by no means complete and will be extended.

---
## Numpy
* https://numpy.org/doc/1.26/user/absolute_beginners.html

---
## SciPy
* https://scipy.org/

---
## SimPy