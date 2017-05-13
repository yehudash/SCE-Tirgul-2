# -*- coding: utf-8 -*-

import sys
import unittest
from flask import Flask
from app import app,db

class test_login(unittest.TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        db.init_app(app)
        with app.app_context():
            db.create_all()
            self.insert_data_to_db()
        return app

    def setUp(self):
        self.check =app.test_client()

    def test_manager(self):
        response = self.check.get('app/manager')
        self.assertEqual(response.status_code, 404);

    def test_for_missing_id(self):
        # this test ensures that you cannot get an access without id number
        invalid_login = self.check.post('login' , data = { 'first_name':'tomer' , 'last_name': 'admon'} ,  follow_redirects=True)
        self.assertEqual(invalid_login.status_code , 400);# 400 is for bad request

    def test_invalid_user(self):
        invalid_user=self.check.post('/login', data = { 'first_name':'sali' , 'last_name': 'impostor', 'id':'2407' , 'voted':'0' })
        return u'המצביע אינו מופיע בבסיס הנתונים' in invalid_user.data.decode("utf-8")

    # def test_customer_not_exist_in_db(self):
    #     invalid_customer = self.check.post('login' , data = dict(first_name = 'impostor' , last_name='impostor' , id = '0' ))
    # #     assert u'המצביע אינו מופיע בבסיס הנתונים' in invalid_customer.data.decode('utf-8')



    def tearDown(self):
        del self.check
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()












