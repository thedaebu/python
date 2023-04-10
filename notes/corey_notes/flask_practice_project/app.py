from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return '<p>I am the Dae Bu</p>'

if __name__ == '__main__':
    app.run(debug=True)