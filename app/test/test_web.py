
# -*- coding: utf-8 -*-

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask
from flask_testing import LiveServerTestCase
from flask_config import basedir

from app.models import User, Party
from app import app , db

basedir = os.path.abspath(os.path.dirname(__file__))
class test_web(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'test.db')
    TESTING = True
    @classmethod
    def create_app(self):
        self.app = app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        # Default port is 5000
        self.app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        self.app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.insert_data_to_db()
        return self.app

    @classmethod
    def setUp(self):
        # self.app = app
        # create a new Firefox session
        self.browser = webdriver.PhantomJS()
        # nevigate to the application home page
        self.driver.get(self.get_server_url())


    def test_enter_system(self):
        first_name = self.browser.find_element_by_id("first_name")
        last_name = self.browser.find_element_by_id("last_name")
        id = self.browser.find_element_by_id("id")
        first_name.send_keys('tomer')
        last_name.send_keys('admon')
        id.send_keys('123')
        id.send_keys(Keys.RETURN)

        assert u'המצביע אינו מופיע בבסיס הנתונים' not in self.browser.page_source or u'המשתמש הנל הצביע כבר' in self.browser.page_source

    def insert_data_to_db(self):
        db.session.commit()

        admon = User('tomer', 'admon', '123')
        tomer = User(u'תומר', u'אדמון', '1234')

        avoda = Party(u'העבודה',
                      'https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg')
        likud = Party(u'הליכוד',
                      'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Likud_Logo.svg/250px-Likud_Logo.svg.png')
        lavan = Party(u'פתק לבן',
                      'https://www.weberthai.com/fileadmin/user_upload/01_training-elements/02.4_others/02.5_color_cards/05_color_mosaic/images/1.jpg')

        db.session.add(avoda)
        db.session.add(likud)
        db.session.add(lavan)
        db.session.add(admon)
        db.session.add(tomer)
        db.session.commit()
        users = User.query.all()



    @classmethod
    def tearDown(self):
        self.browser.quit()



if __name__ == '__main__':
    unittest.main()


