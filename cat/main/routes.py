from flask import render_template, request, Blueprint
from cat.models import Result, Trivia
from sqlalchemy import func



main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index")
def index():
    results = Result.query.order_by(Result.percentage).all()
    return render_template('index.html', results=results)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/trivia")
def trivia():
    trivia = Trivia.query.order_by(func.random()).all()
    return render_template('trivia.html', trivia=trivia)