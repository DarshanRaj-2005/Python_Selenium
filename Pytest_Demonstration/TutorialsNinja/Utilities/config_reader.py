from configparser import ConfigParser


def get_value(filename,category, key):
    config = ConfigParser()
    config.read("C:/Users/dhars/Documents/Python_Selenium/Pytest_Demonstration/TutorialsNinja/DataFiles/"+filename)
    return config.get(category, key)