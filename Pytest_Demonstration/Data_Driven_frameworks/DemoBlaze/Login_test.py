import read_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import pytest

@pytest.mark.usefixtures("setupLogin")
class TestLogin:
    def test_validLogin(self):
        login = self.driver.find_element(By.XPATH,"//*[@id='login2']")
        login.click()

        username = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='loginusername']")))
        username.send_keys(read_config.getData("credentials","username"))

        password = self.driver.find_element(By.XPATH,"//*[@id='loginpassword']")
        password.send_keys(read_config.getData("credentials","password"))

        submit = self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
        submit.click()

        weltext = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='nameofuser']")))
        assert weltext.text == "Welcome DarshanRaj"
        print("Test Passed")





