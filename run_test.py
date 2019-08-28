from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='baidu*.py')
nowtime=time.strftime("%Y-%m-%d %H:%M:%S")
filename='./'+nowtime+'.html'
fp=open(filename,'wb')
runner=HTMLTestRunner(stream=fp,title='百度搜索',description='the report of baidu-search')
runner.run(discover)
fp.close()