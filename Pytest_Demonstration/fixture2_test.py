import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("input,expected",[('macbook',"MacBook")])
def test_searchProduct(setUp,input,expected):
    driver,wait = setUp
    searchBox = driver.find_element(By.XPATH,"//input[@name='search']")
    searchBox.send_keys(input)
    btn = driver.find_element(By.XPATH,"//*[@id='search']/span/button").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")))

    mac = driver.find_element(By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")
    
    assert mac.text == expected,"MacBook is not searched"