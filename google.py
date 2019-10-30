import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Login(unittest.TestCase):


    def test(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://seleniumbymahesh.com")

    def test_login(self):
        driver.find_element(By.LINK_TEXT, 'HMS').click()
        driver.find_element(By.NAME, 'username').send_keys('admin')
        driver.find_element(By.NAME, 'password').send_keys('admin')
        driver.find_element(By.NAME, 'submit').click()
        time.sleep(5)

    def test_logout(self):
         driver.find_element(By.LINK_TEXT, 'Logout').click()
         driver.quit()





if __name__ == '__main__':
    unittest.main()


