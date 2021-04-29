import os
from dotenv import load_dotenv
load_dotenv()
#contains all the
class Config:
    
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = ('postgresql+psycopg2://kigen:29584933@localhost/pitch')
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}