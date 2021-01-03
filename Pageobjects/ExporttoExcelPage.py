"""1. Open the chrome browser
2.open the url:https://admin-demo.nopcommerce.com
3. provide username:admin@yourstore.com
4.provide pwd:admin
5. click on the login
6.Navigate to customers >>customers(sub menu)>>Add customer
7.Export to excel
"""
import time

class Eport_excel:
    # Locators of All elements"
    #btn_export_xpath="//div[@class ='btn-group open']"
    table_xpath ="//body/div[3]/div[3]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]"
    btn_export_css ="button.btn.btn btn-success dropdown-toggle[data-toggle='dropdown']"
    btn_export_xpath ="//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/button[2]"
    #lnk_export_xpath ="//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/button[1]"
    lnk_export_all_xpath ="// button[@ name ='exportexcel-all']"
    lnk_export_selected_xpath ="//button[@id='exportexcel-selected']"
    chk_box_name ="checkbox_customers"
    # List of action method for the above Elements

    def __init__(self, driver):
        self.driver = driver

    def click_export(self):
        self.driver.find_element_by_xpath(self.btn_export_xpath).click()
        #self.driver.find_element_by_css_selector(self.btn_export_css).click()
    def click_export_all(self):
        self.driver.find_element_by_xpath(self.lnk_export_all_xpath).click()

    def select_checkbox(self):
        checkboxes =[]
        checkboxes=self.driver.find_elements_by_name(self.chk_box_name)
        print(checkboxes[0].is_selected())
        checkboxes[0].click()
        checkboxes[4].click()
        print(checkboxes[0])
        print(checkboxes[0].is_selected())
        print(len(checkboxes))

    def export_selected(self):
        self.driver.find_element_by_xpath(self.lnk_export_selected_xpath).click()




