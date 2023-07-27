import pytest
from locators_testdata import locatorReader
from selenium import webdriver
from excel_data.ReadingExcel import excelDataReader
from Pages.SearchData import SearchData
import logging
import time


class TestSearchSample:

    # def dataGernrat():
    #     li = [['test'],['test2'], ['checkbounce']]
    #     return li

    @pytest.mark.parametrize('data', excelDataReader())
    def test_Validatesearchcall(self, data):
        log = logging.getLogger('test_Validatecall')
        search_data = SearchData(self.driver)
        search_data.search_data(data[0])
        # self.driver.find_element_by_xpath(read_data_search).send_keys()
        # #search_go
        # self.driver.find_element_by_xpath(read_data_search).send_keys()
        # self.driver.find_element_by_xpath(read_data_search).click()
