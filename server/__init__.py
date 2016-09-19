from .app import create_app, create_db
import os

app = create_app()

if os.environ['FLASK_ENV'] == 'development':
    app.config.from_pyfile(
        'config/{env}.py'.format(env=os.environ['FLASK_ENV'])
    )

db = create_db(app)

