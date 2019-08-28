from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


test_dir='./'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='baidu*.py')
nowtime=time.strftime("%Y-%m-%d %H:%M:%S")
# filename=test_dir+nowtime+'.html'
filename='./report/'+nowtime+'.html'
fp=open(filename,'wb')
runner=HTMLTestRunner(stream=fp,title='baidutest',description='the report of baidu-search')
runner.run(discover)
fp.close()