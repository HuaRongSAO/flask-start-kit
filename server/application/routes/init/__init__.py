# encoding: utf-8
from flask import Blueprint
from flask_restful import Api
from .init import Init

init_blueprint = Blueprint("init", __name__)
api = Api(init_blueprint)

api.add_resource(Init, '/init')
