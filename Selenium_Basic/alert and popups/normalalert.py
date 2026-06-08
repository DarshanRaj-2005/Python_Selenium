from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

driver = wb.Chrome()
driver.get("https://www.leafground.com/alert.xhtml")
driver.maximize_window()

wait = WebDriverWait(driver,15)

alertBox = driver.find_element(By.XPATH,"//*[@id='j_idt88:j_idt91']")
alertBox.click()

wait.until(expected_conditions.alert_is_present()).accept()
print("Alert is accpeted")