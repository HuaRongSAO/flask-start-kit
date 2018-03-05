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
    password = mysql.Column(mysql.String(250), nullable=False)
    create_time = mysql.Column(mysql.DateTime)
    update_time = mysql.Column(mysql.DateTime)

    def __init__(self, username, email, phone, password, create_time, update_time):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.create_time = create_time
        self.update_time = update_time
