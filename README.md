# Flask Demo

## Installation
### Get the code
In the terminal, use `git clone` to get a copy of the code.
```shell
git clone https://github.com/Morgan-Elkins/FlaskPythonProject.git
```

Then, set up your environment using  PyCharm.



### PyCharm

After cloning the code:

- Open PyCharm
- Select `File` > `Open...`
- Navigate to the cloned project folder and click `Open`
- PyCharm should automatically detect that the project has dependencies.
  - Keep the default values and click "OK"

## Running the API

To start the server, in the Terminal:

```shell
flask run
```
--------------
## Testing Each REST request
Using Postman, each of the request can be tested.
### Actors
#### Get all actors, using GET
```commandline
localhost:5000/api/actors/
```
#### Get specific actor by id (e.g. actor_id: 1), using GET
```commandline
localhost:5000/api/actors/1
```
#### Create a new actor by entering all info, using POST
```commandline
localhost:5000/api/actors/
```
```JSON
{"first_name": "FIRSTNAMETEST",
"last_name": "LASTNAMETEST"}
```
#### Update the information of an actor by adding some or all information and ID, using PATCH
```commandline
localhost:5000/api/actors/101
```
```json
{"first_name": "UPDATEDNAMETEST"}
```
#### Delete an actor by ID, using DELETE
```commandline
localhost:5000/api/actors/101
```
--------------------
### Films
#### Get all films, using GET
```commandline
localhost:5000/api/films/
```
#### Get specific film by id , using GET
```commandline
localhost:5000/api/films/1
```
#### Create a new film by entering all info, using POST
```commandline
localhost:5000/api/films/
```
```JSON
{"title": "TESTFILMNAME", 
  "release_year": 2025, 
  "length": 100, 
  "rating": "PG"}
```
#### Update the information of an film by adding some or all information and ID, using PATCH
```commandline
localhost:5000/api/films/1001
```
```json
{"first_name": "UPDATEDNAMETEST"}
```
#### Delete an film by ID, using DELETE
```commandline
localhost:5000/api/films/1001
```
----------
### Film Actor Relationship
#### Get all the films information that contain a specific actor by ID, using GET
```commandline
localhost:5000/api/film_actors/get_films/1
```
#### Get all the actors information who are part of the specific film by ID, using GET
```commandline
localhost:5000/api/film_actors/get_actors/1
```