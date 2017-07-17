#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: spiderSession.py 
@time: 2017/7/17 14:10 
"""
import urllib
import urllib2
import cookielib
import time

url = "http://eoms.17cai.com/qc-invoicing/powermgr/login"
# headers = {
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     # "Accept-Encoding":"gzip, deflate",
#     "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
#     "Cache-Control":"max-age=0",
#     "Connection":"keep-alive",
#     "Cookie":"ipLocation=%u5E7F%u4E1C; ipLoc-djd=CN-44%23CN-44-SZ%23CN-44-SZ-NS%230; gr_user_id=05d474ea-f80b-460d-b161-5b0ac94e6940; Hm_lvt_aeb4c875bbbab774b39139245b0ddb83=1499737164,1499825868,1499853252,1500003466; JSESSIONID=ED98D3AAC781A0AC2CE9F095ED4C34EA.jvm21.jvm21; gr_session_id_b7dc155e081be945=de322dcf-1887-42a5-bb94-08019385aca2; gr_cs1_de322dcf-1887-42a5-bb94-08019385aca2=party_id%3A10245; Hm_lvt_1ca60822772f025a4b04f248f27c4ae8=1499844091,1499844993,1499844999,1500257794; Hm_lpvt_1ca60822772f025a4b04f248f27c4ae8=1500271344",
#     "Host":"www.17cai.com",
#     "Referer":"http://www.17cai.com/control/checkSsoLogin?service=http%3A%2F%2Fwww.17cai.com%2Fcontrol%2FmyOrderList",
#     "Upgrade-Insecure-Requests":"1",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
# }

# 构建cookiejar对象保存访问站点的cookie
cookie = cookielib.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器对象，参数为cookiejar对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookie_handler)
# addheaders接受一个列表，里面每个元素都是一个信息的元祖
opener.add_handler = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")]
# 设置登录密码
data = {
    "selfPhone": "18710611750",
    "passWord": "123456"
}
# 转码
postdata = urllib.urlencode(data)

request = urllib2.Request(url, data=postdata)

response = opener.open(request)
# time.sleep(30)
response_deng = opener.open("http://eoms.17cai.com/qc-invoicing/product/getProductList")

## 可以按标准格式将保存的Cookie打印出来
# cookieStr = ""
# for item in cookiejar:
#     cookieStr = cookieStr + item.name + "=" + item.value + ";"

## 舍去最后一位的分号
print response_deng.read()
