from flask import render_template, request, Blueprint
from cat.models import Result
from sqlalchemy import desc


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index")
def index():
		results = Result.query.order_by(desc(Result.date)).limit(10).all()
		return render_template('index.html', results=results)


@main.route("/about")
def about():
		return render_template('about.html', title='About')