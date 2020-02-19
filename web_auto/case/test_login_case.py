#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: test_login_case.py 
@time: 2020/02/18 
"""
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
'''
1、输入admin输入123456，，点登陆 期望结果：
2、输入admin输入        ，点登陆
3、输入admin输入123456，，点保持登录，点登陆
4、点击忘记密码
'''
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.loginp = LoginPage(cls.driver)
    def setUp(self) -> None:

        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()#清空cookies
        self.driver.refresh()
    def test_01(self):
        '''输入admin输入123456，，点登陆'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("123456")
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == "admin")
        #断言

    def test_02(self):
        '''输入admin输入        ，点登陆'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("")
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == "")
        #断言

    def test_03(self):
        '''输入admin输入123456，，点保持登录，点登陆'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("123456")
        self.loginp.click_keep_login()
        self.loginp.click_login_button()
        result =self.loginp.get_login_name()
        self.assertTrue(result=="admin")
        #断言

    def test_04(self):
        '''点击忘记密码'''
        # self.loginp.input_user("admin")
        # self.loginp.input_psw("123456")
        # self.loginp.click_keep_login()
        # self.loginp.click_login_button()
        self.loginp.click_forget_psw()
        result =self.loginp.is_refresh_exist()
        self.assertTrue(result)
        #断言
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()