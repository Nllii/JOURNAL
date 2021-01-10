# newrow.py
import time
from selenium import webdriver
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('')  # Optional argument, if not specified will search path.
driver.get('');
time.sleep(9) # Let the user actually see something!


full_name = driver.find_element_by_id('txtFullName').click()
full_name = driver.find_element_by_id('txtFullName').send_keys("")
time.sleep(1)
email = driver.find_element_by_id('txtNewEmail').click()
email = driver.find_element_by_id('txtNewEmail').send_keys("")
time.sleep(2)
email = driver.find_element_by_id('txtNewEmail').send_keys(Keys.ENTER)

