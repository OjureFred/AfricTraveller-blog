import unittest
import datetime
from app.models import Blog

class BlogTest(unittest.TestCase):
    '''
    Test class to test the behaviuor of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_blog = Blog(122, 'Travel to Congo Brazzaville', 'All the stories of what happened in the Congo', datetime.datetime(2020, 5, 7), 'A piture')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_blog, Blog))