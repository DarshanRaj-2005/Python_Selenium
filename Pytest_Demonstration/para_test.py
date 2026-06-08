from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.parametrize("items",[("jaggu"),("jagadeep")])

def test_sample(items):
    driver = wb.Chrome()
    driver.get("https:google.co.in")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID,"APjFqb").send_keys(items)
    time.sleep(5)
    driver.quit()