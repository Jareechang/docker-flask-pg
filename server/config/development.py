# SQLALCHEMY_DATABASE_URI = \
    # "postgresql://postgres_user:testpw@localhost/my_postgres_db"

import os

SQLALCHEMY_DATABASE_URI = \
'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    os.environ['POSTGRES_USER'], 
    os.environ['POSTGRES_PASSWORD'], 
    'postgres', 
    os.environ['POSTGRES_PORT'], 
    os.environ['POSTGRES_DB']
)

STATIC_FOLDER='client'
