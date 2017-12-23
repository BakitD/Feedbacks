import os


basedir = os.path.abspath(os.path.dirname(__file__))

DATABSE_NAME = 'database.sqlite'


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'change this string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DATABSE_NAME)


class TestingConfig(Config):
	pass


class ProductionConfig(Config):
	pass


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig
}

