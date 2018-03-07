from flask import jsonify
from functools import wraps


def promise_required(fn):
    @wraps(fn)
    def promise_check(*args, **kwargs):
        has_promise = False
        if has_promise:
            return fn(*args, **kwargs)
        else:
            return jsonify({'promise': '你没有权限!'})
    return promise_check
