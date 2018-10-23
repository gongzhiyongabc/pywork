from selenium import webdriver
from threading import Thread
from time import ctime, sleep

def test_baidu(browser, search):
    print("开始时间%s"%ctime())
    print("browser是%s" %browser)
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'ff':
        driver = webdriver.Firefox()
    else:
        print("browser参数有误")

    driver.get('http://wwww.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()

if __name__ == "__main__":
    # 启用参数
    lists = {'chrome':'web', 'ie':'webdriver', 'ff':'threading'}
    files = range(len(lists))
    threads = []
    # 创建线程
    for browser,search in lists.items():
        t = Thread(target=test_baidu, args=(browser, search))
        threads.append(t)
    #启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

    print("end:%s"%ctime())
