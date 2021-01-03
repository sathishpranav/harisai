"""1. Open the chrome browser
2.open the url:https://admin-demo.nopcommerce.com
3. provide username:admin@yourstore.com
4.provide pwd:admin
5. click on the login
6.Navigate to customers >>customers(sub menu)>>Add customer
"""
""" multiple condition: 
//div[@class='bubble-title' and contains(text(), 'Cover')]
partial match: //span[contains(text(), 'Assign Rate')]
starts-with: //input[starts-with(@id,'reportcombo')]
value has spaces: //div[./div/div[normalize-space(.)='More Actions...']]
sibling: //td[.='LoadType']/following-sibling::td[1]/select"
more complex: //td[contains(normalize-space(@class), 'actualcell sajcell-row-lines saj-special x-grid-row-collapsed')]
"""


from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class addCustomer():
    #Locators of All elements
    lnkcustomers_menu_xpath = "//body/div[3]/div[2]/div[1]/ul[1]/li[4]/a[1]"
    lnkcustomers_submenu_xpath ="//body/div[3]/div[2]/div[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/span[1]"
    btnAddnew_xpath="//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath ="//input[@id='Email']"
    txtPassword_xpath ="//input[@id='Password']"
    txtFname_xpath="//input[@id='FirstName']"
    txtLname_xpath ="//input[@id='LastName']"
    RdMaleGender_id="Gender_Male"
    RdFeMaleGender_id ="Gender_Female"
    txtDob_xpath="//input[@id='DateOfBirth']"
    txtCompanyName_xpath="//input[@id='Company']"
    chk_isTaxExmpt_xpath = "//input[@id='IsTaxExempt']"
    txt_Newsletter_xpath = "//body/div[3]/div[3]/div[1]/form[1]/div[3]/div[1]/nop-panels[1]/nop-panel[1]/div[1]/div[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]"
    txt_custRole_xpath="//body/div[3]/div[3]/div[1]/form[1]/div[3]/div[1]/nop-panels[1]/nop-panel[1]/div[1]/div[2]/div[1]/div[10]/div[2]/div[1]/div[1]/div[1]"
    lstitem_Guests_xpath ="//li[contains(text(),'Guests')]"
    lstitem_Administrators_xpath ="//li[contains(text(),'Administrators')]"
    lstitem_Forum_Moderators_xpath="//li[contains(text(),'Forum Moderators')]"
    lstitem_Registered_xpath ="//li[contains(text(),'Registered')]"
    lstitem_Vendors_xpath ="//li[contains(text(),'Vendors')]"
    drp_ManagerofVendors_xpath = "//select[@id='VendorId']"
    txt_admincomment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"


# List of action method for the above Elements

    def __init__(self,driver):
        self.driver =driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkcustomers_menu_xpath).click()
    def clickOnCustomerSubMenu(self):
        self.driver.find_element_by_xpath(self.lnkcustomers_submenu_xpath).click()


    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLname_xpath).send_keys(lname)

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,cmp):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(cmp)
    def setNewsletter(self,Newsltr):
        self.driver.find_element_by_xpath(self.txt_Newsletter_xpath).send_keys(Newsltr)
    def setCustomerroles(self,role):
        self.driver.find_element_by_xpath(self.txt_custRole_xpath).click()
        time.sleep(3)
        #Here the user canbe Registered or Guests
        if role == "Registered":
           self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)
        elif role =="Administrators":
            self.listitem =self.driver.find_element_by_xpath(self.lstitem_Administrators_xpath)
        elif role == "Guests":
            time.sleep(10)
            self.driver.find_element_by_xpath("//li[contains(text(),'Registered')]").click()
            time.sleep(4)
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)

        elif role =="Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)
        elif role=="Vendors":
            self.listitem =self.driver.find_element_by_xpath(self.lstitem_Vendors_xpath)
        elif role =="Forum Moderators":
            self.listitem= self.driver.find_element_by_xpath(self.lstitem_Forum_Moderators_xpath)
        else:
            self.listitem=self.driver.find_element_by_xpath(self.lstitem_Guest_xpath)
        time.sleep(15)
        #self.listitem.click()#Ifthis click action is not working we can go for java script
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
      drpdownMgr_vendor =Select(self.driver.find_element_by_xpath(self.drp_ManagerofVendors_xpath))
      drpdownMgr_vendor.select_by_visible_text(value)


    def setGender(self,gender):
        if gender =="Male":
            self.driver.find_element_by_id(self.RdMaleGender_id).click()
        elif gender =="Female":
            self.driver.find_element_by_id(self.RdFeMaleGender_id).click()
        else :
            self.driver.find_element_by_id(self.RdMaleGender_id).click()
    def setAdminComment(self,comment):
        self.driver.find_element_by_xpath(self.txt_admincomment_xpath).send_keys(comment)
    def click_save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()













