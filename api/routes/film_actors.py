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

# GET requests to a specific document
@film_actors_router.get('/<actor_id>')
def read_films_by_actor(actor_id):
    actors = Actor.query.get(actor_id)

    if actors == None:
            return f"The actor id: {actor_id} is invalid", 404

    return films_schema.dump(actors.film)