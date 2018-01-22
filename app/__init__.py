from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

database = SQLAlchemy()
login = LoginManager()

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	Bootstrap(app)
	db.init_app(app)
	login.init_app(app)
	login.login_message = "Harus Login Terlebih dahulu"
	login.login_view = "Login.Login.html"
	migrate = Migrate(app, db)

	from app import models

	from .Login import Login as login_blueprint
	app.register_blueprint(login_blueprint)

	from .HomePage import HomePage as home_blueprint
	app.register_blueprint(home_blueprint)

	from .Siswa import Siswa as siswa_blueprint
	app.register_blueprint(siswa_blueprint)

	from .Admin import Admin as admin_blueprint
	app.register_blueprint(admin_blueprint)

	from .Ppdb import Ppdb as ppdb_blueprint
	app.register_blueprint(ppdb_blueprint)