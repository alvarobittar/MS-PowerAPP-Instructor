from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.database import FULL_URL_DB
import os


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    #config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # f = config.factory(config_name if config_name else 'development')
    # app.config.from_object(f)
    app.debug = True
    # f.init_app(app)
    db.init_app(app)
    #migrate.init_app(app, db)

    # @app.shell_context_processor
    # def ctx():
    #     return {"app": app, "db": db}
    
    return app