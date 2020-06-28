from locators_testdata import configReader
import os
from selenium import webdriver

def startAnyBrowser():
    global driver
    if ((configReader.readConfigData('Details', 'browser')) == 'chrome'):
        driver = webdriver.Chrome(os.path.relpath('../driver/chromedriver'))
    elif ((configReader.readConfigData('Details', 'browser')) == 'firefox'):
        driver = webdriver.Firefox(executable_path=os.path.relpath('../driver/geckodriver'))

    ## maximize browser window
    driver.maximize_window()
    ## enter url in the browser
    driver.get(configReader.readConfigData('Details', 'application_url'))
    return driver

def closeBrowser():
    driver.close()