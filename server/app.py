from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# import REST routes
import os

def create_app():
    """
        create an instance of app and returns it
    """
    app = Flask(__name__)
    return app

def create_db(app):
    """
        create an instance of database conn. and returns it

        :param app: instance of app 

    """
    db = SQLAlchemy(app)
    return db

if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'
