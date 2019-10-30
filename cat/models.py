from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app 
from cat import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(16), unique=True, nullable=False)
	email = db.Column(db.String(64), unique=True, nullable=False)
	password = db.Column(db.String(32), nullable=False)
	results = db.relationship('Result', backref='examinee', lazy=True)

	def get_reset_token(self, expires_sec=900):
		s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

	def __repr__(self):
		return f"User('{self.username}','{self.email}')"

class Result(db.Model):
	__tablename__ = 'result'
	id = db.Column(db.Integer, primary_key=True)
	percentage = db.Column(db.Float, nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Result('{self.percentage}','{self.date}')"

class Trivia(db.Model):
	__tablename__ = 'trivia'
	id = db.Column(db.Integer, primary_key=True)
	question = db.Column(db.String, unique=True, nullable=False)
	correct_answer = db.Column(db.String, nullable=False)
	incorrect_answer = db.Column(db.String, nullable=False)
	incorrect_answer2 = db.Column(db.String, nullable=True)
	incorrect_answer3 = db.Column(db.String, nullable=True)

	def __repr__(self):
		return f"Trivia('{self.question}','{self.correct_answer}', '{self.incorrect_answer}', '{self.incorrect_answer2}', '{self.incorrect_answer3}')"