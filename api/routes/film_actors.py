from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.actor import Actor
from api.models.film import Film
from api.schemas.actor import actor_schema, actors_schema
from api.schemas.film import films_schema


#Create module to insert into flask app
film_actors_router = Blueprint('film_actors', __name__, url_prefix='/film_actors')

@film_actors_router.get('/')
def read_all_film_actors():
    filaActors = Actor.query.all()
    print("HELLO")
    return actors_schema.dump(filaActors)

# GET requests to return all films be an actor
# localhost:5000/api/film_actors/get_films/5
@film_actors_router.get('/get_films/<actor_id>')
def read_films_by_actor(actor_id):
    actors = Actor.query.get(actor_id)

    if actors == None:
            return f"The actor id: {actor_id} is invalid", 404

    return films_schema.dump(actors.film)

@film_actors_router.get('/get_actors/<film_id>')
def read_actors_by_film(film_id):
    films = Film.query.get(film_id)

    if films == None:
            return f"The actor id: {film_id} is invalid", 404

    return actors_schema.dump(films.actor)
