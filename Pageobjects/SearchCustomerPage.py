"""1. Open the chrome browser
2.open the url:https://admin-demo.nopcommerce.com
3. provide username:admin@yourstore.com
4.provide pwd:admin
5. click on the login
6.Navigate to customers >>customers(sub menu)>>Add customer
7.search customer by email
8.search customer by Fname
8. logout
"""
import string
import time

class search_customer:
    #Locators of all the elements
    txt_email_id= "SearchEmail"
    txt_fname_id ="SearchFirstName"
    txt_lname_id ="SearchLastName"
    btn_search_id ="search-customers"
    tbl_xpath= "//div[@id='customers-grid_wrapper']"
    tbl_searchResult_xpath ="//table[@role ='grid']"
    tblRows_xpath ="//div[@id ='customers-grid_wrapper']//tbody//tr"
    tblcolumns_xpath="//div[@id='customers-grid_wrapper']//tbody//tr//td"

    # List of action method for the above Elements

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txt_email_id).clear()
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)
    def setFname(self,Fname):
        self.driver.find_element_by_id(self.txt_fname_id).clear()
        self.driver.find_element_by_id(self.txt_fname_id).send_keys(Fname)
    def setLName(self,Lname):
        self.driver.find_element_by_id(self.txt_lname_id).clear()
        self.driver.find_element_by_id(self.txt_lname_id).send_keys(Lname)
    def clickSearch(self):
        self.driver.find_element_by_id(self.btn_search_id).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tblRows_xpath))

    def getNoOfColums(self):
        columns  =self.driver.find_elements_by_xpath(self.tblcolumns_xpath)
        return len(columns)

    def searchCustbyEmail(self,email):
        flag=False
        for r in range (1,self.getNoOfRows()+1):
            table =self.driver.find_element_by_xpath(self.tbl_xpath)
            email_id=table.find_element_by_xpath("//div[@id='customers-grid_wrapper']//tbody/tr["+str(r)+"]/td[2]").text
            time.sleep(10)
            if email_id == email:
                flag =True
                break
        return flag

    def searchCustbyname(self,name):
        flag =False
        for r in range (1,self.getNoOfRows()+1):
            table =self.driver.find_element_by_xpath(self.tbl_xpath)
            Name =table.find_element_by_xpath("//div[@id='customers-grid_wrapper']//tbody/tr["+str(r)+"]/td[3]").text
            time.sleep(5)
            if Name ==name:
                flag =True
                break
        return flag














