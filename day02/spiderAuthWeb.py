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

user = "18710611750"
password = "yx404414"

url = "http://www.17cai.com/control/myOrderList/"

# 构建一个密码管理对象
passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# 域，站点、账户、密码
passwordMgr.add_password(None, url, user, password)

http_auth_handler = urllib2.HTTPBasicAuthHandler(passwordMgr)

opener = urllib2.build_opener(http_auth_handler)

request = urllib2.Request(url)

# response = opener.open(request)
response = urllib2.urlopen(url)
print response.read()
