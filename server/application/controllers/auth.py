# encoding: utf-8
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    pass


@auth_bp.route('/logout', methods=['POST'])
def logout():
    pass
