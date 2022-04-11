#!/bin/python3

# This software is intended to get all the university coop documents that are located in http://ccisimsiu.net/ccisstaf/
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username=sys.argv[1]
password=sys.argv[2]

driverPath = "/home/x/apps/chromedriver"
driver = webdriver.Chrome(driverPath)
 
driver.get("http://ccisimsiu.net/ccisstaf/")

usernameField = driver.find_element_by_name("usrs")
usernameField.send_keys(username)

passwordField = driver.find_element_by_name("nid")
passwordField.send_keys(password)
passwordField.send_keys(Keys.RETURN)


driver.quit()
