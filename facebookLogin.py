#!/usr/bin/env python
# 
"""     
   AutoLogin to Facebook
"""
__program__ = 'AutoLogin-Facebook'
__author__  = 'Alex Ruber'

#Imports
import os
import sys
import re
import argparse
import sched
import time
import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

#Use crontab to automate process daily

#Connect to website and open website 
chromedriver = #'Path to chrome driver'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.facebook.com/")
action = webdriver.ActionChains(driver)

#Take in username and password credentials and set it to a variable
username = raw_input("Please enter your Facebook Username: ")
#print "You entered: ", username
password = getpass.getpass("Please enter your Facebook Password: ")
#print "You entered: ", password

#Autologin logic using Xpath
driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
print("Waiting 3 seconds...")
time.sleep(3)
facebook_links = driver.find_element_by_xpath('//*[@id="loginbutton"]')
facebook_links.click()
print("Succesfully signed in")


# visible_link = next(link for link in wiki_links if link.is_displayed())
# print visible_link
# if visible_link: print True
# else: print False
# visible_link.click()
#print("Successfully logged in")


#Stores PDF to Local 
#def storePDF():


#Set time scheduler to run in background at 3am 








