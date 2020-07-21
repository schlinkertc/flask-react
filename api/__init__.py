"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')
    #app.config.from_pyfile('config.py')

    db.init_app(app)

    # assets = Environment()
    # assets.init_app(app)

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        #from .assets import compile_static_assets

        # Import Dash application
        from .plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        # Compile static assets
        #compile_static_assets(assets)

        # Database tables
        db.create_all()

        return app
