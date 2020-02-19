#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: test_add_bug.py 
@time: 2020/02/14 
"""
from selenium import webdriver
from pages.add_bug_page import ZenTaoBug
from pages.login_page import Login
import unittest
import time
class Test_Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.bug = ZenTaoBug(cls.driver)
        cls.a = Login(cls.driver)
        cls.a.login()#用例前登陆
    def test_add_bug(self):

        timestr = time.strftime("%Y_%m_%d_%H_%m_%S")
        title = "测试提交BUG" + timestr
        self.bug.add_bug(title)

        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()