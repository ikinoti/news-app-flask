from app.news_test import News
from app import app
import urllib.request, json
from .models import news

News = news.News

# getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news top headline base url
base_url = app.config['NEWS_API_TOP_HEADLINES_URL']

def get_top_headlines(source):
  '''
  Function that gets the json response to our url request
  '''
  get_top_headlines_url = base_url.format(source, api_key)
  with urllib.request.urlopen(get_top_headlines_url) as url:
    get_top_news_data = url.read()
    get_top_news_response = json.loads(get_top_news_data)

    top_news_results = None

    if get_top_news_response['articles']:
      top_news_list = get_top_news_response['articles']
      top_news_results = process_results(top_news_results)

  return top_news_results