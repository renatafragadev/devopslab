# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_root_request(self):

        self.result = self.app.get('/')
       
        self.assertEqual(self.result.status_code, 200)
        self.assertEqual(self.result.data.decode('utf-8'), "Laboratório Pipeline DevOps")

    def test_randon_request(self):
        self.result = self.app.get('/random')

        result = int(self.result.data.decode('utf-8'))
        self.assertEqual(self.result.status_code, 200)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 20)





