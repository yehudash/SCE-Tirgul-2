import unittest
from app import app

class test_login(unittest.TestCase):
    def setUp(self):
        self.check = app.app.test.client;

    def test_manager(self):
        response = self.check.get('app/manager')
        self.assertEqual(response.status.code , 404);


    def test_for_exist_id(self):
        invalid_login = self.check.post('login' , data=dict(first_name='tomer' ,last_name = 'admon' ,  follow_redirects=True))
        self.assertEqual(response.status.code , 400);

if __name__ == '__main__':
    unittest.main() ;
