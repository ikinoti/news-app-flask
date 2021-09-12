from instance.config import NEWS_API_KEY
import os

class Config:
  '''
  general configuration parent class
  '''
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
  TOP_HEADLINES_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
  ARTICLES_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  CATEGORIES_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

class ProdConfig(Config):
  '''
  subclass that contain configuration  of production stage and inherit from parent class
  '''
  pass

class DevConfig(Config):
  '''
  subclass that contain configuration  of development stage and inherit from parent class
  '''
  DEBUG = True

config_options = {
  'development' :DevConfig,
  'production' :ProdConfig
}