# encoding: utf-8
from application.routes import api_blueprint
from application.routes.init import init_blueprint

all_bp = [
    api_blueprint,
    init_blueprint
]
