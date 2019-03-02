# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pages.home_page import HomePage

class WizzairRegistration(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()

    def test_correct_registration(self):
        home_page = HomePage(self.driver)
        home_page.click


if __name__ == '__main__':
    unittest.main()
