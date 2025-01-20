from api.models import db

# A model for our actor table
class Film(db.Model):
    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String(255), nullable=False)