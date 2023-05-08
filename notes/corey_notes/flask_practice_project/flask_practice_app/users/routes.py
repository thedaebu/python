from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_practice_app import bcrypt, db
from flask_practice_app.models import User
from flask_practice_app.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestPasswordForm, RequestResetForm
from flask_practice_app.users.utils import save_picture, send_reset_email
from flask_login import current_user, login_user, logout_user, login_required

users = Blueprint('users', __name__)

# add methods argument to allow certain request actions
@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

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
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Account logged in for {form.email.data}.', 'success')
            # used for redirect directly to specific route page if route page was accessed without current user
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Log in unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

# add login_required decorator for a redirect that is established in __init__ file
@users.route('/account', methods=['GET', 'POST'])
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
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    # 'static' is folder name
    # apparently, if method is not found in current file, it looks in directory
    image_file = url_for('static', filename=current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('users.login'))

    return render_template('reset_request.html', title='Reset Password', form=form)

@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an expired token.', 'warning')
        return redirect(url_for('reset_request'))
    
    form = RequestPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been reset', 'success')
        return redirect(url_for('users.login'))
    
    return render_template('reset_token.html', title='Reset Password', form=form)