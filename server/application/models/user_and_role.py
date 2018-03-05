from application.extensions import mysql
from .abc import BaseModel


class UserAndRole(mysql.Model, BaseModel):
    __tablename__ = 'user_and_role'

    id = mysql.Column(mysql.Integer, primary_key=True)
    user_id = mysql.Column(mysql.Integer)
    role_id = mysql.Column(mysql.Integer)
    create_time = mysql.Column(mysql.DateTime)
    create_time = mysql.Column(mysql.DateTime)

    def __init__(self, user_id, role_id, create_time, update_time):
        self.user_id = user_id
        self.role_id = role_id
        self.create_time = create_time
        self.update_time = update_time
