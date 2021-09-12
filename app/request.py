

import urllib.request, json
from .models import News_Source, Top_Headlines, Article, News_Category

# getting api key
api_key = None

# getting sources base url
source_base_url = None

# getting the news top headline base url
headlines_base_url = None

# getting categories url
categories_base_url = None

# getting articles base url 
articles_base_url = None

def confure_request(app):
  global api_key,source_base_url,headlines_base_url, categories_base_url, articles_base_url
  api_key = app.config['NEWS_API_KEY']
  source_base_url = app.config['NEWS_API_SOURCES_URL']
  headlines_base_url = app.config['TOP_HEADLINES_API_URL']
  categories_base_url = app.config['CATEGORIES_API_URL']
  articles_base_url = app.config['ARTICLES_API_URL']

def get_news_source():
  '''
  Function that gets the json response to our url request
  '''
  get_news_source_url = source_base_url.format(api_key)
  with urllib.request.urlopen(get_news_source_url) as url:
    get_news_source_data = url.read()
    get_news_source_response = json.loads(get_news_source_data)

    news_source_results = None

    if get_news_source_response['sources']:
      news_source_list = get_news_source_response['sources']
      news_source_results = process_sources(news_source_list)

  return news_source_results

def process_sources(source_list):
  '''
  function that process the news articles and transform them to a list of objects
  '''
  news_source_result = []
  for news_source_item in source_list:
    id = news_source_item.get('id')
    name = news_source_item.get('name')
    description = news_source_item.get('description')
    url = news_source_item.get('url')

    if id:
      news_source_object = News_Source(id, name, description,url)
      news_source_result.append(news_source_object)
  return news_source_result

def news_article_source(id):
  article_source_url = 

def get_top_headlines():
  '''
  function that gets the response to the category json
  '''

  get_headlines_url = headlines_base_url.formart(api_key)
  with urllib.request.urlopen(get_headlines_url) as url:
    get_headlines_data = url.read()
    get_headlines_response = json.loads(get_headlines_data)

    get_headlines_results = None

    if get_headlines_response['articles']:
      get_headlines_list = get_headlines_response['articles']
      get_headlines_results = process_articles_results(get_headlines_list)

  return get_headlines_results

def process_articles_results(news):
  '''
  function to process json files of articles from the api key
  '''
  article_source_results = []
  for article in news:
    author = article.get('author')
    title = article.get('title')
    description = article.get('description')
    url = article.get('url')
    image = article.get('urlToImage')
    publishedDate = article.get('publishedAt')

    if image:
      article_objects = Article(author, title, description, url, image, publishedDate)