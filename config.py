import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'vmengwa'.encode('utf-8')

    SQLALCHEMY_DATABASE_URI = os.environ.get('sqlite:///C:\\absolute\\path\\to\\app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False