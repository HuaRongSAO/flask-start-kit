from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
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

manager = Manager(app)
migrate = Migrate(app, mysql)

class User(mongo.Document):
    name = mongo.StringField()
    email = mongo.StringField()


class Admin(mysql.Model):
    __tablename__ = 'admins'
    id = mysql.Column(mysql.Integer, primary_key=True, autoincrement=True)
    username = mysql.Column(mysql.String(80), unique=True)
    email = mysql.Column(mysql.String(320), unique=True)
    password = mysql.Column(mysql.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/")
def index():
    for i in range(10):
        User(name='user name : {}'.format(i), email='admin@qq.com').save()
    users = User.objects()
    return jsonify({"users": users})


@app.route("/admin")
def admin():
    admimUser = Admin(username='admin', email='admin@qq.com', password='1234')
    mysql.session.add(admimUser)
    mysql.session.commit()
    admins = Admin.query.all()
    return jsonify({"admins": admins})

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5200, debug=True)
