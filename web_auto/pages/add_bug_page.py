#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: add_bug.py
@time: 2020/02/18
"""
from selenium import webdriver
from common.base1 import Base
# from pages.login_page import Login
import time


class AddBugPage(Base):

    # 添加bug
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_addbug = ("xpath", "// *[ @ id = 'createActionMenu'] / a")
    loc_truck = ("xpath", "// *[ @ id = 'openedBuild_chosen'] / ul")
    loc_truck_add = ("xpath", "//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id", "title")
    # 需要先切换ifram    ke-edit-iframe
    loc_input_body = ("class name", "article-content")
    loc_save = ("css selector", "#submit")

    # 新增的列表
    loc_new = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    def add_bug(self,title):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendKeys(self.loc_input_title,title)
        # 输入正文body
        frame = self.findElement(("xpath","//*[@id='dataform']/table/tbody/tr[6]/td/div[2]/div[2]/iframe"))
        self.driver.switch_to.frame(frame)#切换iframe
        # self.clear(self.loc_input_body)

        body = '''[步骤]XXXXXXX  
        [结果]XXXXXXX  
        [期望]XXXXXXX    
        '''


        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()#回到主页面
        self.js_scroll_end()
        self.click(self.loc_save)

    def is_add_bug_success(self,_text):
        return self.is_text_in_element(self.loc_new,_text)


if __name__ == '__main__':
    driver = webdriver.Chrome()

    bug = AddBugPage(driver)
    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()
    timestr = time.strftime("%Y_%m_%d_%H_%m_%S")
    title = "测试提交BUG"+timestr
    bug.add_bug(title)

    result = bug.is_add_bug_success(title)
    print(result)