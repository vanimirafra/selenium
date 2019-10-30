import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login(unittest.TestCase):
    def test(self):
        global driver
        driver = webdriver.Firefox('/home/mirafra/geckodriver-v0.24.0-linux64')
        driver.get("https://www.google.com")
        driver.get("https://www.github.com")



    def test_login(self):
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        driver.find_element_by_id('login_field').send_keys('vanimirafra')
        driver.find_element_by_name('password').send_keys('vani@@@123')
        driver.find_element_by_name('commit').click()
        time.sleep(5)
        driver.quit()









if __name__ == '__main__':
    unittest.main()



