#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: spiderXpath.py 
@time: 2017/7/18 14:24 
"""
# xpath是路径匹配语言，用于在xml文档中查找信息
from lxml import etree

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
#      </ul>
#  </div>
# '''
#
# html = etree.HTML(text)
#
# result = etree.tostring(html)

# with open(r"hello.html", 'w') as f:
#     f.write(result)

html = etree.parse('hello.html')
# print type(html)
# 匹配所有li
# result = html.xpath('//li')
# print len(result)
# print type(result)
# print type(result[0])
# 选取所有li下的class属性值
# result = html.xpath('//li/@class')
# 选取所有li下属性为link1.html的a标签
# result = html.xpath('//li/a[@href="link1.html"]')
# 选取li下所有span
# result = html.xpath('//li//span')
# 选取所有li下的a的所有class
# result = html.xpath('//li/a//@class')
# 选取最后一个li的a的href
# result = html.xpath('//li[last()]/a/@href')

# 获取class职位aaa的标签
result = html.xpath('//*[@class="aaa"]')
print result[0].tag



