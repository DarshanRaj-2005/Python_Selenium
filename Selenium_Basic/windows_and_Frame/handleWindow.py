from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

driver = wb.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/window.xhtml")

wait = WebDriverWait(driver,15)

parent = driver.current_window_handle

openBtn = driver.find_element(By.XPATH,"//*[@id='j_idt88:new']");
openBtn.click()

newWindow = driver.window_handles

for window in newWindow:
    if window != parent:
        driver.switch_to.window(window)

element  = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[5]/div[1]/div")))

if element.text == "/ Dashboard":
    print("Switched to new window")

else:
    print("Not Switched to new window")



