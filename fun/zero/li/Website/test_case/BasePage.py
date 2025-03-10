class basepage:
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, by, value):
        return self.driver.find_element(by, value)

    def find_eles(self, by, value, num):
        return self.driver.find_elements(by, value)[num]

    def find_eles_list(self, by, value):
        return self.driver.find_elements(by, value)

    def find_ele_ele(self, by, value):
        return self.driver.find_element(by[0], value[0]).find_element(by[1], value[1])
