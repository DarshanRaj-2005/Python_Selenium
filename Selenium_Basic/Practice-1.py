from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window
driver.get("https://www.google.co.in")
title = driver.title

if(title == "Google"):
    print("Page opened successfully")
else:
    print("Page not opened successfully")

textarea = driver.find_element(By.XPATH,value="//textarea[@id='APjFqb']")

if textarea.is_enabled:
    print("The Search Box is enabled")
else:
    print("The Search Box is not enabled")
textarea.send_keys("Hello")
textarea.submit()
time.sleep(5)
driver.close()