# JavaScript Web Scraping Project

This repository contains scripts written in JavaScript for various tasks related to web scraping. The scripts are designed to accomplish different objectives such as reading and writing files, making HTTP requests, and interacting with APIs.

## Table of Contents

1. [Requirements](#requirements)
2. [Tasks](#tasks)
3. [Usage](#usage)
4. [Resources](#resources)
5. [License](#license)

## Requirements <a name="requirements"></a>

- Allowed editors: vi, vim, emacs
- All files should be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Code should be semistandard compliant (Rules of Standard + semicolons on top), following AirBnB style
- All files must be executable
- You are not allowed to use `var`
- Install Node 14: 
  ```
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```
- Install semistandard: 
  ```
  $ sudo npm install semistandard --global
  ```
- Install request module: 
  ```
  $ sudo npm install request --global
  $ export NODE_PATH=/usr/lib/node_modules
  ```

## Tasks <a name="tasks"></a>

### 0. Readme
- Description: Write a script that reads and prints the content of a file.
- Script: `0-readme.js`
- Usage: `./0-readme.js <file_path>`

### 1. Write me
- Description: Write a script that writes a string to a file.
- Script: `1-writeme.js`
- Usage: `./1-writeme.js <file_path> <string_to_write>`

### 2. Status code
- Description: Write a script that displays the status code of a GET request.
- Script: `2-statuscode.js`
- Usage: `./2-statuscode.js <URL>`

### 3. Star wars movie title
- Description: Write a script that prints the title of a Star Wars movie based on the episode number.
- Script: `3-starwars_title.js`
- Usage: `./3-starwars_title.js <movie_ID>`

### 4. Star wars Wedge Antilles
- Description: Write a script that prints the number of movies where the character "Wedge Antilles" is present.
- Script: `4-starwars_count.js`
- Usage: `./4-starwars_count.js <API_URL>`

### 5. Loripsum
- Description: Write a script that gets the contents of a webpage and stores it in a file.
- Script: `5-request_store.js`
- Usage: `./5-request_store.js <URL> <file_path>`

### 6. How many completed?
- Description: Write a script that computes the number of tasks completed by user id.
- Script: `6-completed_tasks.js`
- Usage: `./6-completed_tasks.js <API_URL>`

## Usage <a name="usage"></a>

To run any of the scripts, use the following format in the terminal:
```
./<script_name> <arguments>
```

## Resources <a name="resources"></a>

- Working with JSON data
- The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco
- `request` module
- Modern JS

## License <a name="license"></a>

Copyright © 2024 ALX, All rights reserved.
