from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from cat.config import Config


db = SQLAlchemy()
admin = Admin()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	admin.init_app(app)
	from cat.models import User, Trivia
	admin.add_view(ModelView(models.User, db.session))
	admin.add_view(ModelView(models.Trivia, db.session))
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from cat.main.routes import main
	from cat.users.routes import users
	from cat.trivia.routes import triviaa
	app.register_blueprint(main)
	app.register_blueprint(users)
	app.register_blueprint(triviaa)

	return app