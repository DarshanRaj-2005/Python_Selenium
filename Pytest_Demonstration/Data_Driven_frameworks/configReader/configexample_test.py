import read_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def test_validLogin():
        driver = webdriver.Chrome()
        driver.get(read_config.getData("info","url"))
        driver.maximize_window()
        wait = WebDriverWait(driver,30)
        account = driver.find_element(By.XPATH,"//*[@id='top-links']/ul/li[2]/a")
        account.click()

        login = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[2]/a")))
        login.click()

        username = driver.find_element(By.XPATH,"//*[@id='input-email']")
        username.send_keys(read_config.getData("credentials","username"))

        password = driver.find_element(By.XPATH,"//*[@id='input-password']")
        password.send_keys(read_config.getData("credentials","password"))

        submit = driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input")
        submit.click()




