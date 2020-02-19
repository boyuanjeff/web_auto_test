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
import ddt
from common.read_excel import ExcelUitil
import os
'''
1、输入admin输入123456，，点登陆 期望结果：
2、输入admin输入        ，点登陆
3、输入admin111输入123456，，点保持登录，点登陆
'''
# 测试数据源
# testdates = [
#     {"user":"admin","psw":"123456","expect":"admin"},
#     {"user": "admin", "psw": "", "expect":""},
#     {"user": "admin123", "psw": "123456", "expect":""},
# ]
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

filepath = os.path.join(propath,"common","datas1.xlsx")
print(filepath)

data = ExcelUitil(filepath)
testdates = data.dict_data()
print(testdates)
@ddt.ddt
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

    def login_case(self,user,psw,expect):

        self.loginp.login(user,psw,expect)
        result = self.loginp.get_login_result(user)
        if expect=="True":expect_result = True
        else:expect_result = False
        print("测试结果：%s"%result)
        self.assertTrue(result == expect_result)

    @ddt.data(*testdates)
    def test_01(self,data):
        '''输入admin输入123456，，点登陆'''
        print("----------开始测试----------")
        print("测试数据%s"%data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("----------结束测试----------")
    # def test_02(self):
    #     '''输入admin输入        ，点登陆'''
    #     print("----------开始测试：test_02----------")
    #     data2 = testdates[1]
    #     print("测试数据%s"%data2)
    #     self.login_case(data2["user"],data2["psw"],data2["expect"])
    #     print("----------结束测试：test_02----------")
    # def test_03(self):
    #     '''输入admin111输入123456，，点保持登录，点登陆'''
    #     print("----------开始测试：test_03----------")
    #     data3 = testdates[2]
    #     print("测试数据%s"%data3)
    #     self.login_case(data3["user"],data3["psw"],data3["expect"])
    #     print("----------结束测试：test_03----------")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()