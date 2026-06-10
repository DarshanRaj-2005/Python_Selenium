from Pages.SearchPage import SearchPage
from Pages.LoginPage import LoginPage
from Actions.BaseActions import BaseActions

class SearchAction(BaseActions):

    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def validSearch(self):
        self.send(LoginPage.searchBar,"Macbook Air")
        self.jsclick(LoginPage.searchBtn)
    
    def checkingtext(self):
        return "MacBook Air" in self.gettext(SearchPage.macbookAir)

