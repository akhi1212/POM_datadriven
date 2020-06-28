import configparser
import os

def readLocData(section, key):
    config = configparser.ConfigParser()
    ##G:\framework_setup\locators_testdata\locator.cfg
    data = os.path.relpath('../locators_testdata/locator.cfg')
    config.read(data)
    return config.get(section, key)


print('Locators', 'Sign_In')