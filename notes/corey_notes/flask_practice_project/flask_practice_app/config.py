import os

class Config:
    SECRET_KEY = 'd6753ab27f50e1f2c49228a7aebb4fc7'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_database.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')