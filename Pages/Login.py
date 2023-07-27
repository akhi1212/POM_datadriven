from locators_testdata import locatorReader
import time
from BaseClass.base_driver import BaseDriver

class LoginPage(BaseDriver):
    
    def __init__(self,driver):
        super().__init__(driver)
        # super().__init__(wait)  
        self.driver = driver
        


    def clicksingIn(self):
        read_data_sin = locatorReader.readLocData('Locators', 'Sign_In')
        self.driver.find_element("xpath",read_data_sin).click()

    def enterUsername(self,usernme):
        read_usr = locatorReader.readLocData('Locators', 'user_name')
        self.text_field_entered(read_usr,usernme)

    def enterPassword(self, password):
        read_pss = locatorReader.readLocData('Locators', 'passwd')
        self.text_field_entered(read_pss,password)

    def clickSubmitButton(self):
        bttn_clk = locatorReader.readLocData('Locators', 'bttn')
        self.driver.find_element("xpath",bttn_clk).click()
        time.sleep(10)

    def clickSignoff(self):
        sign_off = locatorReader.readLocData('Locators','sign_off')
        self.driver.find_element("xpath",sign_off).click()