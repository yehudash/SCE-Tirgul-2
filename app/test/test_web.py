
# -*- coding: utf-8 -*-

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_web(unittest.TestCase):
    @classmethod
    def setUp(self):
        # create a new Firefox session
        self.browser = webdriver.Firefox(executable_path="/usr/local/sbin/geckodriver")
        # nevigate to the application home page
        self.browser.get('http://localhost:5000/')

    def test_enter_system(self):
        first_name = self.browser.find_element_by_id("first_name")
        last_name = self.browser.find_element_by_id("last_name")
        id = self.browser.find_element_by_id("id")
        first_name.send_keys('tomer')
        last_name.send_keys('admon')
        id.send_keys('123')
        id.send_keys(Keys.RETURN)

        assert u'המצביע אינו מופיע בבסיס הנתונים' not in self.browser.page_source or u'המשתמש הנל הצביע כבר' in self.browser.page_source

    @classmethod
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()


