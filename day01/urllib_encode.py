# encoding: utf-8
import urllib
import urllib2

url = "http://www.baidu.com/s"
# py3里面接受输入数据用input
keyword = raw_input("请输入要查询的字符串：")

wd = {"wd": keyword}
# 使用urllib的urlecode方法转码，接受的参数是一个字典类型
world = urllib.urlencode(wd)

print world

full_url = url + "?" + world

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

request = urllib2.Request(full_url, headers=headers)
# 发送
response = urllib2.urlopen(request)

print urllib.unquote(world)
# print response.read()

