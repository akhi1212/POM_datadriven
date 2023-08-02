from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators_testdata import configReader


class BaseDriver:
    
    def __init__(self,driver):
        self.driver =driver
        
    ## This is explicit wait     
    def global_wait_explicit_single_elemnt(self,wait,locator):
        # list_element = self.wait.until(EC.presence_of_all_elements_located((By.locator_type,locator)))
        # self.wait.until(EC.presence)
        # wait_val = self.WebDriverWait(self.driver, wait).wait_val.until(EC.presence_of_element_located(locator_type,locator))
        wait_va = WebDriverWait(self.driver,wait)
        elem = wait_va.until(EC.visibility_of_element_located((By.XPATH,locator)))
        return elem
    
    ## This is entering data in text field 
    def text_field_entered(self,locator,testdata):
        generic_wait = configReader.readConfigData('Details', 'globalWait')
        user__entered = self.global_wait_explicit_single_elemnt(generic_wait,locator)
        final_value = user__entered.send_keys(testdata)
        return final_value
    
    
        # self.driver.find_element("xpath",locator).send_keys(testdata)
        # return wait_for_ele
        
    ## This is generic hyperlink     
    def click_hyperlink(self,locator):
        generic_wait = configReader.readConfigData('Details', 'globalWait')
        user_click = self.global_wait_explicit_single_elemnt(generic_wait,locator)
        user_click.click()
        
    ### logic to extract data from table 
    def tble_data_verify(self):
        columns = len(self.driver.find_elements(By.XPATH,"//table[contains(@id,'_ctl0__ctl0_Content_Main_MyTransactions')]//tr[1]//td"))
        rows = len(self.driver.find_elements(By.XPATH,"//table[contains(@id,'_ctl0__ctl0_Content_Main_MyTransactions')]//tr"))
        print("rows - ",rows)   # rows -  3
        print("columns - ",columns) #columns -  4
        for row in range(1,rows):
            # print(row)
            for col in range(1,columns+1):
                values = self.driver.find_element(By.XPATH,"//table[contains(@id,'_ctl0__ctl0_Content_Main_MyTransactions')]//tr["+str(row)+"]//td["+str(col)+"]").text
                open('../utitlity/table.txt','w+').write(values)

                    
                # print(f"Dynamic web table index {row}, ---> {col}, --------> {values}",end="")
                # print(values,end="")
                # print(type(values))
        # if (values.find(dataMatch)== 1):
        #     assert True
                    # break
    
                # values = self.driver.find_element(By.XPATH,"//table[contains(@id,'_ctl0__ctl0_Content_Main_MyTransactions')]//tr["+str(row+1)+"]//td["+str(col+1)+"]").text
                # print(valuesF,end="  ")
                # else:
                #     value_ele = self.driver.find_element(By.XPATH,"//table[contains(@id,'_ctl0__ctl0_Content_Main_MyTransactions')]//tr["+str(row-1)+"]//td["+str(col-1)+"]").text
                #     print(value_ele,end="")
        # generic_wait = configReader.readConfigData('Details', 'globalWait')
        # table_data = self.driver.find_element("xpath",table_locator)
        # # rows=str(table_data.find_elements(By.TAG_NAME,"tr"))
        # # table_id = driver.find_element(By.ID, 'data_configuration_feeds_ct_fields_body0')
        # rows = table_data.find_elements(By.TAG_NAME, "tr") 
        # # get all of the rows in the table
        # for row in rows:	
        # # Get the columns (all the column 2)    
        #      #note: index start from 0, 1 is col 2
        #     col = row.find_elements(By.TAG_NAME, "td")
        #     print(col.text) #prints text from the element

        # for row in rows[1:]:
        #     cells=row.find_elements(By.TAG_NAME,"td")
        #     transaction_ID,transaction_Time,account_ID,action,amount = [cell.text for cell in cells]
        #     print(f"Transaction ID is {transaction_ID}, Transaction Time is {transaction_Time}, account ID is {account_ID}, Action is {action}, Amount is {amount} ")
        #     return transaction_ID,transaction_Time,account_ID,action,amount
        
    
    def cap_screenshot(self,file):
        return  self.driver.save_screenshot(file)