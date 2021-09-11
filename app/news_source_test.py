import unittest
from models import news_source

News_Source = news_source.News_Source

class NewsSourceTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the News source class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.news_source = News_Source('espn', 'ESPN', 'SPN has up-to-the-minute sports news coverage, scores, highlights and commentary for NFL, MLB, NBA, College Football, NCAA Basketball and more.', 'http://espn.go.com',)

  def test_instance(self):
    self.assertTrue(isinstance(self.news_source, News_Source))

if __name__ == "__main__":
  unittest.main()