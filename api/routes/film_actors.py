from flask import Blueprint, request, jsonify, render_template
from marshmallow import ValidationError

from api.models import db
from api.models.actor import Actor
from api.models.film import Film
from api.schemas.actor import actor_schema, actors_schema
from api.schemas.film import films_schema

#Create module to insert into flask app
film_actors_router = Blueprint('film_actors', __name__, url_prefix='/film_actors')

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
            return f"The film id: {film_id} is invalid", 404

    return actors_schema.dump(films.actor)

@film_actors_router.route('/home_get_films/<actor_id>')
def home_films(actor_id):
    page = request.args.get('page', 1, type=int)  # Default to page 1 if not specified
    actors = Actor.query.filter_by(actor_id = actor_id).first()
    if actors == None:
            return f"The film id: {actor_id} is invalid", 404
    films = actors.film.paginate(page=page, per_page=10, error_out=False)
    return render_template('index_films.html', items=films.items, pagination=films)


@film_actors_router.route('/home_get_actors/<film_id>')
def home_actors(film_id):
    page = request.args.get('page', 1, type=int)  # Default to page 1 if not specified
    films = Film.query.filter_by(film_id = film_id).first()
    if films == None:
            return f"The film id: {film_id} is invalid", 404
    actors = films.actor.paginate(page=page, per_page=10, error_out=False)
    return render_template('index_actors.html', items=actors.items, pagination=actors)

@film_actors_router.patch('/link_actor_to_film/<actor_id>,<film_id>')
def link_actor_to_film(actor_id, film_id):
    # Check that actor not already linked with film
    film = Film.query.get(film_id)
    if film == None:
            return f"The film id: {film_id} is invalid", 404

    actor = Actor.query.get(actor_id)
    if actor == None:
            return f"The actor id: {actor_id} is invalid", 404

    actor_in_film = any(x.actor_id == int(actor_id) for x in film.actor )

    # If actor already linked then don't update
    if (actor_in_film):
        return actors_schema.dump(film.actor)
    else:
        film.actor.append(actor)
        db.session.commit()
        return actors_schema.dump(film.actor)



