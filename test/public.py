class Login():

    #登录
    def user_login(self,driver):
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys("username")
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
    #退出
    def user_loginout(self,driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()
