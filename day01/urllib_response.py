# encoding: utf-8
import urllib2
url = "http://www.baidu.com/"
# User-agent是应对反爬虫的第一步
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
request = urllib2.Request(url, headers=ua_headers)
response = urllib2.urlopen(request)
# urlopen 不支持构造，指定了发送的请求的user-agent：python2.7
# response = urllib2.urlopen("http://www.baidu.com/")
# 服务器返回的类文件对象支持python文件对象的操作方法，read就是读取内容，返回字符串
# 可以查看响应状态码
print response.getcode()
# 返回实际url，防止重定向
print response.geturl()
# 返回相应信息
print response.info()

html = response.read()
# 打印响应内容
print html

