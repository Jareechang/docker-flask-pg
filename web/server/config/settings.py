import os

class BaseConfig(object):
    SECRET_KEY = 'some secret'
    DEBUG = True 
    STATIC_FOLDER='client'
    DB_NAME = os.environ['POSTGRES_DB'] 
    DB_USER = os.environ['POSTGRES_USER']
    DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
    DB_PORT = os.environ['POSTGRES_PORT']

class DevelopmentConfig(BaseConfig):
    DB_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )

class ProductionConfig(BaseConfig):
    # todo
    pass

