from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

#获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

#获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

#进入注册窗口
for handle in all_handles:
    if handle !=sreach_windows:
        driver.switch_to.window(handle)
        print('now register window')
        driver.find_element_by_name('accent').send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
        time.sleep(2)


#回到搜索窗口
for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to.window(handle)
        print('now sreach window!')
        driver.find_element_by_id('TANGRAM_PSP_2_closeBtn').click()
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(2)



driver.quit()