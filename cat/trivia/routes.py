from flask import render_template, request, Blueprint
from flask_login import current_user, login_required
from cat import db
from cat.models import Trivia, Result
from cat.trivia.utils import shuffle, to_dict, get_correct_answers
from sqlalchemy import func
import copy, random

triviaa = Blueprint('triviaa', __name__)


@triviaa.route("/take_trivia")
@login_required
def take_trivia():
	trivia_questions = Trivia.query.order_by(func.random()).all() # randomly retrieve trivia questions from db
	# copy_questions = copy.deepcopy(trivia_questions) # make a copy of original data
	
	global original_questions, copy_questions
	
	original_questions = to_dict(trivia_questions) # convert the data to dict
	copy_questions = copy.deepcopy(original_questions)
	for i in copy_questions.keys():
		random.shuffle(copy_questions[i]) # shuffle the choices
	return render_template('take_trivia.html', title='Play', trivia_questions=copy_questions)

@triviaa.route("/trivia_answers", methods=['POST'])
def trivia_answers():
	accuracy = 0
	answered_answers = {}
	correct_answers = get_correct_answers(original_questions) #collect correct answers
	for q in original_questions.keys():
		answered = request.form[q]
		answered_answers[q] = answered
		if original_questions[q][0] == answered:
			accuracy = accuracy+1

	percent = accuracy/10 # calc accuracy rate and insert into db
	result = Result(percentage=percent, examinee=current_user)
	db.session.add(result)
	db.session.commit()

	print(correct_answers, '\n')
	return render_template('trivia_answers.html', accuracy=accuracy, original=copy_questions, correct=correct_answers, answered=answered_answers)