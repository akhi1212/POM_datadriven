import time
from Pages.Login import LoginPage
from Pages.LoginDashboard import ViewDashboardPage
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

    def test_linking_page(self):
        click_page = LoginPage(self.driver)
        click_page.click_personal()
        time.sleep(3)
        click_page.click_smallBusiness()
        time.sleep(3)
        click_page.click_altro()
        time.sleep(3)

    def test_TrasactionDetails(self):
        login_account = LoginPage(self.driver)
        login_account.clicksingIn()
        read_usr_value = configReader.readConfigData('Details', 'username')
        read_pass_value = configReader.readConfigData('Details', 'password')
        login_account.login_account(read_usr_value,read_pass_value)
        time.sleep(4)
        dashboard_acc = ViewDashboardPage(self.driver)
        dashboard_acc.click_viewTrasactionPage()