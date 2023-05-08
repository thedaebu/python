from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import current_user

main = Blueprint('main', __name__)

# use @main.route to signify routes
@main.route('/')
@main.route('/home')
def home():
    # import render_template
    # first argument is template file
    # subsequent arguments are keys that could be used in the html template and extended templates
    if request.path == '/':
        return redirect(url_for('main.home'))
    posts = []
    if current_user.is_authenticated:
        posts = current_user.posts
    return render_template('home.html', title='Home', posts=posts)