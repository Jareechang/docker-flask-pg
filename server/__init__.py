from .app import create_app, create_db
import os

app = create_app()
db = create_db(app)

if os.environ['FLASK_ENV'] == 'development':
    # Set up the configuration for the app
    app.config.from_pyfile(
        'config/{env}.py'.format(env=os.environ['FLASK_ENV'])
    )
