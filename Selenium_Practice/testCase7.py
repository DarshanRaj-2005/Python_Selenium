from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert

driver = wb.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
wait = WebDriverWait(driver,30)

signUpBtn = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-8']/div/ul/child::li[4]")))
assert signUpBtn.text == "Signup / Login", "Home page not successfully opened"

testcase = driver.find_element(By.XPATH,"//div[@class='col-sm-8']/div/ul/child::li[5]").click()

text = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='form']/div/div[1]/div/h2/b")))
assert text.text == "TEST CASES","test case page not loaded"

print("Test Passed")
