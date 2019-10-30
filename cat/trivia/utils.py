import random


def shuffle(answers):

## Credit: https://radiusofcircle.blogspot.com/2016/03/making-quiz-website-with-python.html
## It can be used to shuffle any dictionary

	selected_keys = []
	i = 0
	while i < len(answers):
		current_selection = random.choice(list(answers))
		if current_selection not in selected_keys:
			selected_keys.append(current_selection)
			i = i+1
	return selected_keys

def to_dict(trivia_questions):
	dicts = {}
	for trivia_question in trivia_questions:
		answers=[]
		answers.append(trivia_question.correct_answer)
		answers.append(trivia_question.incorrect_answer)
		answers.append(trivia_question.incorrect_answer2)
		answers.append(trivia_question.incorrect_answer3)
		dicts[trivia_question.question] = answers
	return dicts

def get_correct_answers(original_questions):
## generate a mini dictionary to be used to
## check correctness and frontend also
	correct_answers={}
	for trivia_question in original_questions:
		correct_answers[trivia_question] = original_questions[trivia_question][0]
	return correct_answers