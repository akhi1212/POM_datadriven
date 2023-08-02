from locators_testdata import locatorReader
import time
from BaseClass.base_driver import BaseDriver

class LoginPage(BaseDriver):
    
    def __init__(self,driver):
        super().__init__(driver)
        # super().__init__(wait)  
        self.driver = driver
        

    ## Click Sign in button
    def clicksingIn(self):
        read_data_sin = locatorReader.readLocData('Locators', 'Sign_In')
        self.click_hyperlink(read_data_sin)
   
    ## Enter username 
    def enterUsername(self,usernme):
        read_usr = locatorReader.readLocData('Locators', 'user_name')
        self.text_field_entered(read_usr,usernme)
    
    ## Enter password.
    def enterPassword(self, password):
        read_pss = locatorReader.readLocData('Locators', 'passwd')
        self.text_field_entered(read_pss,password)

    ## Click Submit button
    def clickSubmitButton(self):
        bttn_clk = locatorReader.readLocData('Locators', 'bttn')
        self.driver.find_element("xpath",bttn_clk).click()
        time.sleep(2)
    
    ## Login into the account
    def login_account(self,username,password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickSubmitButton()

    ## click Signoff button
    def clickSignoff(self):
        sign_off = locatorReader.readLocData('Locators','sign_off')
        self.click_hyperlink(sign_off)
        
    ## clkick into the small business section
    def click_smallBusiness(self):
        small_bus = locatorReader.readLocData('Locators','small_business')
        self.click_hyperlink(small_bus)
    
     ## clkick into the personal section
    def click_personal(self):
        persnl_link = locatorReader.readLocData('Locators','personal_link')
        self.click_hyperlink(persnl_link)

     ## clkick into the altro  section
    def click_altro(self):
        inside_alt = locatorReader.readLocData('Locators','inside_altro')
        self.click_hyperlink(inside_alt)

