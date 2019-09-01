from selenium.webdriver import Remote
from threading import Thread
import time
import unittest
import warnings
from selenium import webdriver
# driver=Remote(command_executor='http://192.168.39.102:6666/wd/hub',desired_capabilities={'platform':'ANY','browserName':'chrome','version':'','javascriptEnabled':True})
# driver=Remote(command_executor='http://192.168.39.102:5555/wd/hub',desired_capabilities={'platform':'ANY','browserName':'firefox','version':'','javascriptEnabled':True})
# def driver(ip,bro):
#     driver=Remote(command_executor='%s/wd/hub'%(ip),desired_capabilities={'platform':'ANY','browserName':'%s'%(bro),'version':'','javascriptEnabled':True})
#     return driver

# def open_url(driver):
#     driver.get('http://www.baidu.com')
#     time.sleep(1)
#     driver.quit()
from driver_def import d



class Baidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = d()
        warnings.simplefilter("ignore", ResourceWarning)
        print('start create browser')
        cls.driver.implicitly_wait(5)


    def test_baidu_search1(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('jenkins_test1')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.assertEqual(self.driver.title,'jenkins_test1_百度搜索')
        print(self.driver.title)

    def test_baidu_search2(self):
        self.driver.get("http://www.baidu.com")
        time.sleep(1)
        self.driver.find_element_by_id('kw').send_keys('jenkins_test2')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.assertEqual(self.driver.title,'jenkins_test2_百度搜索')
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


#
#
# d=webdriver.Chrome()
#
# test_dir='./'
# discover=unittest.defaultTestLoader.discover(test_dir,pattern='driver.py')
# runner=unittest.TextTestRunner()
# runner.run(discover)


#
# threads=[]
#
# driver_list={'http://192.168.39.102:6666':'chrome','http://192.168.39.102:5555':'firefox'}



# for host,browser in driver_list.items():
#     d=driver(host,browser)
#     d.implicitly_wait(5)
#     unittest.main()



#
# for host,browser in driver_list.items():
#     d=driver(host,browser)
#     d.implicitly_wait(5)
#     t=Thread(target=test_baidu,args=(d,))
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()



