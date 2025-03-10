from selenium.webdriver.common.by import By
from fun.zero.li.Website.test_case.funtion import funtion
from fun.zero.li.Website.test_case.Elements import elements
from fun.zero.li.Website.test_case.BasePage import basepage


class loginpage:
    def login(self, driver, username, password):
        elements.keys(elements(), basepage.find_ele(basepage(driver), By.ID, "loginName"), username)
        elements.keys(elements(), basepage.find_ele(basepage(driver), By.ID, "password"), password)
        elements.click(elements(), basepage.find_ele(basepage(driver), By.CLASS_NAME, "login-button"))
        funtion.introjs_skip_button(funtion(driver))
