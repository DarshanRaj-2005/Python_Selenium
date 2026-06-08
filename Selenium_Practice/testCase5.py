from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")  
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless=new")           
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = wb.Chrome(options=chrome_options)
driver.get("http://automationexercise.com")
wait = WebDriverWait(driver, 30)

signUpBtn = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Signup / Login')]")))
assert "Signup / Login" in signUpBtn.text, "Home page not successfully opened"
signUpBtn.click()

text = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='signup-form']/h2")))
assert text.text == "New User Signup!", "Sign up page not loaded"

name = driver.find_element(By.XPATH, value="//input[@data-qa='signup-name']")
name.send_keys("messi")

email = driver.find_element(By.XPATH, value="//input[@data-qa='signup-email']")
email.send_keys("messi10@gmail.com")

signup = driver.find_element(By.XPATH, value="//button[@data-qa='signup-button']")
signup.click()

errortext = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Email Address already exist!']")))
assert errortext.text == "Email Address already exist!", "Message is not displayed"

print("Test Case Passed")
driver.quit()