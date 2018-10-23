from selenium import webdriver
driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# #参数数字为像素点
# print("设置浏览器宽度480，高800显示")
# driver.set_window_size(480, 800)


#访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s"%(first_url))
driver.get(first_url)

driver.refresh()
#访问新闻首页
second_url = 'http://news.baidu.com'
print("now access %s"%(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to %s"%(first_url))
driver.back()

#前进到新闻页
print("forword to %s"%(second_url))
driver.forward()

driver.quit()