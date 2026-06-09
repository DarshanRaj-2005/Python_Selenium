import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setUp")
class TestSearch:
    @pytest.mark.parametrize("input,expected",[('macbook',"MacBook")])
    def test_searchProduct(self,input,expected):
        searchBox = self.driver.find_element(By.XPATH,"//input[@name='search']")
        searchBox.send_keys(input)
        btn = self.driver.find_element(By.XPATH,"//*[@id='search']/span/button")
        btn.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")))

        mac = self.driver.find_element(By.XPATH,"//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a")
    
        assert mac.text == expected,"MacBook is not searched"