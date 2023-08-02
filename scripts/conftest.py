import time
import pytest
from locators_testdata import configReader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


global driver

@pytest.fixture(scope="class", autouse=True)
def startbrowser(request, browser):
    if browser == "chrome":
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
        common_option = ChromeOptions()
        common_option.page_load_strategy = 'none'
        common_option.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(options=common_option)
    elif browser == "edge":
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
        edge_options = EdgeOptions()
        edge_options.page_load_strategy = 'none'
        edge_options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError(f"Please enter chrome and edge browser only {browser}")
    driver.maximize_window()
    driver.get(configReader.readConfigData('Details', 'application_url'))
    driver.delete_all_cookies()
    time.sleep(1)
    driver.set_page_load_timeout(60)
    request.cls.driver = driver
    yield
    driver.close()
    
    
    
def pytest_addoption(parser):
    parser.addoption("--browser", action="store")
    
    
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")