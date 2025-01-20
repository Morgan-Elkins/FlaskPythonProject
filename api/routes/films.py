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

# TOTEST -> {"title": "TESTFILMNAME", "release_year": 2025, "length": 100, "rating": "PG"}
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

# TOTEST -> localhost:5000/api/films/1001 (if done create before)
@films_router.delete('/<film_id>')
def delete_film(film_id):
    film = Film.query.get(film_id)

    if film == None:
        return f"An film of ID {film_id} does not exist, so cannot be deleted" , 404

    db.session.delete(film)
    db.session.commit()
    return film_schema.dump(film)

@films_router.patch('/<film_id>')
def update_film(film_id):
    film = Film.query.get(film_id)
    film_data = request.json

    if film == None:
        return f"An film of ID {film_id} does not exist, so cannot be updated" , 404

    if (film_data.get("title") != "" and film_data.get("title") != None):
        film.title = film_data.get("title")
    if (film_data.get("release_year") != "" and film_data.get("release_year") != None):
        film.release_year = film_data.get("release_year")
    if (film_data.get("length") != "" and film_data.get("length") != None):
        film.length = film_data.get("length")
    if (film_data.get("rating") != "" and film_data.get("rating") != None):
        film.rating = film_data.get("rating")

    db.session.add(film)
    db.session.commit()
    return film_schema.dump(film)