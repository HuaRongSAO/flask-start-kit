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


def role_required(fn):
    @wraps(fn)
    def role_check(*args, **kwargs):
        return jsonify({'promise': '你没有权限!'})
