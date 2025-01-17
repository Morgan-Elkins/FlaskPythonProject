from api.models.actor import Actor
from api.schemas import ma


# Auto-generate a schema fpr actor models to use for serialise and validate actor data
class ActorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Actor


actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)