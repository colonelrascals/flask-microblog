from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = { 'username': 'Patrick'}
    posts = [
        {
            'author': {'username': 'Kenji'},
            'body': 'Beautiful day in Houston!'
        },
        {
            'author': {'username': 'Josh'},
            'body': 'I love D&D!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


