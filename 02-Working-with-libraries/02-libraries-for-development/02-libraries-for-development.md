---
marp: true
paginate: true
theme: default 
header: ![h:35](../../imgs/starwit.png)
footer: 'Starwit Technologies GmbH | Python | Overview'
---
<!-- _class: lead -->
# Chpater 2.1 - Libraries to develop software with Python
---
## Overview
In this chapter we will look into a number of libraries, that helps you developing software system with Python.

* Reading CSV data
* REST services - Flask
* Databases - PostgreSQL
* Protobuf/gRPC Example
* On Authentication
* On Logging
* Network Tools
* Messaging
* openAPI
---
## Virtual environments
Most examples need libraries to run.For all examples, in which you find a requirements.txt file, you have to set up a virtual environment. 
```bash
  cd folder/with/requirements.tx
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install -r requirements.txt
```

---
## 01 - Working with CSV files

Files with comma seperated values are still very useful and thus, this example shows you, how to use them with Python.

How to run example:
```bash
    cd 01-CSV-files
    python3 csv-files.py
```

### Tasks
* Run program and observice output
* Look at extract column names function - is this a good idea?
* Use DictReader reader to create output with column name in front of every field
* Read data from all other CSV files, check if files exist - display error message, if not. Keep content in global variables
* Write a new method that adds an entry to every CSV file - check if file exists first, create a new file if not
* Write a function, that tries to find all CSV files recursively in a folder.
* Bonus challenge: after reading all CSV files, write a function, that finds for a given club ID respective league data
---

## 02 - Rest services
A wide spread interface technology for application is called [REST](https://en.wikipedia.org/wiki/REST) and it is based on HTTP. This example shows you, how to use FastAPI to implement REST services with Python.

How to run example:
```bash
    cd 02-REST-services/restexample
    python main.py
```

### Tasks
* Run program
* Implement a service for all four models for the football manager
* Load data from CSV files from last example
* Implement a service "/fooball/clubs/leauge/{id}" that delivers all clubs playing in provided leauge

---

## 03 - Talking to Databases
In order to talk to PostgreSQL some binaries needs to be installed in Linux. Following example shows how to install on Ubuntu:
```bash
    apt install libpq
```
How to run example, first start demo database with docker compose
```bash
    cd 03-PostgreSQL
    docker compose up
```
```bash
    cd 03-PostgreSQL
    python postgres.py
```

### Tasks
* Run program
* Import data from CSV files and add them to database
* Write a function that queries for all clubs playing in a league

---
## 04 - Connecting REST services with a database
This example is supposed to combine the last two - writing an app, that runs a database and provide its content via a REST interface. Start database like in the last example.
```bash
  cd 04-Postgres-REST-app
  python main.py
```

### Tasks
* Run program
* Implement REST function for all four football objects
* Implement REST services for
  * clubs per leauge
  * players per club
---
## 05 - Talking binary gRPC & Protobuf

```bash
  #Generate code
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. football-manager.proto
```
```bash
  #Run server
  python football_server.py
```
```bash
  # Run client
  python football_client.py
```
### Tasks
* Run server & client
* Modify Protobuf file and add messages for all four football objects
* Implement services for list/find by id for all objects
* Look at streaming example - modify protobuf/python such that home/guest club and goals are transfered
* build a second live stream, that responds with a list of results
* Bonus challenge: connect database from db example as a backend

---

## 06 REST and authorization

```bash
  # run Keycloak
  docker compose up
```
```bash
  # start REST app
  python main.py
```
```bash
  # request token
  curl -d client_id=microservices \
    -d username=microservices-admin \ 
    -d password=microservices-admin \
    -d grant_type=password http://yourip:8090/realms/microservices/protocol/openid-connect/token
```
```bash
  # request token
  curl -i -H "Authorization: Bearer TOKEN" localhost:8000/football/clubs
```
---
## 07 Documenting Python code
Generating code documentation is an obviously important tool. PDoc does this for Python.
```bash
  # start doc server
  pdoc restexample/main.py
```
```bash
  # start doc server
  pdoc -o ./html restexample/main.py
```

### Tasks
* Add classes from OOP example to this project and generate docs

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