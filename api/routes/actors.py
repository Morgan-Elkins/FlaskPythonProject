from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.actor import Actor
from api.schemas.actor import actor_schema, actors_schema

#Create module to insert into flask app
actors_router = Blueprint('actors', __name__, url_prefix='/actors')

@actors_router.get('/')
def read_all_actors():
    actors = Actor.query.all()
    return actors_schema.dump(actors)

# GET requests to a specific document in collection return a single actor
@actors_router.get('/<actor_id>')
def read_actor(actor_id):
    actor = Actor.query.get(actor_id)
    return actor_schema.dump(actor)

# TOTEST ->{"first_name": "TEST1", "last_name": "TEST1LAST"}
@actors_router.post('/')
def create_actor():
    actor_data = request.json

    try:
        actor_schema.load(actor_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    actor = Actor(**actor_data)
    db.session.add(actor)
    db.session.commit()

    return actor_schema.dump(actor)

# TOTEST -> localhost:5000/api/actors/201 (if done create before)
@actors_router.delete('/<actor_id>')
def delete_actor(actor_id):
    actor = Actor.query.get(actor_id)
    db.session.delete(actor)
    db.session.commit()
    return actors_schema.dump("")

@actors_router.patch('/<actor_id>')
def update_actor(actor_id):
    actor = Actor.query.get(actor_id)
    actor_data = request.json

    # print(actor_data)
    # print(actor.first_name)

    # try:
    #     actor_schema.load(actor_data)
    # except ValidationError as err:
    #     return jsonify(err.messages), 400

    print(actor_data)

    # new_actor = Actor()
    # new_actor.actor_id = actor.actor_id
    # new_actor.first_name = actor.first_name
    # new_actor.last_name = actor.last_name
    if (actor_data.get("first_name") != "" and actor_data.get("first_name") != None):
        actor.first_name = actor_data.get("first_name")
        print("Updated First")
    if (actor_data.get("last_name") != "" and actor_data.get("last_name") != None):
        actor.last_name = actor_data.get("last_name")
        print("Updated Last")

    print(actor.actor_id, actor.first_name, actor.last_name)

    db.session.add(actor)
    db.session.commit()

    dump_data = actors_schema.dump("")
    return dump_data