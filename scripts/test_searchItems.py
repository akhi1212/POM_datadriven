import pytest
from locators_testdata import locatorReader
from selenium import webdriver
from utitlity.testFixtures import startbrowser
from excel_data.ReadingExcel import excelDataReader
import logging
import time


@pytest.mark.usefixtures("startbrowser")
class TestSearchSample:

    # def dataGernrat():
    #     li = [['test'],['test2'], ['checkbounce']]
    #     return li

    @pytest.mark.parametrize('data', excelDataReader())
    def test_Validatesearchcall(self, data):
        log = logging.getLogger('test_Validatecall')
        read_data_search = locatorReader.readLocData('Locators', 'serch_item')
        print(read_data_search)
        # self.driver.find_element_by_xpath(read_data_search).send_keys()
        # #search_go
        read_search_go = locatorReader.readLocData('Locators', 'search_go')
        # self.driver.find_element_by_xpath(read_data_search).click()
        # time.sleep(5)
        self.driver.find_element_by_xpath(read_data_search).send_keys(data[0])
        self.driver.find_element_by_xpath(read_search_go).click()
        time.sleep(5)
        # self.driver.find_element_by_xpath(read_data_search).send_keys()
        # self.driver.find_element_by_xpath(read_data_search).click()
