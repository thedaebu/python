from flask import render_template, url_for, flash, redirect, request
from flask_practice_app import app, db, bcrypt
from flask_practice_app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_practice_app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image

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
    if request.path == '/':
        return redirect(url_for('home'))
    return render_template('home.html', title='Home', posts=posts)

# add methods argument to allow certain request actions
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    # import specific form from forms
    form = RegistrationForm()
    # validate_on_submit method runs when form is submitted
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # data attribute signifies value of input field
        flash(f'Account created for {form.username.data}.', 'success')
        # redirect url should be for method name and not for route name
        # put url in string
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Account logged in for {form.email.data}.', 'success')
            # used for redirect directly to specific route page if route page was accessed without current user
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Log in unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static', picture_fn)
    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_fn

# add login_required decorator for a redirect that is established in __init__ file
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    # 'static' is folder name
    # apparently, if method is not found in current file, it looks in directory
    image_file = url_for('static', filename=current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)
