from BaseClass.base_driver import BaseDriver
from locators_testdata import locatorReader
import time


class SearchData(BaseDriver):
    
    def __init__(self,driver):      
        super().__init__(driver)
        # super().__init__(wait)  
        self.driver = driver


    def search_data(self,data):
        read_search_go = locatorReader.readLocData('Locators', 'search_go')
        # self.driver.find_element_by_xpath(read_data_search).click()
        # time.sleep(5)
        read_data_search = locatorReader.readLocData('Locators', 'serch_item')
        print(read_data_search)
        self.text_field_entered(read_data_search,data)
        # self.driver.find_element("xpath",read_data_search).send_keys(data)
        self.driver.find_element("xpath",read_search_go).click()
        time.sleep(5)
        return data
