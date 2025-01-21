from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Auxiliary table for films and actors
# actor_film = db.Table(
#     "film_actor",
#     db.Column("actor_id", db.Integer, db.ForeignKey("actor.actor_id")),
#     db.Column("film_id", db.Integer, db.ForeignKey("film.film_id")),
# )

# A model for film_actor table
class film_actor(db.Model):
    __tablename__ = "film_actor"
    actor_id = db.Column(db.Integer, db.ForeignKey("actor.actor_id"), primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.film_id"), primary_key=True)
