import unittest
from app.models import Top_Headlines




class HeadlinesTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Headlines class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_headlines = Top_Headlines('Mark Orgen', 'Cristiano Ronaldo delivers on Man United return with two goals and a show to delight Old Trafford - ESPN', 'Twelve years after he left Old Trafford, Ronaldo picked up where he left off in a Man United shirt, showing that he remains a difference maker.', "https://www.espn.com/soccer/english-premier-league/story/4472125/cristiano-ronaldo-delivers-on-man-united-return-with-two-goals-and-a-show-to-delight-old-trafford","https://a2.espncdn.com/combiner/i?img=%2Fphoto%2F2021%2F0911%2Fr907512_1296x729_16%2D9.jpg", '2021-09-11T18:50:39Z')

def test_instance(self):
  '''
  Test to check creation of new headline instance
  '''
  self.assertTrue(isinstance(self.new_headlines,Top_Headlines))

