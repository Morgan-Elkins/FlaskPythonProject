from api.models import db

# A model for film_actor
class FilmActor(db.Model):
    actor_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, nullable=False)