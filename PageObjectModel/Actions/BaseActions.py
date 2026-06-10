from selenium.webdriver.support import expected_conditions as ec
class BaseActions:

    def jsclick(self,element):
        ele = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].click();",ele)
    
    def send(self,element,value):
        self.driver.find_element(*element).send_keys(value)
    
    def visibilityWait(self,element):
        self.wait.until(ec.visibility_of_element_located(element))
    
    def gettext(self,element):
        return self.driver.find_element(*element).text