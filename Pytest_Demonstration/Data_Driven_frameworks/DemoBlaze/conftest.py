from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import read_config
import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import read_config
import pytest

@pytest.fixture()
def setupLogin(request):
    if read_config.getData("info", "browser") == "chrome":
        driver = webdriver.Chrome()
    driver.get(read_config.getData("info", "url"))
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()
