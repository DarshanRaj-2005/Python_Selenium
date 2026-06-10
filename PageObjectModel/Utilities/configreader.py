from configparser import ConfigParser

config = ConfigParser()
config.read("C:/Users/dhars/Documents/Python_Selenium/PageObjectModel/Configurations/config.ini")

def readData(category,key):
    value = config.get(category,key)
    return value