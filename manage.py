import os

from flask import render_template
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import Application, db
from app import models

application = Application.create_app()
manager = Manager(application)
migrate = Migrate(application, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	manager.run()