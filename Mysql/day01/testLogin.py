#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: testLogin.py 
@time: 2017/7/21 14:12 
"""
from MysqlHelper import *
from hashlib import sha1

sname = raw_input("请输入用户名：")
spwd = raw_input("请输入密码：")

s1 = sha1()
s1.update(spwd)
spwdSha1 = s1.hexdigest()

sql = "select upwd from userinfos where uname=%s"
params = [sname]

sqlhelper = MysqlHelper('localhost', 3306, 'python', 'root', 'root')
userinfo = sqlhelper.get_one(sql, params)
if userinfo == None:
    print '用户名错误'
elif userinfo[0] == spwdSha1:
    print '登录成功'
else:
    print '密码错误'
