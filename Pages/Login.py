from locators_testdata import locatorReader
import time
from utitlity import testFixtures


class LoginPage:

    def __init__(self, obj):
        global driver
        driver = obj


    def clicksingIn(self):
        read_data_sin = locatorReader.readLocData('Locators', 'Sign_In')
        driver.find_element_by_xpath(read_data_sin).click()

    def enterUsername(self, username):
        read_usr = locatorReader.readLocData('Locators', 'user_name')
        driver.find_element_by_xpath(read_usr).send_keys(username)

    def enterPassword(self, password):
        read_data_pass = locatorReader.readLocData('Locators', 'passwd')
        driver.find_element_by_xpath(read_data_pass).send_keys(password)

    def clickSubmitButton(self):
        bttn_clk = locatorReader.readLocData('Locators', 'bttn')
        driver.find_element_by_xpath(bttn_clk).click()
        time.sleep(10)

    def clickSignoff(self):
        sign_off = locatorReader.readLocData('Locators','sign_off')
        driver.find_element_by_xpath(sign_off).click()