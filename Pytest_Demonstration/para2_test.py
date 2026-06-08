from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.mark.parametrize("items",['firefox','chrome'])
@pytest.mark.parametrize("url",['https://www.flipkart.com','https://www.amazon.com'])
@pytest.mark.test1
def test_sample(items,url):
    if items == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = wb.Chrome(options=chrome_options)
        
    elif items == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = wb.Firefox(options=firefox_options)
    
    driver.get(url)
    driver.maximize_window()
    
    print(driver.title)
    time.sleep(5)
    driver.quit()
    
