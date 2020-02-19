#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: test_add_bug_case.py 
@time: 2020/02/18 
"""

from selenium import webdriver
import unittest
from pages.login_page import LoginPage
from pages.add_bug_page import AddBugPage
import time

my = "http://127.0.0.1/zentao/my/"
class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.bug = AddBugPage(cls.driver)
        a = LoginPage(cls.driver)
        a.login()
    def setUp(self) -> None:
        self.driver.get(my)


    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%m_%S")
        title = "测试提交BUG" + timestr
        self.bug.add_bug(title)

        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    def test_add_bug2(self):
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