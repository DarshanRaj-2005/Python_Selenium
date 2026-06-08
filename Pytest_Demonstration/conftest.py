from urllib import request
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    wait = WebDriverWait(driver,30)
    request.cls.driver = driver
    yield driver,wait
    driver.quit()