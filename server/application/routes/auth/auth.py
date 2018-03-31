from flask import jsonify
from flask_restful import Resource
from application.routes import api
from flask_jwt import jwt_required, current_identity


class Auth(Resource):
    @jwt_required()
    def get(self):
        """ 登入验证 """
        current_identity
        user = current_identity.json
        del (user['password'])
        user['is_admin'] = current_identity.is_admin
        user['promise_list'] = current_identity.promise_list
        user['roles_list'] = current_identity.roles_list
        return jsonify(user)


api.add_resource(Auth, '/auth/login')
