# encoding: utf-8
import json
from flask import jsonify
from flask_restful import Resource, reqparse, marshal_with, fields
from application.routes import api, meta_fields
from application.models.user import User
from application.util import InvalidUsage

parser = reqparse.RequestParser()

# Marshaled field definitions for user objects
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'password': fields.String,
}

# Marshaled field definitions for collections of user objects
user_collection_fields = {
    'items': fields.List(fields.Nested(user_fields)),
    'meta': fields.Nested(meta_fields),
}


class UserController(Resource):
    def get(self):
        users = User.query.all()
        users_json = []
        for user in users:
            users_json.append(user.json)
        return {'users': users_json}

    def post(self):
        parser.add_argument('username', required=True, help='username 必填选项')
        parser.add_argument('password', required=True, help='password 必填选项')
        parser.add_argument('email', required=True, help='email 必填选项')
        parser.add_argument('phone')

        args = parser.parse_args()
        print(args)
        try:
            user = User(username=args['username'], email=args['email'],
                        phone=args['phone'], password=args['password']).save()
        except Exception:
            raise InvalidUsage('添加用户失败', status_code=500)
        return {'user': user.json}


class UserInfo(Resource):
    def get(self, query):
        user = User.query.filter_by(username=query).first()
        return jsonify({'success': 'success', 'user': user.json})

    def put(self):
        return {'hello': 'put'}

    def delete(self):
        return {'delete': 'delete'}


api.add_resource(UserInfo, '/user/<string:query>')
api.add_resource(UserController, '/user')
