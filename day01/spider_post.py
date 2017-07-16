# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence
@file: request_post.py
@time: 2017/7/15 19:40
"""
import urllib
import urllib2

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"

key = raw_input("请输入要翻译的文字：")

ua_headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With" : "XMLHttpRequest",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
}

formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1500172955440",
    "sign": "95657175fc4286bb138c57c80c680963",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CL1CKBUTTON",
    "typoResult": "true",
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=ua_headers)
response = urllib2.urlopen(request)

print urllib2.urlopen(request).read()
