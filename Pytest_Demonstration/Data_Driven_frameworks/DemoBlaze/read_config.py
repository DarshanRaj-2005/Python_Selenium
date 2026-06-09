from configparser import ConfigParser

config = ConfigParser()

config.read("C:/Users/dhars/Documents/Python_Selenium/Pytest_Demonstration/Data_Driven_frameworks/DemoBlaze/config.ini")

def getData(category,key):
    value = config.get(category,key)
    return value