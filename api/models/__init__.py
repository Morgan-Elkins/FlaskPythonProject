from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Auxilery table for films and actors
# actor_film = db.Table(
#     "actor_film",
#     db.Column("actor_id", db.Integer, db.ForeignKey("actor_id")),
#     db.Column("film_id", db.Integer, db.ForeignKey("film_id")),
# )