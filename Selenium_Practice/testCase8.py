from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

try:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    assert driver.title == "Automation Exercise", "Home page is not reached."
    print("Home page is reached.")

    # Click Products
    products_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='/products']")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        products_link
    )

    assert (
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[text()='All Products']")
            )
        ).text
        == "ALL PRODUCTS"
    ), "All Products Page is not reached."

    print("All Products Page is reached")

    assert wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='features_items']")
        )
    ).is_displayed(), "Default products not displayed."

    print("Default products are displayed.")

    # Product Details Click
    product_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//a[contains(@href,'product_details')])[1]")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        product_link
    )

    driver.execute_script(
        "arguments[0].click();",
        product_link
    )

    print("Current URL:", driver.current_url)

    assert wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='product-information']")
        )
    ).is_displayed(), "Product information is NOT displayed."

    print("Product information is displayed.")

    print("Test case passed.")

except Exception as e:
    print("\n========== TEST FAILED ==========")
    print("Exception Type :", type(e).__name__)
    print("Exception      :", str(e))
    traceback.print_exc()

finally:
    driver.quit()