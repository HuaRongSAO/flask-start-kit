from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask',
    'host': 'localhost',
    'port': 27017
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mongo = MongoEngine()
mongo.init_app(app)

mysql = SQLAlchemy(app)
mysql.drop_all()
mysql.create_all()

manager = Manager(app)
migrate = Migrate(app, mysql)


class User(mongo.Document):
    name = mongo.StringField()
    email = mongo.StringField()


class Admin(mysql.Model):
    __tablename__ = 'admins'
    id = mysql.Column(mysql.Integer, primary_key=True)
    username = mysql.Column(mysql.String(80), unique=True)
    email = mysql.Column(mysql.String(320), unique=True)
    password = mysql.Column(mysql.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
