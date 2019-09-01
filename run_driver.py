from selenium.webdriver import Remote
from threading import Thread
import time
import unittest
import warnings
from selenium import webdriver



def run_driver():
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='driver.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)



run_driver()
run_driver()


# test_dir='./'
# discover=unittest.defaultTestLoader.discover(test_dir,pattern='driver.py')
# runner=unittest.TextTestRunner()
# runner.run(discover)
