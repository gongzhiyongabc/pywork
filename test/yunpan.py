from selenium import webdriver
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.hrome()
driver.get("http://yunpan.360.cn")

#……
#定位到要右击的元素
right_click= driver.find_element_by_id("xx")
#定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()
#……

#定位到要悬停的元素
above = driver.find_element_by_id("id")
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

#定位到要双击的元素
double_click = driver.find_element_by_id('xx')
#对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()

#定位元素的原位置
element = driver.find_element_by_id('xx')
#定位元素要移动到的目标位置
target = driver.find_element_by_id('xx')

#执行元素的拖动操作
ActionChains(driver).drag_and_drop(element, target).perform()

