from selenium import webdriver

#to run in incognito mode

# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--incognito")
# driver = webdriver.Chrome(options=options)

driver = webdriver.chrome()
driver.maximize_window
driver.get("https://www.google.co.in")
print(driver.title)
driver.close()