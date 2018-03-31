# encoding: utf-8
from flask import jsonify, abort, request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from application.util import hash_encrypt
from application.routes import api
from application.middleware import promise_required, role_required
from application.util import InvalidUsage
from application.controllers import user_controller


class UserController(Resource):
    @jwt_required()
    @role_required(role=['admin', 'user'])
    def get(self):
        """ 获取用户列表 """
        count = user_controller.get_user_count()
        page_index = int(request.args.get('page_index') or 0)
        page_size = int(request.args.get('page_size') or 10)
        users = user_controller.get_user_list(page_index=page_index, page_size=page_size)
        users_json = []
        for user in users:
            user_json = user.json
            del (user_json['password'])
            users_json.append(user_json)
        return {
            'count': count,
            'list': users_json
        }
    
    @jwt_required()
    @role_required(role=['admin'])
    def post(self):
        """ 新增用户 """
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='username 必填选项')
        parser.add_argument('password', required=True, help='password 必填选项')
        parser.add_argument('email', required=True, help='email 必填选项')
        parser.add_argument('phone')
        
        args = parser.parse_args()
        password = hash_encrypt(args['password'])
        username = args['username']
        email = args['email']
        phone = args['phone']
        try:
            user = user_controller.create_user(username=username, email=email,
                                               phone=phone, password=password).json
        except Exception as e:
            raise InvalidUsage(message='添加用户失败', status_code=500, payload={'error': '{}'.format(e)})
        del (user['password'])
        return {'status': 'success', 'user': user}


class UserInfo(Resource):
    def get(self, id):
        """ 通过id获取用户信息 """
        user = user_controller.get_user_by_id_or_name(id).json
        if not user:
            abort(404)
        del (user['password'])
        return jsonify({'status': 'success', 'user': user})
    
    @jwt_required()
    @role_required(role=['admin', 'user'])
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        parser.add_argument('email')
        parser.add_argument('phone')
        
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        email = args['email']
        phone = args['phone']
        if current_identity.id != id and (not current_identity.is_admin): abort(401)
        try:
            user = user_controller.update_user(id=id, username=username, email=email,
                                               phone=phone, password=password).json
        except Exception as e:
            if (e.code == 404): raise e
            raise InvalidUsage(message='更新用户失败', status_code=500, payload={'error': '{}'.format(e)})
        del (user['password'])
        return jsonify({'status': 'success', 'user': user})
    
    @jwt_required()
    @role_required(role=['admin'])
    def delete(self, id):
        try:
            user = user_controller.delete_user_by_id(id)
        except Exception as e:
            if (e.code == 404): raise e
            raise InvalidUsage(message='删除用户失败', status_code=500, payload={'error': '{}'.format(e)})
        return jsonify({'status': 'success', 'user': user.json})


api.add_resource(UserInfo, '/user/<int:id>', '/user/<string:id>')
api.add_resource(UserController, '/user')
