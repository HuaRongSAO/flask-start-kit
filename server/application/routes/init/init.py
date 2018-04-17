# encoding: utf-8
from flask import jsonify
from flask_restful import Resource

from application.util import hash_encrypt, now_datetime
from application.models import Promise, UserAndRole, User, Role


class Init(Resource):
    def get(self):
        user = User.query.filter_by(username='admin').first()
        if user:
            return jsonify({'status': 'fail', 'message': '你已经初始化过了'})
        init_promise()
        init_role()
        init_user()
        init_user_and_role()
        
        return jsonify({'status': 'success', 'message': 'init成功'})


def init_promise():
    Promise(url='/*', desc='开放所有权限', method='GET', create_time=now_datetime(),
            update_time=now_datetime()).save()
    Promise(url='/auth', desc='登入权限权限', method='POST', create_time=now_datetime(),
            update_time=now_datetime()).save()
    Promise(url='/api/users', desc='查看用户权限', method='GET', create_time=now_datetime(),
            update_time=now_datetime()).save()
    Promise(url='/api/users', desc='新增用户权限', method='POST', create_time=now_datetime(),
            update_time=now_datetime()).save()
    Promise(url='/api/users', desc='修改用户权限', method='PUT', create_time=now_datetime(),
            update_time=now_datetime()).save()
    Promise(url='/api/users', desc='删除用户权限', method='DELETE', create_time=now_datetime(),
            update_time=now_datetime()).save()


def init_role():
    Role(name='admin', desc='管理员', promise_id=1, create_time=now_datetime(),
         update_time=now_datetime()).save()
    Role(name='user', desc='用户', promise_id=2, create_time=now_datetime(),
         update_time=now_datetime()).save()


def init_user():
    User(username='admin', password=hash_encrypt('123456'), email='admin@flask.com', create_time=now_datetime(),
         update_time=now_datetime(), phone='18259261803').save()
    User(username='user', password=hash_encrypt('123456'), email='user@flask.com', create_time=now_datetime(),
         update_time=now_datetime(), phone='18259261802').save()
    User(username='user1', password=hash_encrypt('123456'), email='user1@flask.com', create_time=now_datetime(),
         update_time=now_datetime(), phone='18259261804').save()


def init_user_and_role():
    UserAndRole(user_id=1, role_id=1, create_time=now_datetime(),
                update_time=now_datetime()).save()
    UserAndRole(user_id=2, role_id=2, create_time=now_datetime(),
                update_time=now_datetime()).save()
    UserAndRole(user_id=3, role_id=2, create_time=now_datetime(),
                update_time=now_datetime()).save()
