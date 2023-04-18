from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# configure flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd6753ab27f50e1f2c49228a7aebb4fc7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_database.db'
# configure database for flask app
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# establishes redirect route for routes that have login_required decorator and when not logged in
login_manager.login_view = 'login'
# establishes message for login_view redirect
login_manager.login_message_category = 'info'

from flask_practice_app import routes

# has to be used for db commands
# with app.app.context():
    ## creates database file
    # db.create_all()
    ## creates instance of model
    # user1 = User(username="username", email="username@gmail.com", password="password")
    ## adds data to session
    # db.session.add(user1)
    ## commits session data to database
    # db.session.commit()
    # User.query.all()
    # User.query.first()
    # User.query.filter_by(username="username").all()
    ## queries by ID
    # User.query.get(1)
    # User.posts
    ## delete method for db item
    # db.session.delete(User.query.first())
    ## deletes database
    # db.drop_all()