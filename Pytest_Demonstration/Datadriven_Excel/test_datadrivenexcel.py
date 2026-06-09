import pytest
from utilitie import excelreader
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utilitie import logCreater

@pytest.mark.parametrize("username,password",excelreader.getdata("C:\\Users\\dhars\\Documents\\Python_Selenium\\Pytest_Demonstration\\Datadriven_Excel\\Excelfiles\\logindata.xlsx","Sheet1"))
class Testlogin:
    logger = logCreater.log_generator()
    def test_login(self,username,password):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver,30)
        driver.get("https://demoblaze.com/")
        driver.maximize_window()

        login = driver.find_element(By.XPATH,"//*[@id='login2']")
        self.logger.info("Login Button is clicked")
        login.click()

        user = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='loginusername']")))
        self.logger.info("entered username")
        user.send_keys(username)

        passwor = driver.find_element(By.XPATH,"//*[@id='loginpassword']")
        self.logger.info("Entered password")
        passwor.send_keys(password)

        submit = driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
        submit.click()

        weltext = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='nameofuser']")))
        assert weltext.is_displayed()
        self.logger.info("Asserted login")
        print("Test Passed")
