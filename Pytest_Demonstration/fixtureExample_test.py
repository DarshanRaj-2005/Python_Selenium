from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture()
def test_setupAndteardown():
    global driver
    global wait

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    wait = WebDriverWait(driver,30)

    yield

    driver.quit()

@pytest.mark.parametrize("input,expected",[('macbook',"MacBook")])
def test_searchProduct(test_setupAndteardown,input,expected):
    searchBox = driver.find_element(By.XPATH,"//input[@name='search']")
    searchBox.send_keys(input)
    btn = driver.find_element(By.XPATH,"//*[@id='search']/span/button").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")))

    mac = driver.find_element(By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")
    
    assert mac.text == expected,"MacBook is not searched"
    print("passed")

def test_invalidProduct(test_setupAndteardown):
    driver.find_element(By.XPATH,'//*[@id="search"]/input').send_keys("hdfg")
    driver.find_element(By.XPATH,'//*[@id="search"]/span/button').click()
    assert driver.find_element(By.XPATH,'//*[@id="content"]/p[2]').is_displayed()
    print("Product not found")


