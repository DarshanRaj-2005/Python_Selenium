from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://automationexercise.com")
wait = WebDriverWait(driver, 15)

#To check Home page

if driver.title == "Automation Exercise":
    print("Home page is loaded successfully")
else:
    print("Home page is not loaded")


#To signup using name and email. 
signupBut = driver.find_element(By.XPATH,value='//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
signupBut.click()

signupText = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div[3]/div/h2')
if signupText.is_displayed():
    print("new signup Text is visible")
else:
    print("new signupText is not visible")

name = driver.find_element(By.XPATH,value="//input[@name='name']")
name.send_keys("messi")

email = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div[3]/div/form/input[3]')
email.send_keys("messi9910@gmail.com")

signup = driver.find_element(By.XPATH,value="//button[contains(text(),'Signup')]")
signup.click()


#Filling user details for signup the user. Here Used both xpath and css Selectors and used explicit wait for password
password = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("messi10")

firstname = driver.find_element(By.CSS_SELECTOR,"#first_name")
firstname.send_keys("messi")

lastName = driver.find_element(By.XPATH,value="//input[@id='last_name']")
lastName.send_keys("10")

address = driver.find_element(By.CSS_SELECTOR,"#address1")
address.send_keys("10,car street")

state = driver.find_element(By.XPATH,value="//input[@id='state']")
state.send_keys("tamilnadu")

city = driver.find_element(By.XPATH,value="//input[@id='city']")
city.send_keys("salem")

zipcode = driver.find_element(By.CSS_SELECTOR,"#zipcode")
zipcode.send_keys("123456")

mn = driver.find_element(By.XPATH,value="//input[@id='mobile_number']")
mn.send_keys("1234567890")

createBut = driver.find_element(By.XPATH,value="//button[contains(text(),'Create Account')]")
createBut.click()

successText = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='form']/div/div/div/h2/b")))
if successText.is_displayed:
    print("Account created")
    driver.save_screenshot("Screenshots/TestCase1_AccountCreated.png")
else:
    print("Account not created")

continueBut = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div/div/a')
continueBut.click()

logmess = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-8']/div/ul/child::li[10]/a")))
if logmess.text == "Logged in as messi":
    print("Message displayed")
    driver.save_screenshot("Screenshots/TestCase1_MessageDisplayed.png")
else:
    print("Message not displayed")

delBut = driver.find_element(By.XPATH,value='//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
driver.execute_script("arguments[0].click();",delBut)

delmess = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='form']/div/div/div/h2/b")))
if delmess.is_displayed:
    print("Account Deleted")
    driver.save_screenshot("Screenshots/TestCase1_AccountDeleted.png")
else:
    print("Account not deleted")

conbut = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div/div/a')
conbut.click()

driver.close()





