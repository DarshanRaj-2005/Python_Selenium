from selenium.webdriver.common.by import By
class LoginPage:

    def __init__(self,driver):
        self.driver = driver
    
    myacc = (By.XPATH,"//div[@id='top-links']/ul/li[2]/a")
    login = (By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[2]/a")
    userName = (By.XPATH,"//*[@id='input-email']")
    passWord = (By.XPATH,"//*[@id='input-password']")
    submitBtn = (By.XPATH,"//*[@id='content']/div/div[2]/div/form/input")
    logout = (By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[5]/a")
    searchBar = (By.XPATH,"//*[@id='search']/input")
    searchBtn = (By.XPATH,"//*[@id='search']/span/button")


