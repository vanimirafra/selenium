'''from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()
import re
l = 'a','u','i',7,3

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]


print(l)


l_in = ["on@3", "two#", "thre%e"]
l_out = []
#l_out = [''.join(e for e in string if e.isalnum()) for string in l_in]
#print(l_out)

for string in l_in:
    for e in string:
        if e.isalnum():
            r=e.split(',')
            l_out.append(','.join(r))





print(l_out)'''


'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.python.org")
try:
   element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
)
finally:
   driver.quit()'''
if():
   print('hii')
else:
   print('hello')


