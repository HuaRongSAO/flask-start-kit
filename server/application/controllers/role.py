# encoding: utf-8
from flask import Blueprint, jsonify

role_bp = Blueprint('roles', __name__, url_prefix='')


@role_bp.route('/', methods=['get'])
def roles():
    return jsonify({'home': 'home'})
