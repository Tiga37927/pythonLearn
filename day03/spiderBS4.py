#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: spiderBS4.py 
@time: 2017/7/18 16:04 
"""
from bs4 import BeautifulSoup
import urllib2
#
# url = "http://www.baidu.com/"
# response = urllib2.urlopen(url)
#
# html = response.read()

soup = BeautifulSoup(open("hello.html"), 'lxml')
# 获取标签文字内容
# print soup.a.string
print soup.li.a['href']