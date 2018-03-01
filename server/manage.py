from flask_script import Manager
from flask_script.commands import ShowUrls
from flask_migrate import Migrate, MigrateCommand
from application import create_app
from application.extensions import mysql

app = create_app()
manager = Manager(app)
migrate = Migrate(app, mysql)


manager.add_command('db', MigrateCommand)
manager.add_command("showurls", ShowUrls())

if __name__ == "__main__":
    manager.run()
