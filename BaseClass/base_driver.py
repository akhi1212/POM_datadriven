from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators_testdata import configReader


class BaseDriver:
    
    def __init__(self,driver):
        self.driver =driver
        
        
    def global_wait_explicit_single_elemnt(self,wait,locator):
        # list_element = self.wait.until(EC.presence_of_all_elements_located((By.locator_type,locator)))
        # self.wait.until(EC.presence)
        # wait_val = self.WebDriverWait(self.driver, wait).wait_val.until(EC.presence_of_element_located(locator_type,locator))
        wait_va = WebDriverWait(self.driver,wait)
        elem = wait_va.until(EC.visibility_of_element_located((By.XPATH,locator)))
        return elem
    
    def text_field_entered(self,locator,testdata):
        generic_wait = configReader.readConfigData('Details', 'globalWait')
        user__entered = self.global_wait_explicit_single_elemnt(generic_wait,locator)
        final_value = user__entered.send_keys(testdata)
        return final_value
    
    
        # self.driver.find_element("xpath",locator).send_keys(testdata)
        # return wait_for_ele
        
        
    