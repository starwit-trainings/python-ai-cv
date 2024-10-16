---
marp: true
paginate: true
theme: default 
header: ![h:35](../../imgs/starwit.png)
footer: 'Starwit Technologies GmbH | IT Foundations | Overview'
---
<!-- _class: lead -->

# Dependecy Management with Python

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
* But: multiple versions of same library are not possible -> virt envs
* For this course we will use pip

---
### Pip requirements example
* Pip can download all packages listed in __requirements.txt__
* Fix version number/range for libs
  * numpy==1.26.4 vs requests>=2.31.0 
* Multiple calls result in same target state
* Run example
```bash
  cd 01-depmanagement-pip
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt 
```
![](../imgs/venv04.jpg)

__Make sure you understand this idea - we will use from now on!__

---
## Using poetry for dependency management
* same library repository as pip
* support to build _and_ publish
* [TOML](https://en.wikipedia.org/wiki/TOML) file for config
* Much more powerfull than pip
---
### Poetry example
* Install Poetry
  ```bash
  apt install python3-poetry
  ```
* Run example
  ```bash
    cd 02-depmanagement-poetry
    TODO
  ```


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