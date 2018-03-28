from flask import jsonify, request
from functools import wraps
from flask_jwt import current_identity


def promise_required(fn):
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
            return jsonify({'promise': '你没有权限!'})

    return promise_check


def role_required(role=''):
    """ 传入用户权限列表 """
    print(role)
    def func_wrapper(fn):
        print(fn)
        @wraps(fn)
        def role_check(*args, **kwargs):
            print(kwargs)
            # roles_list = current_identity.roles_list
            # has_promise = False
            # for role in roles_list:
            #     if (request.path == role['url'] and request.method == role['method']):
            #         has_promise = True
            #
            # if has_promise:
            #     return fn(*args, **kwargs)
            # else:
            #     return jsonify({'promise': '你没有权限!'})
            return fn(*args, **kwargs)
        return role_check
    return func_wrapper

