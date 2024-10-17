---
marp: true
paginate: true
theme: default 
header: ![h:35](../../imgs/starwit.png)
footer: 'Starwit Technologies GmbH | IT Foundations | Overview'
---
<!-- _class: lead -->
# Chpater 2.1 - Libraries to develop software with Python
---
## Overview
In this chapter we will look into a number of libraries, that helps you developing software system with Python.

* Reading CSV data
* REST services - Flask
* Databases - PostgreSQL
* On Authentication
* On Logging
* Protobuf/gRPC Example
* Network Tools
* Messaging
* openAPI
---

### 01 - Working with CSV files

```bash
    cd 01-CSV-files
    python csv-files.py
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