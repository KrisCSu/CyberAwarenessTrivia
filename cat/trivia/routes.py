from flask import render_template, request, Blueprint
from flask_login import current_user, login_required
from cat import db
from cat.models import Trivia, Result
from sqlalchemy import func

triviaa = Blueprint('triviaa', __name__)


@triviaa.route("/take_trivia")
@login_required
def take_trivia():
	global trivia_questions
	trivia_questions = Trivia.query.order_by(func.random()).all()
	return render_template('take_trivia.html', trivia_questions=trivia_questions)

@triviaa.route("/trivia_answers", methods=['POST'])
@login_required
def trivia_answers():
	correct = 0
	answered_answers = []
	for q in trivia_questions:
		answered = request.form[str(q.id)]
		answered_answers.append(answered)
		if q.correct_answer == answered:
			correct = correct+1
	percent = correct/10
	result = Result(percentage=percent, examinee=current_user)
	db.session.add(result)
	db.session.commit()
	return render_template('trivia_answers.html', correct=correct, original=trivia_questions, answered_answers=answered_answers)