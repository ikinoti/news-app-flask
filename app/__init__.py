from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap

def create_app(config_name):

  
  app = Flask(__name__)

  # creating the app configutation
  app.config.from_object(config_options[config_name])
  
  #  initializing flask extension
  bootstrap.init_app(app)

  

  return app
