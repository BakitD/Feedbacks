from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config


db = SQLAlchemy()

from .main import main
from . import models

class Application(object):

	@staticmethod
	def create_app(configName='development'):
		application = Flask(__name__)
		application.config.from_object(config[configName])
		config[configName].init_app(application)

		db.init_app(application)

		application.register_blueprint(main)

		return application

