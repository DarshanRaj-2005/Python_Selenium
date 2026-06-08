from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, 10)
    driver.get("https://automationexercise.com/")

    assert driver.title == "Automation Exercise", "Home page title mismatch"
    print("Home page is reached.")

    driver.find_element(By.XPATH, "//a[@href = \"/login\"]").click()
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text() = \"Login to your account\"]"))).is_displayed(), "Login page is not reached"
    print("Login text is verified")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-qa = \"login-email\"]"))).send_keys("messi1@gmail.com")
    driver.find_element(By.XPATH, "//input[@data-qa = \"login-password\"]").send_keys("messi10")
    driver.find_element(By.XPATH, "//button[@data-qa = \"login-button\"]").click()

    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//i/following-sibling::b"))).text == "messi", "Cannot login"
    print("Login Successfull")
    delBtn = driver.find_element(By.XPATH, "//a[@href = \"/delete_account\"]")
    driver.execute_script("arguments[0].click();",delBtn)

    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text() = \"Account Deleted!\"]"))).is_displayed(), "Cannot delete account"
    print("Account deleted successfully.")
    print("Test case passed.")
    
except Exception as e:
    print(f"Test Failed: {e}")
    raise

finally:
    driver.quit()

