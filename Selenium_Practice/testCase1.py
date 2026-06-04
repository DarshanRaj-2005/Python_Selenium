from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")

if driver.title == "Automation Exercise":
    print("Home page is loaded successfully")
else:
    print("Home page is not loaded")

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
email.send_keys("messi104@gmail.com")

signup = driver.find_element(By.XPATH,value="//button[contains(text(),'Signup')]")
signup.click()

password = driver.find_element(By.XPATH,value="//input[@id='password']")
password.send_keys("messi10")

firstName = driver.find_element(By.XPATH,value="//input[@id='first_name']")
firstName.send_keys("messi")

lastName = driver.find_element(By.XPATH,value="//input[@id='last_name']")
lastName.send_keys("10")

address = driver.find_element(By.XPATH,value="//input[@id='address1']")
address.send_keys("10,carstreet")

state = driver.find_element(By.XPATH,value="//input[@id='state']")
state.send_keys("tamilnadu")

city = driver.find_element(By.XPATH,value="//input[@id='city']")
city.send_keys("salem")

zipcode = driver.find_element(By.XPATH,value="//input[@id='zipcode']")
zipcode.send_keys("123456")

mn = driver.find_element(By.XPATH,value="//input[@id='mobile_number']")
mn.send_keys("1234567890")

createBut = driver.find_element(By.XPATH,value="//button[contains(text(),'Create Account')]")
createBut.click()

successText = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div/h2/b')
if successText.is_displayed:
    print("Account created")
else:
    print("Account not created")

continueBut = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div/div/a')
continueBut.click()

logmess = driver.find_element(By.XPATH,value='//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
if logmess.text == "Logged in as messi":
    print("Message displayed")
else:
    print("Message not displayed")

delBut = driver.find_element(By.XPATH,value='//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
delBut.click()

delmess = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div/h2/b')
if delmess.isDisplayed():
    print("Account Deleted")
else:
    print("Account not deleted")

conbut = driver.find_element(By.XPATH,value='//*[@id="form"]/div/div/div/div/a')
conbut.click()






