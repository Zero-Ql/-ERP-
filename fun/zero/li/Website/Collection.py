import unittest
import os
from time import sleep

from ddt import ddt, data

from selenium import webdriver
from fun.zero.li.Website.test_data.csv_data import csv_data
from fun.zero.li.Website.test_case.LoginPage import loginpage
from fun.zero.li.Driver.Driver import driver
from fun.zero.li.Website.test_case.Product_informationPage import product_informationPage
from fun.zero.li.Website.test_case.Purchase_orderPage import purchase_orderpage


@ddt
class Collection(driver):
    csv_path1 = os.path.join(os.path.dirname(__file__), "test_data/data1.csv")
    csv_path2 = os.path.join(os.path.dirname(__file__), "test_data/data2.csv")

    csv_data1 = csv_data.get_data1(csv_path1)
    csv_data2 = csv_data.get_data2(csv_path2)

    # for c in csv:
    #     c['username'] = "xtgly"
    #     c['password'] = "123456"

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome()
        super(Collection, cls).setUp(cls.driver, url="http://43.139.75.249:3000/user/login", time=5)
        loginpage().login(cls.driver, "xtgly", "123456")
        cls.product_information = product_informationPage(cls.driver)
        cls.purchase_order = purchase_orderpage(cls.driver)

    @data(*csv_data1)
    def test_01(self, data_list):
        self.product_information.product_information(data_list['key'], data_list['value'])
        sleep(2)

    # @data(*csv_data2)
    # def test_02(self, data_list):
    #     self.purchase_order.purchase_order(
    #         data_list['vendor'], data_list['barcodes'],
    #         data_list['quantity'], data_list['price'])
    #     sleep(2)

    @classmethod
    def tearDown(cls) -> None:
        super(Collection, cls).tearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2)
