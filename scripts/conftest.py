import pytest
from locators_testdata import configReader
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import os


global driver
@pytest.fixture(scope="class", autouse=True)
def startbrowser(request,browser):
    # browser_name =  browser.config.getoption("--browser") 
    if browser == 'chrome':
        chromeexe_path = 'E:\Latest_browser_webdriver_exe\latest\latest-driver\chromedriver_win32'
        chrome_exe= os.path.join(os.getcwd(), 'chromedriver.exe')
        driver = webdriver.Chrome(os.path.relpath("../driver/chromedriver.exe"))
        # driver = webdriver.Chrome(ChromeDriverManager().install())
    elif  browser == 'edge':
        # driver = webdriver.Firefox(executable_path=os.path.relpath("../driver/geckodriver.exe"))
        # edge_pth = "E:/framework_setup/driver/msedgedriver"
        # driver = webdriver.Edge(edge_pth)
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        user_agent  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
        edge_path1 = os.path.join(os.getcwd(), 'msedgedriver.exe')
        edge_path = os.path.relpath("../driver/msedgedriver.exe")
        edge_service  = Service(edge_path)
        edge_options = Options()
        edge_options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Edge(service=edge_service, options=edge_options)
    else:
        raise ValueError(f"Please enter chrome and edge browser only  {browser}")

    ## maximize browser window
    driver.maximize_window()
    ## enter url in the browser
    driver.get(configReader.readConfigData('Details', 'application_url'))

     ## implicit wait to load complete page
    driver.implicitly_wait(configReader.readConfigData('Details', 'globalWait'))
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")    
    