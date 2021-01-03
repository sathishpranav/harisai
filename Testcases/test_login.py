import pytest
from selenium import webdriver
from Pageobjects.LoginPage import Loginpage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LoG


class Test_001_login:

    baseURL= Readconfig.getAppURL()
    username = Readconfig.getUseName()
    password =Readconfig.getPassWord()
    logger_object =LoG.log_gen()


    def test_homepageTitle(self, setup):

        self.logger_object.info("****Test_001_Login*****")
        self.logger_object.info("****verify_homePage*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        expected_title = "Your store. Login"
        if actual_title == expected_title:
            assert True
            self.driver.close()
            self.logger_object.info("****Home Page title test is passed*****")
        else:
            self.driver.close()
            self.logger_object.info("****Home Page title test is failed*****")
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger_object.info("****Verify Login Page *****")
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
            self.driver.get_screenshot_as_file(filename ="/Screenshots\\test_login_001.png")
            self.driver.close()
            self.logger_object.info("****Loggin test is failed*****")
            assert False
        self.logger_object.info("****Test complete*****")
        self.logger_object.info("****Thanks*****")

        self.LP.clicklogout()








