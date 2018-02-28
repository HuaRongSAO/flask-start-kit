# encoding: utf-8
from flask_jwt import JWT
from flask.ext.mongoengine import MongoEngine


db = MongoEngine()
login_manager = LoginManager()
admin = Admin()
jwt = JWT()