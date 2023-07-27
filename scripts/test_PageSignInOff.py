import time
from utitlity import  Initiatebrowser
from Pages.Login import LoginPage
from locators_testdata import configReader
import pytest


class TestPers:

    def test_Validatepom(self):
        # driver = Initiatebrowser.startAnyBrowser()
        loginP = LoginPage(self.driver)
        loginP.clicksingIn()
        read_usr_value = configReader.readConfigData('Details', 'username')
        loginP.enterUsername(read_usr_value)
        # loginP.enterUsername()
        read_pass_value = configReader.readConfigData('Details', 'password')
        loginP.enterPassword(read_pass_value)
        loginP.clickSubmitButton()
        time.sleep(2)
        loginP.clickSignoff()
        time.sleep(2)


