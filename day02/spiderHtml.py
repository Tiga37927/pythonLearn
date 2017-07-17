#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: spiderHtml.py 
@time: 2017/7/17 17:31 
"""
import re
import urllib2

class Spider:
    def __init__(self):
        # 初始化起始页
        self.page = 3
        # 爬虫开关
        self.switch = True
    def loadPage(self):
        """
        下载页面
        :return:
        """
        url = "http://www.neihan.net/text_" + str(self.page) + ".html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        # 每页的html是字符串
        html = response.read()

        # 创建正则表达式对象，匹配文章内容，re.S表示匹配全文
        pattern = re.compile(r'<dd\sclass="content">(.*?)</dd>', re.S)
        # 返回匹配的内容
        content_list = pattern.findall(html)
        # 保存
        print content_list
        self.dealPage(content_list)
    def dealPage(self, content_list):
        """
        处理每个段子
        :return:
        """
        for item in content_list:
            # self.writePage(item)
            print item
    def writePage(self, item):
        """
        把段子逐个写入文件
        :return:
        """
        with open('duanzi.txt', 'a') as f:
            f.write(item)
    def startWork(self):
        """
        爬虫控制
        :return:
        """
if __name__ == "__main__":
    daunziSpider = Spider()
    daunziSpider.loadPage()
