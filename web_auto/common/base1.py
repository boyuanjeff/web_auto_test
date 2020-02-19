#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: base.py 
@time: 2020/02/14 
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Base():

    def __init__(self,driver:webdriver.Chrome):#映射
        self.driver = driver
        self.timeout = 2
        self.t = 0.5
        self.driver.maximize_window()

    def findElementNew(self,locator):
        '''定位到元素，返回元素对象，没定位到，timeout异常'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","value1")')
        else:
            print("正在定位元素信息：定位方式→%s，value→%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele
    def findElement(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","value1")')
        else:
            print("正在定位元素信息：定位方式→%s，value→%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele
    def findElements(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","value1")')
        else:
            print("正在定位元素信息：定位方式→%s，value→%s"%(locator[0],locator[1]))
            try:
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
                return eles
            except:
                return []

    def sendKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        '''判断元素是否而被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self,locator):
        '''判断元素是否存在'''
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def isElementExists(self,locator):
        '''定位一组元素'''
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def is_title(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False
    def is_title_contains(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False
    def is_text_in_element(self,locator,_text):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        '''返回bool值，空字符串返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        '''判断alert是否存在，存在返回alert对象，不存在返回False'''

        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False


    def get_title(self):
        '''获取title'''
        return self.driver.title
    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回'' ")
            return ""

    def get_attribute(self, locator, name):
        '''获取属性'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回'' "%name)
            return ""

    def move_to_element(self,locator):
        '''鼠标悬停'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    '''============定位select============'''
    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几次，从0开始，默认选第一个'''
        element = self.findElement(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)


    def select_by_text(self,locator,text):
        '''通过text属性'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    '''============JS============'''
    def js_focus_element(self,locator):
        '''聚集元素-----页面到指定元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/zentao/user-login.html")
    zentao = Base(driver)
    locl1 = (By.ID, "account")
    locl2 = (By.NAME,"password")
    locl3 = (By.ID, "submit")
    # zentao.findElement(locl1).send_keys("admin")
    zentao.sendkeys(locl1,"admin")
    zentao.sendkeys(locl2,"123456")
    zentao.click(locl3)