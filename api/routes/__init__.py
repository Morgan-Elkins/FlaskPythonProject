from flask import Blueprint

from api.routes.actors import actors_router

# Create a route module to be registered
routes = Blueprint('api', __name__, url_prefix='/api')

# Register nested routes
routes.register_blueprint(actors_router)