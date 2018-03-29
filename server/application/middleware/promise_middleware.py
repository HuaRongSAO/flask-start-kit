from flask import request, abort
from functools import wraps
from functional import seq
from flask_jwt import current_identity


def promise_required(fn):
    """
        通过 用户 角色  路由 来控制权限
        用户包含多种角色
        角色又包含多种 路由权限
    """

    @wraps(fn)
    def promise_check(*args, **kwargs):
        promise_list = current_identity.promise_list
        has_promise = False
        for promise in promise_list:
            if (request.path == promise['url'] and request.method == promise['method']):
                has_promise = True

        if has_promise:
            return fn(*args, **kwargs)
        else:
            return abort(401)

    return promise_check


def role_required(role=[]):
    """ 传入用户权限列表 """

    def func_wrapper(fn):
        @wraps(fn)
        def role_check(*args, **kwargs):
            has_promise = False
            roles_list = current_identity.roles_list
            for ro in roles_list:
                if ro['name'] == 'admin': has_promise = True
                for r in role:
                    if ro['name'] == r: has_promise = True
            if not has_promise:
                return abort(401)
            return fn(*args, **kwargs)

        return role_check

    return func_wrapper
