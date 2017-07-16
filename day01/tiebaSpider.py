# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence
@file: tiebaSpider.py
@time: 2017/7/15 19:40
"""
import urllib
import urllib2
import random

def loadPage(url, filename):
    """
        :return:：根据url发送请求，获取服务器响应文件
        :param 需要爬取的url地址
        filename: 处理的文件名
    """
    print "正在下载" + filename

    ua_headers = [
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
        {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    ]
    ua_headers = random.choice(ua_headers)
    request = urllib2.Request(url, headers=ua_headers)
    response = urllib2.urlopen(request)
    return response.read()

def writePage(html, filename):
    """
    :param html: 服务器响应内容
    :return: 将服务器内容写到本地
    """
    print "正在保存" + filename
    # 这种写法不用关闭
    path = r"E:/python爬虫/day01/" + filename
    # 2.版本对中文编码支持不够
    uipath = unicode(path, "utf8")
    with open(uipath, 'wb') as f:
        f.write(html)
    print "-" * 20

def tiebaSpider(url, beginPage, endPage):
    """
    :param url:
    :param beginPage:
    :param endPage:
    :return:
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print fullUrl
        # 调用loadPage发送请求获取html页面
        html = loadPage(fullurl, filename)
        writePage(html, filename)
        print "谢谢使用"

# python执行顺序是自上而下的，又因为缩进的关系，没有缩进的代码将在载入时自动执行
# 为了区分主执行文件还是被调用的文件，python引入__name__变量
# __name__的值为模块名，当文件被执行时，__name__为‘__main__’
if __name__ == "__main__":
    kw = raw_input("请输入贴吧名：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    url = url + key
    print url
    tiebaSpider(url, beginPage, endPage)