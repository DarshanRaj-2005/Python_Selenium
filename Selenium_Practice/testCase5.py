from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = wb.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
wait = WebDriverWait(driver,30)

signUpBtn = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-8']/div/ul/child::li[4]")))
assert signUpBtn.text == "Signup / Login", "Home page not successfully opened"
signUpBtn.click()

text = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='signup-form']/child::h2")))
assert text.text == "New User Signup!","Sign up page not loaded"

name = driver.find_element(By.XPATH,value="//input[@name='name']")
name.send_keys("messi")

email = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div[3]/div/form/input[3]')
email.send_keys("messi10@gmail.com")

signup = driver.find_element(By.XPATH,value="//button[contains(text(),'Signup')]")
signup.click()

errortext = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/p")))
assert errortext.text == "Email Address already exist!","Message is not displayed"
print("Test Case Passed")



