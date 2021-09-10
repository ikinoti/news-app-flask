class Config:
  '''
  general configuration parent class
  '''
  NEWS_API_bASE_URL = 'https://newsapi.org/v2/{}/sources?apiKey={}'

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