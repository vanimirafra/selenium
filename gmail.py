import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login(unittest.TestCase):


    def test(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/gmail")


    '''def test_login(self):

        driver.find_element_by_id('identifierId').send_keys('jyothisaddula@gmail.com')
        driver.find_element_by_id('identifierNext').click()

        time.sleep(2)
        driver.find_element_by_name('password').send_keys('India@143')
        driver.find_element_by_id('passwordNext').click()
        time.sleep(5)'''



    def test_create(self):

        driver.find_element_by_class_name('j07h3c').click()
        driver.find_element_by_id('firstName').send_keys('vaani')




unittest.main()



