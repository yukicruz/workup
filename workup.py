import os
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# os.startfile("CP-FIREFOX")
driver = webdriver.Firefox("CP-FIREFOXWEBDRIVER")
# os.startfile("CP-CHROME")
# driver= webdriver.Chrome("CP-CHROMEWEBDRIVER") #Need to install chromedriver and change this path for this line to work

driver.get('CP-LW')

userid = driver.find_element_by_id("username")
userid.send_keys("CP-USERNAME1")

pw = driver.find_element_by_id("password")
pw.send_keys("CP-PASSWORD1")

# signin = driver.find_element_by_class_name("gwt-Button")
# signin.click()
