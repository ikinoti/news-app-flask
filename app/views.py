from flask import render_template
from app import app
from .request import get_news_source

# Views
@app.route('/')
def index():
  '''
  Index page view function that returns the index page and its data
  '''

  newsSource = get_news_source()
  # top_headlines = get_top_headlines()
  title = 'Home - Welcome to the News website'
  return render_template('index.html',title=title, source = newsSource)

@app.route('/new/<int:new_id>')
def new(new_id):
  '''
  news view page function that returns the movie details page and its data
  '''
  title = f'You are viewing {{new_id}}'
  return render_template('new.html', id = new_id)