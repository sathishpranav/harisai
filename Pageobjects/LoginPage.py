"""1. Open the chrome browser
2.open the url:https://admin-demo.nopcommerce.com
3. provide username:admin@yourstore.com
4.provide pwd:admin
5. click on the login
6.expected title
7. logout
"""
import time
class Loginpage:
    # locators of all the elements
    textbox_username_xpath = "//input[@id='Email']" #//input[@id='Email']
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//body/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]"
    link_logout_linktext = "Logout"
    def __init__(self,driver):
        self.driver = driver
    def setUserName(self,username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()




