import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = ('postgresql+psycopg2://kigen:29584933@localhost/pitch')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY= ('29584933')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = ("kenyakigen6@gmail.com")
    MAIL_PASSWORD = ("374029584933")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = ('postgresql+psycopg2://kigen:29584933@localhost/pitch')

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}