class News_Source:
  '''
  news source class to define source objects
  '''

  def __init__(self, id, name, description, url):
    self.id = id
    self.name = name
    self.description = description
    self.url = url

class Top_Headlines:
  '''
  top headline class to instantiates headlines objects of the news sources
  '''

  def __init__(self, author, title, description, url, image, publishedDate):
      self.author = author
      self.title = title
      self.description = description
      self.url = url
      self.image = image
      self.publishedDate = publishedDate

class Article:
  '''
  news article objects class of the news sources
  '''
  def __init__(self, author, title, description, url, image, publishedDate):
      self.author = author
      self.title = title
      self.description = description
      self.url = url
      self.image = image
      self.publishedDate = publishedDate

class News_Category:
  '''
  Class to instantiate object of news category
  '''

  def __init__(self, author, title, description, url, image, publishedDate):
      self.author = author
      self.title = title
      self.description = description
      self.url = url
      self.image = image
      self.publishedDate = publishedDate
