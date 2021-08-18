from flask import (Flask, render_template, redirect)
from config import Config

from app.sample_form import SampleForm
# app is directory; sample_form is filename

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def dude():
    # return f'<p>{app.config['SECRET_KEY']}</p><p>{str(__name__)}.py</p>'
    return render_template('index.html', sitename='TheDaeBu')


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = SampleForm()
    if form.validate_on_submit():
        return redirect('/')
        # when form submit is good
    return render_template('form.html', form=form)


@app.route('/about')
def about():
    return '<p>This is the about page</p>'


@app.route('/about/<id>')
def wild_card(id):
    return f'<p>welcome to page {id}</p>'
