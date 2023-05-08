from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_practice_app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# establishes redirect route for routes that have login_required decorator and when not logged in
login_manager.login_view = 'users.login'
# establishes message for login_view redirect
login_manager.login_message_category = 'info'
# e-mail notification configuration
mail = Mail()

def create_app(config_class=Config):
    # configure flask app
    app = Flask(__name__)
    # configure database for flask app
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # these need to be imported after app variable initialization
    from flask_practice_app.main.routes import main
    from flask_practice_app.users.routes import users
    from flask_practice_app.posts.routes import posts
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    return app

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