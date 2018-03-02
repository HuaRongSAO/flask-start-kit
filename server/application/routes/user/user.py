# encoding: utf-8
from flask import jsonify
from sqlalchemy import or_
from flask_restful import Resource, reqparse, fields
from flask_jwt import jwt_required
from application.util import hash_encrypt

from application.routes import api, meta_fields
from application.models.user import User
from application.util import InvalidUsage
from application.extensions import mysql

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
    @jwt_required()
    def get(self):
        users = User.query.all()
        users_json = []
        for user in users:
            users_json.append(user.json)
        return {'users': users_json}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='username 必填选项')
        parser.add_argument('password', required=True, help='password 必填选项')
        parser.add_argument('email', required=True, help='email 必填选项')
        parser.add_argument('phone')

        args = parser.parse_args()
        password = hash_encrypt(bytes(args['password'], 'utf-8'))
        try:
            user = User(username=args['username'], email=args['email'],
                        phone=args['phone'], password=password).save()
        except Exception as e:
            raise InvalidUsage('添加用户失败', status_code=500, payload={'error': '{}'.format(e)})
        return {'user': user.json}


class UserInfo(Resource):
    def get(self, query):
        user = mysql.session.query(User).filter(
            or_(User.id == query, User.username == query, User.email == query)).first()
        if not user:
            return jsonify({'status': 'fail', 'user': {}})
        user_json = {
            "id": user.json["id"],
            "email": user.json["email"],
            "phone": user.json["phone"],
            "username": user.json["username"],
        }
        return jsonify({'status': 'success', 'user': user_json})

    def put(self, query):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        parser.add_argument('email')
        parser.add_argument('phone')

        args = parser.parse_args()
        print(args)
        username = args['username']
        password = args['password']
        email = args['email']
        phone = args['phone']

        user = User.query.filter(User.id == query).first()
        if username != '':
            user.username = username
        if username != '':
            user.password = password
        if username != '':
            user.email = email
        if username != '':
            user.phone = phone
        try:
            mysql.session.merge(user)
            mysql.session.commit()
        except Exception as e:
            raise InvalidUsage('更新用户失败', status_code=500, payload={'error': '{}'.format(e)})
        return jsonify({'status': 'success', 'user': user.json})

    def delete(self, query):
        user = User.query.filter(User.id == query).first()
        if not user:
            return jsonify({'status': 'fail', 'user': {}})
        else:
            try:
                user.delete()
            except Exception as e:
                raise InvalidUsage('删除用户失败', status_code=500, payload={'error': '{}'.format(e)})
        return jsonify({'status': 'success', 'user': user.json})


api.add_resource(UserInfo, '/user/<string:query>', '/user/<string:id>')
api.add_resource(UserController, '/user')
