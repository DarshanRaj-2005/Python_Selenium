from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest_check as check
from pytest import assume
def setup_function(function):
    global driver
    global wait
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver,15)
    driver.get("https://tutorialsninja.com/demo/")


def teardown_function(function):
    driver.quit()

def test_search():
    searchBox = driver.find_element(By.XPATH,"//input[@name='search']")
    searchBox.send_keys("macbook")
    btn = driver.find_element(By.XPATH,"//*[@id='search']/span/button")
    btn.click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")))

    mac = driver.find_element(By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")
    

    #Used Check for soft assertion. it will run the code even it fail
    check.equal(mac.text,"Mac")
    print("Used Check")


    #Used Assume for soft assertions
    assume(mac.text == "Mac")
    print("Used assume")
