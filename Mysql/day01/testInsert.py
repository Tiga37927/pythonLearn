#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: testInsert.py 
@time: 2017/7/21 13:52 
"""
from MysqlHelper import *


mysqlHelper = MysqlHelper('localhost', 3306, 'python', 'root', 'root')

# 测试插入
# sql = 'insert into students(sname,gender) values(%s,%s)'
# sname = raw_input("请输入姓名：")
# gender = raw_input("请输入性别，1为男，0为女")
# params = [sname, bool(gender)]
# count = mysqlHelper.insert(sql, params)
# if count==1:
#     print 'ok'
# else:
#     print 'error'

# 测试查询
sql = 'select sname,gender from students order by id desc'
one = mysqlHelper.get_one(sql)
print one




