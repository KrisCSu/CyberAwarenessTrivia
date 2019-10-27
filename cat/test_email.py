from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
		"MAIL_SERVER": 'smtp.gmail.com',
		"MAIL_PORT": 465,
		"MAIL_USE_TLS": False,
		"MAIL_USE_SSL": True,
		"MAIL_USERNAME": os.environ.get('EMAIL_USER'),
		"MAIL_PASSWORD": os.environ.get('EMAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
		with app.app_context():
				msg = Message(subject="Hello",
											sender=app.config["MAIL_USERNAME"],
											recipients=["apatel@adelphi.edu"], # replace with your email for testing
											body="Testing!!!")
				mail.send(msg)