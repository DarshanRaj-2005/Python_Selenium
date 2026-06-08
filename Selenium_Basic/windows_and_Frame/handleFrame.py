from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

driver = wb.Chrome()
driver.get("https://letcode.in/frame")
driver.maximize_window()
wait = WebDriverWait(driver,15)

frame = driver.switch_to.frame("firstFr")
name = driver.find_element(By.NAME,"fname")
name.send_keys("hello")
print("Switched to frame")
