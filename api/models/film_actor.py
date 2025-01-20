from api.models import db

# A model for film_actor
# class FilmActor(db.Model):
#     __tablename__ = "film_actor"
#     id = db.Column(db.Integer, primary_key=True)
#     actor_id = db.Column(db.Integer, db.ForeignKey("actor_id"))
#     film_id = db.Column(db.Integer, db.ForeignKey("film_id"))