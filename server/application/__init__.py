# encoding: utf-8
import logging
from flask import Flask, current_app, jsonify, request
from datetime import datetime
from config import load_config
from application.blueprints import all_bp
from application.extensions import login_manager, jwt, mongo, mysql
from application.models import User
from application.util import InvalidUsage, hash_encrypt
from application.controllers import UserAuth


def create_app():
    """Create Flask app."""
    config = load_config()

    app = Flask(__name__)
    app.config.from_object(config)

    # Register components
    configure_logging(app)
    register_extensions(app)
    register_blueprint(app)

    # 拦截器
    before_request(app)

    # 异常捕获
    exception_controller(app)
    return app


def register_extensions(app):
    """ 注册models """
    mysql.init_app(app)
    mongo.init_app(app)

    # 注册用户认证
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()

    # jwt config
    def jwt_authenticate(username, password):
        logging.info("username:{}\npassword:{}\n".format(username, password))
        hash_password = hash_encrypt(password)
        user = User.query.filter_by(email=username, password=hash_password).first()
        return user

    def jwt_identity(payload):
        logging.info("payload:{}".format(payload))
        user_id = payload['identity']
        user = UserAuth(user_id=user_id)
        return user

    def make_payload(identity):
        iat = datetime.utcnow()
        exp = iat + current_app.config.get('JWT_EXPIRATION_DELTA')
        nbf = iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')
        identity = str(identity.id)
        return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': identity}

    jwt.authentication_handler(jwt_authenticate)
    jwt.identity_handler(jwt_identity)
    jwt.jwt_payload_handler(make_payload)

    jwt.init_app(app)


def register_blueprint(app):
    """ 注册蓝图 """
    for bp in all_bp:
        app.register_blueprint(bp)


def configure_logging(app):
    pass


def exception_controller(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({'status': '404'})

    @app.errorhandler(500)
    def page_error_handler(error):
        return jsonify({'status': '500'})

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


def before_request(app):
    @app.before_request
    def before_request():
        ip = request.remote_addr
        url = request.url
        print(ip)
        print(url)
