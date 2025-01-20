from api.models.film import Film
from api.schemas import ma


# Auto-generate a schema fpr actor models to use for serialise and validate actor data
class FilmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Film


film_schema = FilmSchema()
films_schema = FilmSchema(many=True)