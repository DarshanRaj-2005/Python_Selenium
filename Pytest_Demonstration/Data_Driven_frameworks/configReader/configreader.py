from configparser import ConfigParser

config = ConfigParser()
config.read("C:/Users/dhars/Documents/Python_Selenium/Pytest_Demonstration/Data_Driven_frameworks/configReader/config.ini")
def getDatas(category, key):
    value = config.get(category, key)
    return value

