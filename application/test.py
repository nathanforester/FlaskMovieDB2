from app import app
from application import db
from application import * 
import unittest
import sys
import pytest 
import sqlite3
import requests_mock 
from flask import g, Flask
from flask import url_for
from flask_testing import TestCase

from app import app


class TestInit(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        print("-----------")

    def tearDown(self):
        print("--------")


class FlaskTestCase(TestInit):

    num = 1
    id_num = str(num)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_add(self):
        tester = app.test_client(self)
        response = tester.get('/add', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_update(self):
        id_num = self.id_num 
        tester = app.test_client(self)
        response = tester.get(f'/update/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_add_review(self):
        id_num = self.id_num
        tester = app.test_client(self)
        response = tester.get(f'/add_review/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_reviews(self):
        id_num = self.id_num
        tester = app.test_client(self)
        response = tester.get(f'/reviews/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    
if __name__ == '__main__':
    unittest.main()