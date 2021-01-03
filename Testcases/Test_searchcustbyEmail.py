from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from Pageobjects.SearchCustomerPage import search_customer
from Pageobjects.LoginPage import Loginpage
from Pageobjects.AddCustomerPage import addCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LoG
import time

class Test_searchCustBY_email:


    baseURL = Readconfig.getAppURL()
    username = Readconfig.getUseName()
    password = Readconfig.getPassWord()
    logger_object = LoG.log_gen()
    @pytest.mark.Regression
    def test_searchCustby_Email(self,setup):

        self.logger_object.info("***search customer by_email")
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
        self.SEmail=search_customer(self.driver)
        self.SEmail.setEmail("victoria_victoria@nopCommerce.com")
        self.SEmail.clickSearch()
        time.sleep(10)
        status = self.SEmail.searchCustbyEmail("victoria_victoria@nopCommerce.com")
        time.sleep(5)
        self.driver.implicitly_wait(5)
        assert True ==status
        self.logger_object.info("****search customer test caseis passed***")
        self.driver.close()


