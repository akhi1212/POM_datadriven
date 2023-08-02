import os
from locators_testdata import locatorReader
import time
from BaseClass.base_driver import BaseDriver
from selenium.webdriver.common.by import By


class ViewTrasactionverify(BaseDriver):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver
        

    def verify_table_transactions(self,dataNatchedValue):
        table_com = locatorReader.readLocData('Locators', 'trans_table')
        final_tab = str(table_com)
        print(type(final_tab))
        # rows = locatorReader.readLocData('Locators', 'trans_table_3')
        # cols = locatorReader.readLocData('Locators', 'trans_table_2')
        self.tble_data_verify(dataNatchedValue)

    def verify_tble_value(self,verifydata):
        webcolm = "//table[contains(@id,'_ctl0__ctl0_Content_Main_MyTransactions')]//tr//td[1]"
        value_cols = len(self.driver.find_elements(By.XPATH,webcolm))
        cols_data= self.driver.find_element(By.XPATH,webcolm).text
        print(cols_data)
        print(type(cols_data))
        for i in range(1,value_cols+1):
            a= self.driver.find_element(By.XPATH,"//table[contains(@id,'_ctl0__ctl0_Content_Main_MyTransactions')]//tr["+str(i)+"]//td[1]").text
            print(a,end= "   ")
            if (a == verifydata):
              print("passed")
              assert True
              break
        else:
            file_path = os.path.relpath("../screenshots_cap/table_cap_nont_matched.png")
            self.cap_screenshot(file_path)          
            print("Failed")
            assert False
            
        print()
        