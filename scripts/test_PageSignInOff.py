from utitlity import  Initiatebrowser
from Pages import Login



class TestPers:

    def test_Validatepom(self):
        driver = Initiatebrowser.startAnyBrowser()
        loginP = Login.LoginPage(driver)
        loginP.clicksingIn()
        loginP.enterUsername("admin")
        loginP.enterPassword("admin")
        loginP.clickSubmitButton()
        Initiatebrowser.closeBrowser()


