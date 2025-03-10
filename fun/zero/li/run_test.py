import HTMLTestRunner_PY3
import os
import unittest

if __name__ == '__main__':
    suit = unittest.TestSuite()
    loader = unittest.defaultTestLoader.discover(start_dir="Website", pattern="*.py")
    suit.addTest(loader)
    html_path = os.path.join(os.getcwd(), "Website\\test_report\\collection_test.html")
    with open(html_path, "wb") as html:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=html, title="Collection_test", description="erp 功能测试")
        runner.run(suit)
