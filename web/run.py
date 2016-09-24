from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy

from server import app, db
from server.views import * 
from server.rest_server import *

# Turn off tracking of modifications

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
