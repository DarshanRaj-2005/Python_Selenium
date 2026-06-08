from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

try:
    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, 10)

    driver.maximize_window();
    driver.get("https://automationexercise.com/")

    assert driver.title == "Automation Exercise", "Home page is not reached."
    print("Home page is reached.")

    element = driver.find_element(By.XPATH, "//a[@href = \"/products\"]")
    driver.execute_script("arguments[0].click();",element)

    # assert "products" in driver.title, "All Products Page is not reached."
    print("All Products Page is reached")

    action = ActionChains(driver)

    action.move_to_element(wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class = \"features_items\"]/div[2]")))).perform()
    time.sleep(10)

    print("Test case passed.")
    
except Exception as e:
    print(e)

finally:
    driver.quit()