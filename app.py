from flask import Flask, request, render_template

from api.config import config
from api.routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from api.models import db
    db.init_app(app)

    from api.schemas import ma
    ma.init_app(ma)

    app.register_blueprint(routes)

    @app.route('/')
    def home():
        # page = request.args.get('page', 1, type=int)  # Default to page 1 if not specified
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

