from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

driver = wb.Chrome()
driver.get("https://www.leafground.com/select.xhtml")
driver.maximize_window()
wait = WebDriverWait(driver,15)

selectBox1 = driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']")
select = Select(selectBox1)
select.select_by_visible_text("Selenium")

selectBox2 = driver.find_element(By.XPATH,"//*[@id='j_idt87:country']/div[3]")
selectBox2.click()

wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//li[text()='India']"))).click()

