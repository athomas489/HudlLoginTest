
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s=Service("/Users/althomas/chromedriver/chromedriver")

driver=webdriver.Chrome(service=s)

driver.get("https://www.hudl.com/")
assert"Hudl" in driver.title

continue_link = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/a[2]").click()

import os

db_email = os.environ.get('DB_EMAIL')
db_password = os.environ.get('DB_PASSWORD')

Emailinput = driver.find_element(By.ID,'email').send_keys('db_email')

                                 
Passwordinput = driver.find_element(By.ID,'password').send_keys('db_password')


                                 
continue_link = driver.find_element(By.XPATH,'//*[@id="logIn"]').click()
time.sleep(3)

yourprofile = driver.find_element(By.CLASS_NAME,'hui-globaluseritem__email').is_displayed()















