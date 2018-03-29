# encoding: utf-8
from application.models import User, UserAndRole, Role, Promise


def UserAuth(user_id=None):
    user = User.query.filter_by(id=user_id).first()
    user_and_roles = UserAndRole.query.filter_by(user_id=user_id).all()
    promise_list, roles_list = [], []
    for role in user_and_roles:
        role_dist = Role.query.filter_by(id=role.role_id).first()
        user.is_admin = False
        if role_dist.name == 'admin': user.is_admin = True
        roles_list.append(role_dist.json)
        promise = Promise.query.filter_by(id=role_dist.promise_id).first()
        promise_list.append(promise.json)
    user.roles_list = roles_list
    user.promise_list = promise_list
    return user
