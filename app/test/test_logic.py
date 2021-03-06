
# -*- coding: utf-8 -*-

import os
import unittest
from flask import Flask
from app.models import User, Party
from app import app , db


class test_login(unittest.TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def setUp(self):
        #db.init_app(app)
        self.check = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()
            self.insert_data_to_db()
        #return app

    def insert_data_to_db(self):
        db.session.commit()
        admon = User('tomer', 'admon', '123')
        avoda = Party(u'העבודה',
                      'https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg')
        db.session.add(avoda)
        db.session.add(admon)
        db.session.commit()

    def test_manager(self):
        response = self.check.get('app/manager')
        self.assertEqual(response.status_code, 404)

    def test_for_missing_id(self):
        # this test ensures that you cannot get an access without id number
        invalid_login = self.check.post('login', data={'first_name': 'tomer', 'last_name': 'admon'},
                                        follow_redirects=True)
        self.assertEqual(invalid_login.status_code, 400);  # 400 is for bad request

    def test_invalid_user(self):
        invalid_user = self.check.post('login', data={'first_name': 'sali', 'last_name': 'impostor', 'id': '2407'},
                                       follow_redirects=True)
        return u'המצביע אינו מופיע בבסיס הנתונים' in invalid_user.data.decode('utf-8')

    def tearDown(self):
        del self.check
        with app.app_context():
            db.session.remove()
            db.drop_all()



if __name__ == '__main__':
    unittest.main()

