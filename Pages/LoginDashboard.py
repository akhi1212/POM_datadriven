from locators_testdata import locatorReader
import time
from BaseClass.base_driver import BaseDriver

class ViewDashboardPage(BaseDriver):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver
    
    def click_viewTrasactionPage(self):
        read_data_sin = locatorReader.readLocData('Locators', 'view_transaction_summary')
        self.click_hyperlink(read_data_sin)    

