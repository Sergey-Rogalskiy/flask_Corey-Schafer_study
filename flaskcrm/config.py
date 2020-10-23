import os


class Config:
    SECRET_KEY = os.environ.get('MY_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('MY_SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MY_EMAIL')
    MAIL_PASSWORD = os.environ.get('MY_EMAIL_PASS')
