# encoding: utf-8
from flask import Blueprint, jsonify

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.route('/', methods=['get'])
def users():
    return jsonify({'users': 'users'})


@user_bp.route('/<string:name>', methods=['get'])
def user_info(name):
    return jsonify({'user': '{}'.format(name)})
