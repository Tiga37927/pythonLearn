# encoding: utf-8

"""
@version: ??
@author: young
@license: Apache Licence 
@file: spiderHandle.py
@time: 2017/7/16 19:52
"""
import urllib2

http_handler = urllib2.HTTPHandler(debuglevel=1)

https_handler = urllib2.HTTPSHandler(debuglevel=1)

opener = urllib2.build_opener(http_handler)

url = "http://www.baidu.com/"

request = urllib2.Request(url)

response = opener.open(request)

print response.read()