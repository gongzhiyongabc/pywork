from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://videojs.com")

# driver.implicitly_wait(20)
video = driver.find_element_by_xpath("//*[@id='preview-player']/button")

#返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()",video)

#播放15秒钟
sleep(15)

#暂停视频
print("stop")
driver.execute_script("arguments[0].pause()",video)

driver.quit()
