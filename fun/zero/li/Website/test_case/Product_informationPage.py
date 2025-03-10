from selenium.webdriver.common.by import By
from fun.zero.li.Website.test_case.Elements import elements
from fun.zero.li.Website.test_case.BasePage import basepage
from fun.zero.li.Website.test_case.funtion import funtion


class product_informationPage(basepage):
    def product_information(self, name, value):
        elements.click(
            elements(), basepage.find_ele_ele(
                basepage(self.driver), [By.CSS_SELECTOR, By.XPATH],
                ["div.ant-menu-submenu-title>span",
                 "//span[text()='商品管理']"]))

        '''
        使用 JavaScript 脚本进行 selenium 无法进行的点击操作
        '''
        elements().js_script_click(
            self.driver,
            basepage.find_ele_ele(
                basepage(self.driver), [By.CSS_SELECTOR, By.XPATH],
                ["a.router-link-active[target='商品信息']",
                 "//span[text()='商品信息']"]))

        elements().js_script_click(
            self.driver,
            basepage.find_ele_ele(
                basepage(self.driver), [By.CSS_SELECTOR, By.XPATH],
                ["button.ant-btn-primary",
                 "//span[text()='新增']"]))

        funtion.introjs_skip_button(funtion(self.driver))

        elements.keys(elements(), basepage.find_ele(
            basepage(self.driver), By.CSS_SELECTOR,
            "span.ant-form-item-children>input[id='name']"), name)

        elements.keys(elements(), basepage.find_ele(
            basepage(self.driver), By.CSS_SELECTOR,
            "div.ant-col-lg-15>input[id='unit']"), "100")

        value_elements = basepage.find_ele(
            basepage(self.driver), By.CSS_SELECTOR,
            "div.td>label>input[placeholder='请输入条码']")

        elements.clear(elements(), value_elements)

        elements.keys(elements(), value_elements, value)

        funtion.save_button(
            funtion(self.driver),
            [By.CSS_SELECTOR, By.XPATH],
            ["div.ant-modal-footer>button.ant-btn-primary",
             "//span[text()='确 定']"])
