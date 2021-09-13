from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_source, get_top_headlines, news_article_source, get_news_categories, search_article


# Views
@main.route('/')
def index():
  '''
  Index page view function that returns the index page and its data
  '''

  newsSource = get_news_source()
  topHeadlines = get_top_headlines()
  # title = 'Home - Welcome to the News website'
  return render_template('index.html', sources = newsSource, topHeadlines=topHeadlines)

@main.route('/article/<id>')
def news_article(id):
  '''
  news view page function that returns the movie details page and its data
  '''
  articles = news_article_source(id)
  return render_template('articles.html',articles =articles, id = id)

@main.route('/categories/<category_name>')
def cat(category_name):
  '''
  view function for categories content
  '''
  category = get_news_categories(category_name)
  title = f'{category_name}'
  cat_name = category_name

  return render_template('category.html', title=title, category = category, cat_name = cat_name)

@main.route('/search/<article_name>')
def search(article_name):
  '''
  View function to display search results
  '''
  article_name_list = article_name.split(" ")
  article_name_format = "+".join(article_name_list)
  searched_articles = search_article(article_name_format)
  title = f'search results for {article_name}'
  return render_template('search.html', articles = searched_articles)