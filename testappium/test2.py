from appium import webdriver
import unittest, time


class AppTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['version'] = '8.0.0'
        desired_caps['deviceName'] = 'MI 6'
        desired_caps['app'] = 'C:\\Users\\gongzhiyong\\Desktop\\174029.apk'
        desired_caps['appPackage'] = 'com.baidu.searchbox'
        desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'
        # 解决无法输入中文问题
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)
    def swipeUp(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(1 / 2 * x, 3 / 4 * y, 1 / 2 * x, 1 / 2 * y, 1000)
    def test_serach(self):
        time.sleep(5)
        # 点击关闭浮窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(5)
        # 获取屏幕宽和高
        self.swipeUp()
        time.sleep(5)
        # 点击输入框
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.baidu.searchbox:id/baidu_searchbox').click()
        # 输入框输入test，点击搜索按钮
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.baidu.searchbox:id/SearchTextInput').send_keys("测试")
        self.driver.find_element_by_id('com.baidu.searchbox:id/float_search_or_cancel').click()

        time.sleep(5)
        # 获取屏幕宽和高
        self.swipeUp()
        time.sleep(10)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main()
