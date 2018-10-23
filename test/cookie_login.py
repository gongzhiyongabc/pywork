from selenium import webdriver
#访问xx网站
driver = webdriver.Chrome()
driver.get("http://wwww.xx.cn")

#将用户名密码写入浏览器的cookie
driver.add_cookie({'name':'Login_UserNumber','value':'username'})
driver.add_cookie({'name':'Login_Passwd','value':'password'})
#再次访问xx网站，将会自动登录
driver.get('http://www.xx.cn')
#……

driver.quit()