from api.models import db

# A model for our actor table
class Film(db.Model):
    __tablename__ = "film"
    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    language_id = db.Column(db.Integer, default=1, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String(255), nullable=False)

    actor = db.relationship('Actor', secondary='film_actor', back_populates='film')