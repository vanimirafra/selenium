import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class GoogleTestCase(unittest.TestCase):

    def test_Google(self):
        global driver
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("http://127.0.0.1:8000/configurations")







       




if __name__ == "__main__":
    unittest.main()































































