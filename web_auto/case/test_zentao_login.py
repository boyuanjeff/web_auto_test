#coding:utf-8

from selenium import webdriver
from time import sleep
import unittest


class LoginTest(unittest.TestCase):
    '''登录类的案例'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    def setUp(self) -> None:

        self.driver.get("http://127.0.0.1/zentao/user-login.html")
        self.is_alert_exist()
        self.driver.delete_all_cookies()#清空cookies
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def get_login_username(self):
        try:
            sleep(2)
            t = self.driver.find_element_by_css_selector("#userMenu > a").text
            print(t)
            return t
        except:
            return ""

    def is_alert_exist(self):
        '''判断alert是不是在'''
        try:
            sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()#有 alert 点alert
        except:
            return ""

    def login(self,user,psw):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()
    def test_01(self):
        '''登陆成功的案例'''
        sleep(2)
        self.login("admin","123456")
        sleep(2)
        t = self.get_login_username()
        print("获取登录的结果：%s"%t)
        self.assertTrue(t == "admin")
    def test_02(self):
        '''登陆失败的案例'''
        sleep(2)
        self.login("admin1","")
        sleep(2)

        t = self.get_login_username()
        print("登陆失败，获取的结果：%s"%t)
        # self.assertTrue(t == "")
        self.assertTrue(1==2)#断言失败截图
if __name__ == '__main__':
    unittest.main()