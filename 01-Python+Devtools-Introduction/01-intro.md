---
marp: true
paginate: true
theme: default 
header: ![h:35](../imgs/starwit.png)
footer: 'Starwit Technologies GmbH | Predictive Analytics | Overview'
---
<!-- _class: lead -->
# Chapter 1 - Introduction to Python & Setup Development 
---
# Overview
* Setting up your development environment
  * Access Github/SSH
  * Checkout code
  * Install Python
* Write first program in Python
* Introduction to the Python programming language
* Interesting & useful Python features
* Docker

---
## Setup your dev environment
* Instructor works with Ubuntu Linux
* Tested with Python version 3.12
* To edit code Visual Studio Code is recommended https://code.visualstudio.com/ 
* Resources:
  * https://www.w3schools.com/python/default.asp

---
## Notes on Installation
### Ubuntu Path
On Linux installing Python is fairly easy, it is usually supported by your OS' package manager. This is how this works on Ubuntu:
```bash
  sudo apt update
  sudo apt upgrade
  sudo apt install python3
  #check installation
  python3 --version
  # install pip packet manager
  sudo apt install python3-pip
  # update pip - we will use that in virtual envs
  pip install --upgrade pip
```

### Windows Path
On Windows you have two choices, install Python on Windows, or use WSL2 to run Ubuntu Linux.
* Basic installation: https://www.digitalocean.com/community/tutorials/install-python-windows-10 
* Alternative: Anaconda - https://docs.anaconda.com/free/anaconda/install/windows/

---
## Review Git
* Course material is stored on Github
* URL: https://github.com/starwit-trainings/python-ai-cv
* Create account at Github / [Generate SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows) 
* Checkout/Clone repository
```bash
  git clone git@github.com:starwit-trainings/python-ai-cv.git
  git checkout -b yourname # create a new branch with your name
  git add yourchanges.py
  git commit -m"meaningful comment"
  git push -u origin yourname # just the first time, for a new branch
```
* Why git flow matters
* On .gitignore
---
# Introduction to the Python Programming Language
* Invented in the 1990ies
* Sort of platform independent
* Both interpreter & compiler
* Foreign Function Interface - or why Python is useful at all
* In a way Python is glue code, to call compute intense functions, not written in Python
* On Multithreading
* We use [CPython](https://en.wikipedia.org/wiki/CPython#:~:text=CPython%20is%20the%20reference%20implementation,CPython)
---
## Language Features
* [Language overview](https://en.wikipedia.org/wiki/Python_(programming_language))
* dynamically typed
* Garbage collected - sort of
* multiple paradigms
* procedural, object oriented, functional
* Shell vs running programs
* Large function library included
* Vast eco-systems of third party libs -> pip
* Indentations...
---
## Hello World
```bash
  python3 scripts/01-hello-world.py 
```
---
## Language Introduction
* [Conditionals](scripts/02-control-flow.py) & [Loops](scripts/04-loops.py)
* [Exceptions](scripts/03-exceptions.py)
* [Lists, Dictionaries](scripts/05-lists-dictionaries.py), [JSON](scripts/07-using-JSON.py)
* And Arrays?
* [Imports & Libraries](scripts/06-importing-from-libs.py)
* [Functions & Parameters](scripts/08-functions.py)
* [Objects & Classes](scripts/09-oop.py) - very brief (abstract classes, interfaces, (multi)inheritance)
---
### Introduction - Tasks 
* Look at every sample script
* For each of the following tasks, create a separate file
* Commit your solutions to your local branch
---
### Introduction - Tasks 
* Task 01 - Control structures & Exceptions
  * Write a script that asks for your age, height and weight
  * Make sure, that data is input correctly by checking types
  * Compute [body mass index](https://en.wikipedia.org/wiki/Body_mass_index) and ouput result
  * program shall comment (politely) on results
  * Extend your program to ask for user's name and greet user by name. Add also explanation on what program is supposed to do
  * Extend your program to run in a loop, to catch a multitude of user info
* Task 02 - Variables
  * Write a script, that for a given startdate and a number of matchdays (e.g. 34) calculates Friday, Saturday & Sunday for every matchday
  * Note: a match day is a set of Friday, Saturday, Sunday.
  * Output table with dates
  * Bonus challenge: make sure to exclude holidays like christmas
* Task 02a - Variables, Loops and decision
  * Imagine a number guessing program
  * Create a random number >0 and < 150
  * let a user guess a number and give feedback if number is smaller, larger or indeed the correct value of user input
  * Bonus Challenge: count attempts a user needs and output a high-score list - can we make this persistent?
---
### Introduction - Tasks
* Task 03 - Loops and lists
  * Write a script, that captures names of ten football clubs
  * All clubs shall then get assigned a unique id (integer) and a football leauge (e.g. 1)
  * Output a table of all clubs
  * Bonus challenge: output list to a file
* Task 03a - JSON
  * Enhance last script to output list as JSON
  * add last modified field to every entry
* Task 04 - Working with complex data structures
  * Take data structure from script [07](01-python-introduction/07-using-JSON.py)
  * Goal is a flat list stored to a file
  * Collect all (!) temperatures, WGS coordinates, Timestamp 
  * Timestamp shall be output in a human readable form
  * Output into a CSV file 
---
### Introduction - Tasks
* Task 05 - Git reminder
  * create a git repository at Github
  * check in solutions for tasks 1-3 in seperate folders each
  * create a Gihub issue that describes requirements for solution 3
    * targeted CSV file shall be taken from a CLI parameter
    * add a main function to script + [shebang](https://de.wikipedia.org/wiki/Shebang)
  * create a branch for that task and change solution 3 on this branch
  * create a pull request for your solution and choose another member from the lecture to review your solution
  * after review merge code to main branch.

---
### Introduction - Modelling a complex application

![width:600px](../imgs/OOD02.png)

---
* Task 06 - Data structures / OOD
  * Let's model the real world application example
  * Build a class for the following for domain objects
  * Imagine a football manager, that holds data about clubs, leagues, players and matches
    * Club: id, name, league_id
    * League: id, name, first_match, champion, record_player, games_record_player
    * Player: id, club_id, trikot_number, player_name, country, total_games, goals, assists
    * Games: id, matchday. match_date, match_time, home_club, guest_club, goals_home, goals_guest
  * As you can see, every object has an id - move that to an abstract class and let every other class inherit from it.
  * Create instances for all objects
---

## Advanced Features
* [Working with files](02-advanced-features/01-working-with-files.py)
* [HTTP requests](02-advanced-features/02-http-requests.py)
  * pip install requests
* [Simple GUI](02-advanced-features/03-simple-gui.py)
* [On main and parameters](02-advanced-features/04-on-main.py)

---
### Advanced Features - Tasks
* Task 07 Files
  * Extend solution from Task 01 and store output to a file
  * Think of a possibility to store data as a CSV file
* Task 08 - Files and folders
  * Write a script, that finds all files ending with *.py in a folder (as parameter)
  * Content of all files shall be concatenated into one output file 
  * Content of each found file shall be separated by a newline in output file
  * output file shall be located in [temporary folder](https://python.readthedocs.io/en/latest/library/tempfile.html) of your operating system
* Task 09 - HTTP requests
  * You can use environment variables in Python (see [example](02-advanced-features/02-http-requests.py))
  * On bash define it like so
  ```bash
  export TRAFIKVERKET_API_KEY=
  ```
  * Get an API token from [Trafikverket](https://data.trafikverket.se/oauth2/Account/register)
  * Get live weather data from [API](https://data.trafikverket.se/documentation/datacache/testbench)
  * Extract data with above solution and write data into file

---
# Introduction to Docker
* How does it work and what is good for?
* Tasks
  * Installation Linux/Windows
  * Run container
  * Build your own images
* About Credentials
* Inspecting Images: [dive](https://github.com/wagoodman/dive)
* Docker Compose
---
* Task 10 - Docker
  * Build Docker image from [example](03-docker/dockerfile)
  ```bash
  sudo docker build . -t pythonbasic/helloworld
  ```
  ![docker image](../imgs/docker-image.jpg)
  * Run image
  ```bash
  sudo docker run --rm -it pythonbasic/helloworld
  ```
  ![running docker](../imgs/running-docker.jpg)
  * Stop image - why is it taking so long?

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
