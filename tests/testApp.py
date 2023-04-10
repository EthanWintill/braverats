import unittest
from flask import url_for
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 200)

    

if __name__ == '__main__':
    unittest.main()