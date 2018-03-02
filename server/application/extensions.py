# encoding: utf-8

from flask_jwt import JWT
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from flask_restful import Api

jwt = JWT()
login_manager = LoginManager()
mongo = MongoEngine()
mysql = SQLAlchemy()
api = Api()
