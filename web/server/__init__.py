from .app import create_app, create_db
from .config import settings 
import os

app = create_app()

if os.environ['FLASK_ENV'] == 'development':
    app.config.from_object(settings.DevelopmentConfig)

db = create_db(app)

