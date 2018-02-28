from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine

from application import create_app
from config import load_config

config = load_config()
app = create_app()

mongo = MongoEngine(app)
mysql = SQLAlchemy(app)
