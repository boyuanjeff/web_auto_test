#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: run_all.py 
@time: 2020/02/14 
"""
import unittest
from common import HTMLTestRunner_cn
#discover可以遍历查找相同的文件
# start_dir：查找用例的目录
# pattern='test*.py',：匹配规则
# top_level_dir=None顶层目录

casePath = "E:\\web_auto\\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath = "E:\\web_auto\\report\\"+"report.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream = fp,#报告存放地址
                                          title = u'测试报告',#报告名称
                                          description = u'用例执行情况：',#描述
                                          retry=1)#断言失败则重跑一次


runner.run(discover)

fp.close()