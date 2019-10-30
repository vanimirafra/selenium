import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login(unittest.TestCase):
    def test(self):
        global driver
        driver = webdriver.Firefox('/home/mirafra/geckodriver-v0.24.0-linux64')
        driver.get("https://www.amazon.com")





unittest.main()