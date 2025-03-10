import unittest


class driver(unittest.TestCase):

    @classmethod
    def setUp(cls, driver, url, time) -> None:
        cls.driver = driver
        cls.driver.get(url)
        cls.driver.implicitly_wait(time)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()
