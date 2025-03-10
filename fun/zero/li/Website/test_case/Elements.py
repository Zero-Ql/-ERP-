class elements():
    def click(self, find):
        find.click()

    def keys(self, find, value):
        find.send_keys(value)

    def clear(self, find):
        find.clear()

    def js_script_click(self, driver, element):
        driver.execute_script("arguments[0].click();", element)

    def js_script_value(self, value, driver, element):
        driver.execute_script("arguments[0].value=arguments[1]", element, value)

    def js_script_remove(self, value, driver, element):
        driver.execute_script("arguments[0].removeAttribute(arguments[1])", element, value)
