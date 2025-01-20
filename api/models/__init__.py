from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Auxiliary table for films and actors
actor_film = db.Table(
    "film_actor",
    db.Column("actor_id", db.Integer, db.ForeignKey("actor.actor_id")),
    db.Column("film_id", db.Integer, db.ForeignKey("film.film_id")),
)