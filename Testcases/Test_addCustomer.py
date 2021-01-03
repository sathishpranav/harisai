import pytest
import time
import random
import string
from selenium import webdriver
from Pageobjects.LoginPage import Loginpage
from Pageobjects.AddCustomerPage import addCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LoG




class Test_003_addCustomer:
    baseURL = Readconfig.getAppURL()
    username = Readconfig.getUseName()
    password = Readconfig.getPassWord()
    logger_object = LoG.log_gen()

    @pytest.mark.sanity
    @pytest.mark.Regression
    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.clickLogin()
        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"
        if actual_title == expected_title:
            assert True
            self.logger_object.info("****Loggin test is passed*****")
        else:
            self.driver.get_screenshot_as_file(
                filename="/Screenshots\\test_003_addCustomer.png")
            self.driver.close()
            self.logger_object.info("****Loggin test is failed*****")
            assert False
        self.logger_object.info("****start AddCustomer Test*****")
        self.addCust = addCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerSubMenu()
        self.addCust.clickOnAddNew()
        self.logger_object.info("***Provide Customer information****")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setpassword("test123")
        self.addCust.setFirstName("sairam")
        self.addCust.setLastName("Hari")
        time.sleep(6)
        self.addCust.setGender("Male")
        time.sleep(6)
        self.addCust.setDOB("01/01/1870")
        self.addCust.setCompanyName("shiridiIndia")
        time.sleep(15)
        # self.addCust.setNewsletter("HELLO")
        #self.addCust.setCustomerroles("")
        self.addCust.setCustomerroles("Guests")

        self.addCust.setCustomerroles("Forum Moderators")



        time.sleep(15)
        self.addCust.setManagerOfVendor("Vendor 1")
        time.sleep(10)
        self.addCust.setAdminComment("This is for Testing purpose1")
        self.addCust.click_save()
        self.logger_object.info("****saving customer informatiion****")
        self.logger_object.info("***starting add customer validation***")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
"""
        if 'The new customer has been added successfully.'in self.msg :
            assert True==True
            self.logger_object.info("TheAddCustomer test case is passed:")
        else:
            self.logger_object.info("The add cust test case is failed")
            self.driver.get_screenshot_as_file(filename ="C:\\Users\\rohit\\PycharmProjects\\NOPCOM\\Screenshots\\test_addCust.png")
            assert True == False
        self.driver.close()
"""



def random_generator(size =8,char =string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))


