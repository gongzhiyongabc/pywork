from selenium.webdriver import Remote

# 定义主机与浏览器
lists = {'http://127.0.0.1:4444/wd/hub': 'chrome', 'http://127.0.0.1:5555/wed/hub': 'firefox',
         'http://127.0.0.1:5556/wd/hub': 'internet explorer'}
# 通过不同的浏览器执行脚本
for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host,
                desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                      'javascriptEnabled': True})
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    driver.quit()
