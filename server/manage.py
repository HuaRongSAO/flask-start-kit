from flask_script import Manager
from flask_script.commands import ShowUrls
from flask_migrate import Migrate, MigrateCommand
from application import create_app
from application.extensions import mysql
# from application.models.user import User

app = create_app()
manager = Manager(app)
migrate = Migrate(app, mysql)

# User(username='admin', email='admin@admin.com', phone='18259261802', password='123456').save()
#
# for i in range(10):
#     User(username='user{}'.format(i), email='user{}@admin.com'.format(i), phone='1825926181{}'.format(i),
#          password='123456').save()

manager.add_command('db', MigrateCommand)
manager.add_command("showurls", ShowUrls())

if __name__ == "__main__":
    manager.run()
