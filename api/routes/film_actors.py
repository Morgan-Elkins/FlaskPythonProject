from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
# from api.models.film_actor import FilmActor
from api.models.actor import Actor
from api.models.film import Film
from api.schemas.actor import actor_schema, actors_schema
from api.schemas.film import films_schema

# from api.schemas.film_actor import film_actor_schema, film_actors_schema

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
    # films_ = actors.film.title
    print(actors.film)
    # print(actor_id)
    # print(actors[0])
    # print(actors[0].actor_id == int(actor_id))
    # print(type(actors[0].actor_id) , type(actor_id))
    # for element in actors:
    #     if element.actor_id == int(actor_id):
    #         print(element.actor_id, element.film_id)
    #     else:
    #         if (element.actor_id == int(4)):
    #             print(f"{element.actor_id == int(293)} ({element.actor_id} {element.film_id}), ", end="")
    # print("")
    # films_id = [x for x in actors if x.actor_id == int(actor_id)]
    # print(films_id)
    # data_ = Film.query.filter(films).all()
    return films_schema.dump(actors.film)