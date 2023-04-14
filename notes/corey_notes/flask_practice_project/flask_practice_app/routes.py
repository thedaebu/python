from flask import render_template, url_for, flash, redirect
from flask_practice_app import app
from flask_practice_app.forms import RegistrationForm, LoginForm
from flask_practice_app.models import User, Post

posts = [
    {
        'author': 'thedaebu',
        'title': 'thedaepost',
        'content': 'I am the Dae Bu'
    }
]

# use @app.route to signify routes
@app.route('/')
@app.route('/home')
def home():
    # import render_template
    # first argument is template file
    # subsequent arguments are keys that could be used in the html template and extended templates
    return render_template('home.html', title='Home', posts=posts)

# add methods argument to allow certain request actions
@app.route('/register', methods=['GET', 'POST'])
def register():
    # import specific form from forms
    form = RegistrationForm()
    # validate_on_submit method runs when form is submitted
    if form.validate_on_submit():
        # data attribute signifies value of input field
        flash(f'Account created for {form.username.data}.', 'success')
        # redirect url should be for method name and not for route name
        # put url in string
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'thedaebu@gmail.com' and form.password.data == 'smakdown':
            flash(f'Account logged in for {form.email.data}.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Log in unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)
