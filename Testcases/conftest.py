from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser== "chrome":
        driver = webdriver.Chrome("C:\\Users\\rohit\\PycharmProjects\\NOPCOM\\Drivers\\chromedriver.exe")
        driver.maximize_window()
        print("Launching chrome browser")
    elif browser=="edge":
        driver= webdriver.Edge("C:\\Users\\rohit\\PycharmProjects\\NOPCOM\\Drivers\\msedgedriver.exe")
        driver.maximize_window()
        print("Launching edge browser")
    else:
        driver = webdriver.Ie("C:\\Users\\rohit\\PycharmProjects\\NOPCOM\\Drivers\\IEDriverServer.exe")
        driver.maximize_window()
        print("Launching IE")

    return driver

def pytest_addoption(parser):#this method willget the value from CLI/hooks
    parser.addoption("--browser")
@pytest.fixture()

def browser(request): #this will return the browser value to the setup method
    return request.config.getoption("--browser")

####pytest HTML report#####

#it is the hook for adding environment  info into HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='NOPCOMERCE'
    config._metadata['Module name']='customers'
    config._metadata['tester']='sathish KANAGARAJ'
# it is the hook for adding/deleting environment info  into HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)




