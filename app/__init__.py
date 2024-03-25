from flask import Flask
from app.config import config
import os

def create_app():
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    
    
    
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)
    
    
    f.init_app(app)
    

    
    
    
    @app.shell_context_processor
    def ctx():
        return {"app": app, }
    
    return app
