from locators_testdata import configReader
import time
from Pages.LoginDashboard import ViewDashboardPage
from Pages.Login import LoginPage
from Pages.ViewTrasaction import ViewTrasactionverify


class TestViewTrasactionTable:
    
    
    def test_Trasactions(self):
        login_account = LoginPage(self.driver)
        login_account.clicksingIn()
        read_usr_value = configReader.readConfigData('Details', 'username')
        read_pass_value = configReader.readConfigData('Details', 'password')
        login_account.login_account(read_usr_value,read_pass_value)
        time.sleep(4)
        dashboard_acc = ViewDashboardPage(self.driver)
        dashboard_acc.click_viewTrasactionPage()
        time.sleep(3)
        viewTrasnstable = ViewTrasactionverify(self.driver)
        # viewTrasnstable.verify_table_transactions("00")  ##4045
        viewTrasnstable.verify_tble_value("14276")
        viewTrasnstable.tble_data_verify()
        time.sleep(2)
        