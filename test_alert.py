# -*- coding utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AlertTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("file:/home/tester/Documents/ula/strona2.html")

    def test_simple_alert(self):
        driver = self.driver
        driver.find_element(By.ID, 'zwykly').click()
        moj_alert=driver.switch_to_alert()
        time.sleep(2)
        moj_alert.accept()


    def test_prompt(self):
        driver=self.driver
        driver.find_element(By.ID, 'prompt').click()
        prom = driver.switch_to_alert()
        prom.send_keys('Radoslaw Patlewicz')
        time.sleep(3)
        prom.accept()
        print(driver.find_element_by_id("tinder").text)
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
