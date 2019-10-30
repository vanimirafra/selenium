from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
ele=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button')
actions=ActionChains(driver)
actions.double_click(ele).perform()