#!/usr/bin/env python
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: spiderRe.py
@time: 2017/7/17 15:45 
"""
# python里正则匹配默认贪婪模式，至少匹配一次
# re.I表示忽略大小写，re.S表示全文匹配
import re

# pattern = re.compile(r"\d+")

# m = pattern.match(r"aaa123", 3, 6)
#  m = pattern.search(r"aaa 123 123456 123")
# print m.group(0)
# print m.span()
# m = pattern.findall(r"aaa 123 123456 123")
# print m

# m = pattern.finditer(r"aaa 123 123456 123")
# for i in m:
#     print i.group()

# pattern = re.compile("[\s\d\\\;]+")
# m = pattern.split(r" abc\123; dd 123 cc")
# print m

# sub方法是替换,这里的正则是分组的意思，分两组，会按空格分开，从开始匹配
# pattern = re.compile(r"(\w+) (\w+)")
# str = "hello 123456, xxx ddd"
# m = pattern.sub(r"\1 \2", str)
# print m
pattern = re.compile(r'[\d]{12}.+')
str = "/Uploads/joke/2017/6183/baoxiao/201706183794.png"
m = pattern.search(str)
print m.group()
