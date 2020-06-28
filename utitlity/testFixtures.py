import pytest
from locators_testdata import configReader
import os
from selenium import webdriver

global driver
@pytest.fixture(scope="class")
def startbrowser(request):

    if ((configReader.readConfigData('Details', 'browser')) == 'chrome'):
        driver = webdriver.Chrome(os.path.relpath('../driver/chromedriver'))
    elif ((configReader.readConfigData('Details', 'browser')) == 'firefox'):
        driver = webdriver.Firefox(executable_path=os.path.relpath('../driver/geckodriver'))

    ## maximize browser window
    driver.maximize_window()
    ## enter url in the browser
    driver.get(configReader.readConfigData('Details', 'application_url'))

     ## implicit wait to load complete page
    driver.implicitly_wait(configReader.readConfigData('Details', 'globalWait'))
    request.cls.driver = driver
    yield
    driver.close()
    return driver