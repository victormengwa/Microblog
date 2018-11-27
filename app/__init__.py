from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

#instantiating the db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#the bottom iimport call is a workaround to circular import
from app import routes, models