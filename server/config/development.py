# coding: utf-8
import os


class DevelopmentConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    TESTING = False
    SECRET_KEY = "sample_key"

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Site domain
    SITE_TITLE = "flask"
    SITE_DOMAIN = "http://localhost:8080"

    # mysql 配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # mongo 配置
    MONGODB_SETTINGS = {
        'db': 'flask',
        'host': 'localhost',
        'port': 27017
    }
