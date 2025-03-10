from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fun.zero.li.Website.test_case.funtion import funtion
from fun.zero.li.Website.test_case.Elements import elements
from fun.zero.li.Website.test_case.BasePage import basepage


class purchase_orderpage(basepage):
    def purchase_order(self, vendor, barcodes, quantity, price):
        elements.click(
            elements(), basepage.find_ele_ele(
                basepage(self.driver), [By.CSS_SELECTOR, By.XPATH],
                ["div.ant-menu-submenu-title>span",
                 "//span[text()='采购管理']"]))

        elements().js_script_click(
            self.driver,
            basepage.find_ele_ele(
                basepage(self.driver),
                [By.CSS_SELECTOR, By.XPATH],
                ["a.router-link-active[target='采购入库']",
                 "//span[text()='采购入库']"]))

        elements().js_script_click(
            self.driver,
            basepage.find_ele_ele(
                basepage(self.driver),
                [By.CSS_SELECTOR, By.XPATH],
                ["button.ant-btn-primary",
                 "//span[text()='新增']"]))

        funtion.introjs_skip_button(funtion(self.driver))

        elements().js_script_click(
            self.driver,
            basepage.find_ele_ele(
                basepage(self.driver),
                [By.CSS_SELECTOR, By.XPATH],
                ["div.ant-select-selection>div.ant-select-selection__rendered",
                 "//div[text()='选择供应商']"]))


        # elements().js_script_click(
        #     self.driver,
        #     basepage.find_ele(
        #         basepage(self.driver),
        #         By.XPATH,
        #         "//div[text()='选择供应商']/parent::div/parent::div/span[@class='ant-select-arrow']"
        #     ))
        #
        # elements_list = basepage.find_eles_list(basepage(self.driver), By.CSS_SELECTOR, "ul.ant-select-dropdown-menu")
        # for e in elements_list:
        #     if e.text == vendor:
        #         elements().js_script_click(self.driver, e)

        sleep(1)

        elements().js_script_value(
            vendor, self.driver,
            basepage.find_ele_ele(
                basepage(self.driver),
                [By.ID, By.CSS_SELECTOR],
                ["organId",
                 "div>div>div.ant-select-search--inline>div>input"]))

        funtion.key_enter(
            funtion(self.driver),
            [By.ID, By.CSS_SELECTOR],
            ["organId",
             "div>div>div.ant-select-search--inline>div>input"])

        elements().js_script_click(self.driver, basepage.find_ele_ele(
            basepage(self.driver),
            [By.CSS_SELECTOR, By.XPATH],
            ["button.ant-btn", "//span[text()='扫码录入']"]
        ))

        elements().keys(basepage.find_ele(
            basepage(self.driver), By.CSS_SELECTOR, "div.ant-col-md-16>input[placeholder='请扫描商品条码并回车']"
        ), barcodes)

        elements().keys(basepage.find_ele(
            basepage(self.driver), By.CSS_SELECTOR, "div.ant-col-md-16>input[placeholder='请扫描商品条码并回车']"
        ), Keys.ENTER)

        sleep(1)

        elements().js_script_value(quantity, self.driver, basepage.find_eles(
            basepage(self.driver), By.CSS_SELECTOR,
            "div.tr[data-idx='0']>div>label>input[data-input-number='true']",
            0
        ))

        elements().js_script_value(price, self.driver, basepage.find_eles(
            basepage(self.driver), By.CSS_SELECTOR,
            "div.tr[data-idx='0']>div>label>input[data-input-number='true']",
            1
        ))

        sleep(10)

        funtion.save_button(

            funtion(self.driver),
            [By.CSS_SELECTOR, By.XPATH],
            ["div.ant-modal-footer>button.ant-btn",
             "//span[text()='保 存']"])
