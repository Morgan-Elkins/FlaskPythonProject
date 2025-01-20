from api.models import db
# from api.models.film_actor import FilmActor
from api.models.film import Film

# A model for our actor table
class Actor(db.Model):
    __tablename__ = "actor"
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    film = db.relationship('Film', secondary='film_actor', back_populates='actor')
