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

contactBtn = driver.find_element(By.XPATH,"//div[@class='col-sm-8']/div/ul/child::li[8]")
contactBtn.click()

contacttext = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-8']/div/child::h2")))
assert contacttext.text == "GET IN TOUCH","Contact us page not loaded"

name = driver.find_element(By.CSS_SELECTOR,"input[name = 'name']")
name.send_keys("Messi")

email = driver.find_element(By.CSS_SELECTOR,"input[name = 'email']")
email.send_keys("messi10@gmail.com")

textarea = driver.find_element(By.CSS_SELECTOR,"textarea[id='message']")
textarea.send_keys("This is testing practice")

submitBtn = driver.find_element(By.CSS_SELECTOR,"input[name='submit']")
driver.execute_script("arguments[0].click();",submitBtn)

wait.until(expected_conditions.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

successtext = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='contact-page']/div[2]/div[1]/div/div[2]")))
assert successtext.is_displayed(),"Success Message not displayed"

home = driver.find_element(By.XPATH,"//div[@class='col-sm-8']/div/ul/child::li[1]")
home.click()
print("Test Passed")




