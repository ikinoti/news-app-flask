from flask import render_template,request,redirect,url
from . import main
from ..request import get_news_source, get_top_headlines, news_article_source, get_news_categories


# Views
@main.route('/')
def index():
  '''
  Index page view function that returns the index page and its data
  '''

  newsSource = get_news_source()
  topHeadlines = get_top_headlines
  # title = 'Home - Welcome to the News website'
  return render_template('index.html',title=title, sources = newsSource, topHeadlines=topHeadlines)

@main.route('/article/<id>')
def news_article(id):
  '''
  news view page function that returns the movie details page and its data
  '''
  articles = news_article_source(id)
  return render_template('new.html',articles =articles, id = id)

@main.route('/categories/<category_name>')
def cat(category_name):
  '''
  view function for categories content
  '''
  category = get_news_categories(category_name)
  title = f'{category_name}'
  cat_name = category_name

  return render_template('category.html', title=title, category = category, cat_name = cat_name)