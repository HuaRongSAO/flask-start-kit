"""
Define the User model
"""
from application.extensions import mysql
from .abc import BaseModel


class User(mysql.Model, BaseModel):
    """ The User model """
    __tablename__ = 'user'

    id = mysql.Column(mysql.Integer, primary_key=True, autoincrement=True)
    username = mysql.Column(mysql.String(80), unique=True)
    email = mysql.Column(mysql.String(250), unique=True)
    phone = mysql.Column(mysql.String(11), unique=True)
    password = mysql.Column(mysql.String(32), nullable=False)

    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
