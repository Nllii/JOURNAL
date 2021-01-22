# newrow.py
import time
from selenium import webdriver
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#/Users/admin/Desktop/CODING JOURNAL /newrow login/chromedriver
driver = webdriver.Chrome('/Users/admin/Desktop/CODING JOURNAL /newrow_login/chromedriver')
# Optional argument, if not specified will search path.
driver.get('https://smart.newrow.com/room/?xub-327');
time.sleep(9) # Let the user actually see something!


full_name = driver.find_element_by_id('txtFullName').click()
full_name = driver.find_element_by_id('txtFullName').send_keys("Nii")
time.sleep(1)
email = driver.find_element_by_id('txtNewEmail').click()
email = driver.find_element_by_id('txtNewEmail').send_keys("W@student.hccs.edu")
time.sleep(2)
email = driver.find_element_by_id('txtNewEmail').send_keys(Keys.ENTER)




