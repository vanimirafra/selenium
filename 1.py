import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Login(unittest.TestCase):

    def test(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.facebook.com/")

    '''def test_login(self):

        driver.find_element_by_name('email').send_keys('jyothisaddula@gmail.com')
        driver.find_element_by_name('pass').send_keys('12333')
        driver.find_element_by_id('u_0_b').click()'''

    def test_login(self):
        driver.find_element_by_id('u_0_m').send_keys('khuii')
        driver.find_element_by_id('u_0_o').send_keys('la')
        driver.find_element_by_id('u_0_r').send_keys('admin@gmail.com')
        driver.find_element_by_id('u_0_u').send_keys('admin@gmail.com')
        driver.find_element_by_id('u_0_y').send_keys('ad1234@min')
        driver.find_element_by_id('day').send_keys('14')
        driver.find_element_by_id('month').send_keys('oct')
        driver.find_element_by_id('year').send_keys('1999')
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/form/div[1]/div[7]/span/span[2]/label').click()
        driver.find_element_by_id('u_0_15').click()










if __name__ == '__main__':
    unittest.main()


