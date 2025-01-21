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
```URL
localhost:5000/api/actors/
```
#### Get specific actor by id (e.g. actor_id: 1), using GET
```URL
localhost:5000/api/actors/1
```
#### Create a new actor by entering all info, using POST
```URL
localhost:5000/api/actors/
```
```JSON
{"first_name": "FIRSTNAMETEST",
"last_name": "LASTNAMETEST"}
```
#### Update the information of an actor by adding some or all information and ID, using PATCH
```URL
localhost:5000/api/actors/201
```
```json
{"first_name": "UPDATEDNAMETEST"}
```
#### Delete an actor by ID, using DELETE
```URL
localhost:5000/api/actors/201
```
--------------------
### Films
#### Get all films, using GET
```URL
localhost:5000/api/films/
```
#### Get specific film by id , using GET
```URL
localhost:5000/api/films/1
```
#### Create a new film by entering all info, using POST
```URL
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
{"title": "TESTFILMNAME2", "length": 120, "rating": "PG-13"}
```
#### Delete an film by ID, using DELETE
```URL
localhost:5000/api/films/1001
```
----------
### Film Actor Relationship
#### Get all the films information that contain a specific actor by ID, using GET
```URL
localhost:5000/api/film_actors/get_films/1
```
#### Get all the actors information who are part of the specific film by ID, using GET
```URL
localhost:5000/api/film_actors/get_actors/1
```
------------------
## Pagination
Used code from [this website](https://devoriales.com/post/323/how-to-implement-pagination-in-your-flask-application) as a template to implement pagination
### Actors
```URL
http://localhost:5000/api/actors/home/
```
### Films
```URL
http://localhost:5000/api/films/home/
```
### Get actors by film_id
```URL
http://localhost:5000/api/film_actors/home_get_actors/1
```
### Get films by actor_id
```URL
http://localhost:5000/api/film_actors/home_get_films/1
```
------------------
## Linking association between film and actor
```URL
http://localhost:5000/api/film_actors/link_actor_to_film/1,1003
```
