from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from Pageobjects.SearchCustomerPage import search_customer
from Pageobjects.LoginPage import Loginpage
from Pageobjects.AddCustomerPage import addCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LoG
import time

class Test_searchCustBY_Fname:


    baseURL = Readconfig.getAppURL()
    username = Readconfig.getUseName()
    password = Readconfig.getPassWord()
    logger_object = LoG.log_gen()

    def test_searchCustby_Fname(self,setup):

        self.logger_object.info("***search customer by_first Name")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.logger_object.info("******Login the application****")
        self.LP =Loginpage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.clickLogin()
        time.sleep(3)
        self.addCust =addCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerSubMenu()
        self.SFN=search_customer(self.driver)
        self.SFN.setFname("James")
        self.SFN.setLName("Pan")
        self.SFN.clickSearch()
        time.sleep(10)
        status = self.SFN.searchCustbyname("James Pan")
        time.sleep(5)
        assert True ==status
        self.logger_object.info("****search customer by fname test caseis passed***")


