from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# import REST routes
import os

def create_app():
    app = Flask(__name__)
    return app

def create_db(app):
    db = SQLAlchemy(app)
    return db

# set development as default
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'
