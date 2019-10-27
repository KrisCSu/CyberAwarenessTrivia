import os

class Config:
	# General Config
	SECRET_KEY = '11c1425ef97b675b013cde72f843499d'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

	# Mail Config
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')