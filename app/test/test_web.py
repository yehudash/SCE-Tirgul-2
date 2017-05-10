import unittest
from app import app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_web(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_enter_system(self):
        # self.browser.get('http://localhost/:5000')
        # self.browser.find_element_by_id("first_name").send_keys('tomer')
        # self.browser.find_element_by_id("last_name").send_keys('admon')
        # id = self.browser.find_element_by_id("id")
        # id.send_keys('1234' + Keys.ENTER)
        assert False

if __name__ == '__main__':
    unittest.main()


