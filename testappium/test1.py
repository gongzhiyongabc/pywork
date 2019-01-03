# -*- coding:utf-8 -*-


import  unittest
from appium import webdriver

class AppTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'MI 6'
        desired_caps['app'] = 'C:\\Users\\gongzhiyong\\Desktop\\174029.apk'
#       desired_caps['noReset'] = False
#       desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps['appPackage'] = 'com.baidu.searchbox'
        desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'

        self.wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(60)

    def test_login(self):
        pass

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

