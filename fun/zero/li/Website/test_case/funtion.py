from fun.zero.li.Website.test_case.BasePage import basepage
from fun.zero.li.Website.test_case.Elements import elements
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class funtion(basepage):
    def introjs_skip_button(self):
        elements.click(elements(), basepage.find_ele(basepage(self.driver), By.CLASS_NAME, "introjs-skipbutton"))

    def key_enter(self, by, value):
        elements.keys(elements(), basepage.find_ele_ele(basepage(self.driver), by, value), Keys.ENTER)

    def save_button(self, by, value):
        elements.js_script_click(elements(), self.driver, basepage.find_ele_ele(basepage(self.driver), by, value))
