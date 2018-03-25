# encoding: utf-8
from flask import jsonify
from sqlalchemy import or_
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from application.util import hash_encrypt
from application.routes import api
from application.models.user import User
from application.middleware import promise_required
from application.util import InvalidUsage
from application.extensions import mysql


class UserController(Resource):
    @jwt_required()
    @promise_required
    def get(self):
        users = User.query.all()
        users_json = []
        
        for user in users:
            users_json.append(user.json)
        return {
            "user": current_identity.json if current_identity else {},
            "promise_list": current_identity.promise_list if current_identity else {},
            "roles": current_identity.roles_list,
            'users': users_json
        }
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='username 必填选项')
        parser.add_argument('password', required=True, help='password 必填选项')
        parser.add_argument('email', required=True, help='email 必填选项')
        parser.add_argument('phone')
        
        args = parser.parse_args()
        password = hash_encrypt(args['password'])
        try:
            user = User(username=args['username'], email=args['email'],
                        phone=args['phone'], password=password).save()
        except Exception as e:
            raise InvalidUsage(message='添加用户失败', status_code=500, payload={'error': '{}'.format(e)})
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
            raise InvalidUsage(message='更新用户失败', status_code=500, payload={'error': '{}'.format(e)})
        return jsonify({'status': 'success', 'user': user.json})
    
    def delete(self, query):
        user = User.query.filter(User.id == query).first()
        if not user:
            return jsonify({'status': 'fail', 'user': {}})
        else:
            try:
                user.delete()
            except Exception as e:
                raise InvalidUsage(message='删除用户失败', status_code=500, payload={'error': '{}'.format(e)})
        return jsonify({'status': 'success', 'user': user.json})


api.add_resource(UserInfo, '/user/<string:query>', '/user/<string:id>')
api.add_resource(UserController, '/user')
