from application.extensions import mysql
from .abc import BaseModel


class Role(mysql.Model, BaseModel):
    """ The User model """
    __tablename__ = 'role'

    id = mysql.Column(mysql.Integer, primary_key=True, autoincrement=True)
    name = mysql.Column(mysql.String(80))
    desc = mysql.Column(mysql.String(250))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
