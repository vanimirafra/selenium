import unittest
from selenium import webdriver
driver = webdriver.Firefox('/home/mirafra/geckodriver-v0.24.0-linux64')
driver.get("https://www.amazon.com")
cookies=driver.get_cookies()
print(len(cookies))
cookie={'name':'Mycookie', 'value':'122'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)


