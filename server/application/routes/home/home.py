# encoding: utf-8
from flask_restful import Resource
from application.routes import api, meta_fields

class HomeController(Resource):
    def get(self):
        return {'home': 'get'}

    def post(self):
        return {'home': 'post'}

    def put(self):
        return {'home': 'put'}

    def delete(self):
        return {'home': 'delete'}
api.add_resource(HomeController, '/home')