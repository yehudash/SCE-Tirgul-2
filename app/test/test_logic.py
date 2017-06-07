# -*- coding: utf-8 -*-

import sys
import unittest
import os
from flask import Flask
from app import app,db
from app.models import User, Party
from flask_config import basedir
from selenium import webdriver
from flask_testing import LiveServerTestCase

class test_login(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        #app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(app)
        with app.app_context():
            db.drop_all()
            db.create_all()
            self.insert_data_to_db()
        return app


    def insert_data_to_db(self):
        db.session.commit()
        a = User('tomer', 'admon', '123')
        v = Party(u'העבודה','https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg')
        db.session.add(v)
        db.session.add(a)
        db.session.commit()

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        # nevigate to the application home page
        self.browser.get(self.get_server_url())


    # def test_manager(self):
    #     response = self.check.get('app/manager')
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_for_missing_id(self):
    #     # this test ensures that you cannot get an access without id number
    #     invalid_login = self.check.post('login' , data = { 'first_name':'tomer' , 'last_name': 'admon'} ,  follow_redirects=True)
    #     self.assertEqual(invalid_login.status_code , 400);# 400 is for bad request
    #
    # def test_invalid_user(self):
    #     invalid_user=self.check.post('login', data = { 'first_name':'sali' , 'last_name': 'impostor', 'id':'2407' } ,  follow_redirects=True)
    #     self.assertEqual(invalid_user.status_code , 500)


    def tearDown(self):
        self.browser.quit()
        with app.app_context():
            db.drop_all()
            db.session.remove()


if __name__ == '__main__':
    unittest.main()












