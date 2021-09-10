from flask import render_template
from app import app

# Views
@app.route('/')
def index():
  '''
  Index page view function that returns the index page and its data
  '''
  message = 'hello world'
  return render_template('index.html',message = message)

@app.route('new/<new_id>')
def new(new_id):
  '''
  news view page function that returns the movie details page and its data
  '''
  return render_template('new.html', id = new_id)