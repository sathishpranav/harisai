import pytest
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Utilities import XLUtils
from Pageobjects.LoginPage import Loginpage
from Utilities.customLogger import LoG
import time
import sys
sys.path.append("C://Users//rohit//PycharmProjects//NOPCOM")
class Test_ddt_002:
    baseURL = Readconfig.getAppURL()
    path ="C:\\Users\\rohit\\PycharmProjects\\NOPCOM\\TestData\\Book2.xlsx"
    LO = LoG.log_gen()
    @pytest.mark.Regression
    def test_login_DDT(self,setup):
        self.LO.info("*****Test_ddt_002****")
        self.LO.info("****Verify Login page****")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.rows =XLUtils.getRowCount(self.path,sheetName="Sheet1")
        self.columns =XLUtils.getColumnCount(self.path,sheetName="Sheet1")
        print(" No of rows in excel:",self.rows)
        print("No of columns in excel",self.columns)
        Lis_status =[]
        #print(Lis_status)
        for r in range (2,self.rows+1):
            self.username =XLUtils.readData(self.path,sheetName="Sheet1",rownum=r,columnno=1)
            self.password =XLUtils.readData(self.path,sheetName="Sheet1",rownum=r,columnno=2)
            self.expected=XLUtils.readData(self.path,sheetName="Sheet1",rownum=r,columnno=3)
            self.output =XLUtils.readData(self.path,sheetName="Sheet1",rownum=r,columnno=4)

            self.LP.setUserName(self.username)
            self.LP.setPassword(self.password)
            self.LP.clickLogin()
            time.sleep(10)
            actual_title =self.driver.title
            expected_title="Dashboard / nopCommerce administration"
            if actual_title == expected_title :
                if self.expected =="pass":
                    self.LO.info("***Passed")
                    self.LP.clicklogout()
                    time.sleep(3)
                    Lis_status.append("Pass")
                    self.output=XLUtils.writeData(self.path,sheetName="Sheet1",rownum=r,columnno=4,data="Pass")
                elif self.expected =="fail":
                    self.LO.info("***Failed")
                    self.LP.clicklogout()
                    time.sleep(10)
                    Lis_status.append("Fail")
                    self.output=XLUtils.writeData(self.path,sheetName="Sheet1",rownum=r,columnno=4,data="Fail")

            elif actual_title != expected_title:
                if self.expected =="pass":
                    self.LO.info("****Failed")
                    Lis_status.append("Fail")
                    self.output=XLUtils.writeData(self.path,sheetName="Sheet1",rownum=r,columnno=4,data="Fail")

                    time.sleep(10)
                elif self.expected =="fail":
                    self.LO.info("****Passed")
                    Lis_status.append("Pass")
                    self.output=XLUtils.writeData(self.path,sheetName="Sheet1",rownum=r,columnno=4,data="Pass")

                    time.sleep(5)
        if "Fail" not in Lis_status:
            self.LO.info("The DDT test is passed")
            self.driver.close()
            assert True
        else :
            self.LO.info("the DDT test is failed")
            self.driver.close()
            assert False
        self.LO.info("End of Login_DDT test")
        self.LO.info("complete the test case for data driven")







