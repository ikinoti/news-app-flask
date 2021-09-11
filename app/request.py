from app.models import headlines
from app import app
import urllib.request, json
from .models import news_source

News_Source = news_source.News_Source

# getting api key
api_key = app.config['NEWS_API_KEY']

# getting sources base url
source_base_url = app.config['NEWS_API_SOURCES_URL']

# getting the news top headline base url
headlines_base_url = app.config['TOP_HEADLINES_API_URL']

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

  