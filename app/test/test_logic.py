import unittest
from app import app

class test_login(unittest.TestCase):
    def setUp(self):
        self.check = app.app.test.client;

    # def test_manager(self):
    #     response = self.check.get('app/manager')
    #     self.assertEqual(response.status.code , 404);
    #
    #
    # def test_for_missing_id(self):
    #     invalid_login = self.check.post('login' , data=dict(first_name='tomer' ,last_name = 'admon' ,  follow_redirects=True))
    #     self.assertEqual(invalid_login.status.code , 400);# 400 is for bad request
    #
    # def test_customer_not_exist_in_db(self):
    #     invalid_customer = self.check.post('login' , data = dict(first_name = 'impostor' , last_name='impostor' , id = '1234' ))
    #     assert u'המצביע אינו מופיע בבסיס הנתונים' in invalid_customer.data

    def test_skipped(self):
        self.fail("shouldn't happen")

if __name__ == '__main__':
    unittest.main() ;





