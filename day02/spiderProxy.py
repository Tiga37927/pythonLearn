#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: spiderProxy.py 
@time: 2017/7/17 10:54 
"""
import urllib2
import random

url = "http://www.baidu.com/"
https = [
    {"http": "58.252.6.165:9000"},
    {"http": "58.252.6.165:9000"},
]

proxySwitch = True

http_proxy_handle = urllib2.ProxyHandler(random.choice(https))
null_proxy_handle = urllib2.ProxyHandler({})

if proxySwitch:
    opener = urllib2.build_opener(http_proxy_handle)
else:
    opener = urllib2.build_opener(null_proxy_handle)

request = urllib2.Request(url)

# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# urllib2.install_opener(opener)
# response = urlopen(request)
response = opener.open(request)

print response.read()
