from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Actions import click

try:
    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, 10)

    driver.maximize_window();
    driver.get("https://automationexercise.com/")

    assert driver.title == "Automation Exercise", "Home page is not reached."
    print("Home page is reached.")

    click(driver, (By.XPATH, "//a[@href = \"/products\"]"))

    assert "products" in driver.title, "All Products Page is not reached."
    print("All Products Page is reached")

    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name = \"search\"]"))).send_keys("Shirt")
    driver.find_element(By.XPATH,"//button[@id = \"submit_search\"]").click()

    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class = \"features_items\"]"))).is_displayed(), "Products not displayed."
    print("Related products displayed.")
    print("Test case passed.")
    
except Exception as e:
    print(e)

finally:
    driver.quit()