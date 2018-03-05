# encoding: utf-8
import types
from application.models import User, UserAndRole, Role, Promise


def UserAuth(user_id=None):
    user = User.query.filter_by(id=user_id).first()
    roles = UserAndRole.query.filter_by(user_id=user_id).all()
    promise_list = []
    for role in roles:
        role_dist = Role.query.filter_by(id=role.role_id).first()
        promise = Promise.query.filter_by(id=role_dist.promise_id).first()
        promise_list.append(promise.json)
    user.promise_list = promise_list
    return user
