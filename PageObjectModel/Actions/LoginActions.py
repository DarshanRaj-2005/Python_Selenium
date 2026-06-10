from Pages.LoginPage import LoginPage
from Utilities import configreader
from Actions.BaseActions import BaseActions

class LoginActions(BaseActions):

    def login(self):
        self.jsclick(LoginPage.myacc)
        self.jsclick(LoginPage.login)
        self.visibilityWait(LoginPage.userName)
        self.send(LoginPage.userName,configreader.readData("credentials","user"))
        self.send(LoginPage.passWord,configreader.readData("credentials","passw"))
        self.jsclick(LoginPage.submitBtn)
    
    def checkingLogin(self):
        self.jsclick(LoginPage.myacc)
        self.visibilityWait(LoginPage.logout)
        return self.driver.find_element(*LoginPage.logout).is_displayed()
        
    
    
    
        

    
    
    
    

