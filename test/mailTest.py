from selenium import webdriver
from public import Login

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.126.com")

#调用登录模块
Login().user_login(driver)

#……

#调用退出模块
Login().user_logout(driver)