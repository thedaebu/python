from flask import (Flask, render_template)
from config import Config
from app.sample_form import SampleForm

app = Flask(__name__)
app.config.from_object(Config)

# @app.before_request
# def before_request_function():
#     print("before_request is running")

# @app.after_request
# def after_request_function():
#     print("after_request is running")

@app.route("/")
def dude():
    # return f'<p>{app.config["SECRET_KEY"]}</p><p>{str(__name__)}.py</p>'
    return render_template('index.html', sitename = "TheDaeBu")

@app.route("/form")
def form():
    form = SampleForm()
    return render_template('form.html', form=form)

@app.route("/about")
def about():
    return '<p>This is the about page</p>'

@app.route("/about/<id>")
def wild_card(id):
    return f'<p>welcome to page {id}</p>'