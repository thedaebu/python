from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd6753ab27f50e1f2c49228a7aebb4fc7'

posts = [
    {
        'author': 'thedaebu',
        'title': 'thedaepost',
        'content': 'I am the Dae Bu'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=posts)

@app.route('/about')
def about():
    return '<p>I am the Dae Bu</p>'

# add methods argument to allow certain request actions
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)