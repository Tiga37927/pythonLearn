#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: python-sql.py 
@time: 2017/7/21 11:01 
"""
import MySQLdb

host = "localhost"
port = 3306
db = "python"
user = "root"
password = "root"
charset = "utf8"

try:
    # 创建连接
    conn = MySQLdb.connect(host=host,port=port,db=db,user=user,passwd='root',charset=charset)
    # 建立cursor对象，用于执行sql语句并获得结果
    cs1 = conn.cursor()
    # 执行语句，返回受影响的行数
    # 插入一条数据
    # count = cs1.execute("insert into students(sname, gender) values('张良', 1)")
    # 删除一条数据
    # count = cs1.execute("delete from students where id=3")
    # 修改一条数据
    # count = cs1.execute("update students set sname='刘邦' where id=5")
    # print count
    # 参数化查询
    # sname = raw_input("请输入学生姓名：")
    # params = [sname]
    cs1.execute("select sname,gender from students order by id desc")
    result = cs1.fetchone()
    print result

    # 执行查询语句是返回第一行数据，返回一个元组
    # fetchone = cs1.fetchone()
    # print fetchone

    # 提交事务
    # conn.commit()
    # 关闭操作
    cs1.close()
    # 关闭连接
    conn.close()
except Exception,e:
    print e.message
