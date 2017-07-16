# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: spider_ajax.py
@time: 2017/7/16 10:47
"""
import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}

formdata = {
    "start": "0",
    "limit": "20",
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=header)

response = urllib2.urlopen(request)

with open("movie.json", 'w+') as f:
    f.write(response.read())

print "*" * 30
