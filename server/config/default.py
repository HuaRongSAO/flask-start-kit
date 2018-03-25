# coding: utf-8
import os
from  datetime import timedelta


class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    TESTING = False
    
    PASSWORD_KEY = '消灭人类暴政,世界属于三体'
    SECRET_KEY = "sample_key"
    
    # jwt 配置
    JWT_AUTH_USERNAME_KEY = "username"
    JWT_AUTH_PASSWORD_KEY = "password"
    JWT_AUTH_URL_RULE = '/api/auth'
    # token 过期时间
    JWT_EXPIRATION_DELTA = timedelta(seconds=30000)
    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Site domain
    PORT = 5000
    SITE_TITLE = "flask"
    SITE_DOMAIN = "http://localhost"
    
    # mysql 配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    # mongo 配置
    MONGODB_SETTINGS = {
        'db': 'flask',
        'host': 'localhost',
        'port': 27017
    }
