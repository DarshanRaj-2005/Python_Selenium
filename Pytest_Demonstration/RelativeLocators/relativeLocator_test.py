from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

def test_validsearch():

    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    div = driver.find_element(By.ID, "search")
    searchbar = driver.find_element(locate_with(By.TAG_NAME, "input").inside(div))
    searchbar.send_keys("Mac")
    searchBtn = driver.find_element(locate_with(By.TAG_NAME, "button").inside(div))
    searchBtn.click()
    time.sleep(5)