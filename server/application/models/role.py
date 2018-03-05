from application.extensions import mysql
from .abc import BaseModel


class Role(mysql.Model, BaseModel):
    """ The User model """
    __tablename__ = 'role'

    id = mysql.Column(mysql.Integer, primary_key=True, autoincrement=True)
    promise_id = mysql.Column(mysql.Integer)
    name = mysql.Column(mysql.String(80))
    desc = mysql.Column(mysql.String(250))
    create_time = mysql.Column(mysql.DateTime)
    update_time = mysql.Column(mysql.DateTime)

    def __init__(self, name, desc, promise_id, create_time, update_time):
        self.name = name
        self.desc = desc
        self.promise_id = promise_id
        self.create_time = create_time
        self.update_time = update_time
