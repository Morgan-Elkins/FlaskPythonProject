from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.film_actor import FilmActor
from api.schemas.actor import actor_schema
from api.schemas.film_actor import film_actor_schema, film_actors_schema

#Create module to insert into flask app
film_actors_router = Blueprint('film_actors', __name__, url_prefix='/film_actors')

@film_actors_router.get('/')
def read_all_film_actors():
    actors = FilmActor.query.all()
    return film_actors_schema.dump(actors)

