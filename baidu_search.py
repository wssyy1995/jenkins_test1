from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner



class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://www.baidu.com")


    def test_baidu_search1(self):

        self.driver.find_element_by_id('kw').send_keys('jenkins_test1')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        print(self.driver.title)
        self.assertEqual(self.driver.title,'jenkins_test1_百度搜索')

    def test_baidu_search2(self):

        self.driver.find_element_by_id('kw').send_keys('jenkins_test2')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        print(self.driver.title)
        self.assertEqual(self.driver.title,'jenkins_test2_百度搜索')

    def test_baidu_search3(self):

        self.driver.find_element_by_id('kw').send_keys('jenkins_test3')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        print(self.driver.title)
        self.assertEqual(self.driver.title,'jenkins_test2_百度搜索')

    def tearDown(self):
        self.driver.quit()

