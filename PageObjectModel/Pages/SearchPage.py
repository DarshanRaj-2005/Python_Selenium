from selenium.webdriver.common.by import By
class SearchPage:

    def __init__(self,driver):
        self.driver = driver

    macbookAir = (By.XPATH,"//*[@id='content']/div[3]/div/div/div[2]/div[1]/h4/a")