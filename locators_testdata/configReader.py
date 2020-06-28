import configparser
import os

def readConfigData(section, key):
    config = configparser.ConfigParser()
    ##G:\framework_setup\locators_testdata\locator.cfg
    data = os.path.relpath('../locators_testdata/Config.cfg')
    config.read(data)
    return config.get(section, key)


print(readConfigData('Details' ,'application_url'))