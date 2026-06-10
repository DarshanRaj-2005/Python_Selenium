import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.excel_reader import get_data
from Utilities.logger import get_logger

@pytest.mark.usefixtures("setup")

class TestLogin:

    @pytest.mark.order(2)
    @pytest.mark.parametrize("email,password",get_data("login_data.xlsx", "ValidLoginData"))
    def test_valid_login(self, email, password):
        logger = get_logger()
        wait = WebDriverWait(self.driver, 30)
        self.driver.save_screenshot("homepage.png")
        print("Current URL:", self.driver.current_url)
        print("Title:", self.driver.title)
        print("Page Source Length:", len(self.driver.page_source))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class = \"fa fa-user\"]"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
        logger.info(f"Entering Email : {email}")
        wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        wait.until(EC.url_contains("account"))
        assert "account" in self.driver.current_url.lower()
        logger.info("Login Successful")

    
    @pytest.mark.order(1)
    @pytest.mark.parametrize("email,password,message",get_data("login_data.xlsx", "InvalidLoginData"))
    def test_invalid_login(self, email, password, message):
        logger = get_logger()
        wait = WebDriverWait(self.driver, 30)
        self.driver.save_screenshot("homepage.png")
        print("Current URL:", self.driver.current_url)
        print("Title:", self.driver.title)
        print("Page Source Length:", len(self.driver.page_source))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class = \"fa fa-user\"]"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
        logger.info(f"Entering Email : {email}")
        wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert message == wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class ,\"alert\")]"))).text
        logger.info("Error message shown Successful")

    
    @pytest.mark.order(3)
    @pytest.mark.depends(depend="test_valid_login")
    @pytest.mark.parametrize("value",["MacBook"])
    def valid_search(self,value):
        loggger = get_logger()
        wait = WebDriverWait(self.driver,30)
        search = self.driver.find_element(By.XPATH,"//*[@id='search']/input")
        search.send_keys("mac")
        searchbtn = self.driver.find_element(By.XPATH,"//div[@id='search']/span/button")
        searchbtn.click()
        macbook = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div[3]/div[2]/div/div[2]/div[1]/h4/a")))
        assert macbook.text == value
        print("Test Passed")

