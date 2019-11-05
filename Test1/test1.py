#!/usr/bin/python
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/home/ebanarp/ArpanTest/chromedriver_linux64/chromedriver")
driver.get("http://newtours.demout.com/")
print(driver.title)
driver.close()
