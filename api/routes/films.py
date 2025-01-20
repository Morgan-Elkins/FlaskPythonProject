from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.film import Film
from api.schemas.film import film_schema, films_schema

#Create module to insert into flask app
films_router = Blueprint('films', __name__, url_prefix='/films')

@films_router.get('/')
def read_all_films():
    films = Film.query.all()
    return films_schema.dump(films)

# GET requests to a specific document in collection return a single film
@films_router.get('/<film_id>')
def read_film(film_id):
    film = Film.query.get(film_id)
    return film_schema.dump(film)

# TOTEST ->
@films_router.post('/')
def create_film():
    film_data = request.json

    try:
        film_schema.load(film_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    film = Film(**film_data)
    db.session.add(film)
    db.session.commit()

    return film_schema.dump(film)