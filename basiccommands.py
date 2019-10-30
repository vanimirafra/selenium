import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GoogleTestCase(unittest.TestCase):

    def test_Google(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("http://www.flipkart.com")
        time.sleep(5)
        print(driver.title)
        driver.get("http://www.amazon.com")
        time.sleep(5)
        print(driver.title)
        driver.back()
        print(driver.title)
        driver.forward()
        driver.close()
