# encoding: utf-8
from application.controllers.user import user_bp
from application.controllers.role import role_bp

all_bp = [
    role_bp,
    user_bp
]
