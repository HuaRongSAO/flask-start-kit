from application.extensions import mysql
from .abc import BaseModel


class Promise(mysql.Model, BaseModel):
    __tablename__ = "promise"

    id = mysql.Column(mysql.Integer, primary_key=True)
    url = mysql.Column(mysql.String(250))
    method = mysql.Column(mysql.String(12))
    desc = mysql.Column(mysql.String(80))
    create_time = mysql.Column(mysql.DateTime)
    update_time = mysql.Column(mysql.DateTime)

    def __init__(self, url, method, desc, create_time, update_time):
        self.url = url
        self.desc = desc
        self.method = method
        self.create_time = create_time
        self.update_time = update_time
