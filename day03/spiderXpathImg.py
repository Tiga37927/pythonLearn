#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: spiderXpathImg.py 
@time: 2017/7/18 14:54 
"""
import os
import urllib2
from lxml import etree
import re
import time

class Spider:
    def __init__(self):
        self.url = "http://www.neihan.net/pic/pic_"
        self.ua_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }

        self.page = 1
        self.switch = True

    def loadPage(self):
        """
        加载页面
        :return:
        """
        url = self.url + str(self.page) + ".html"
        request = urllib2.Request(url, headers=self.ua_header)
        response = urllib2.urlopen(request)
        html = response.read()
        self.loadImages(etree.HTML(html))

    def loadImages(self, html):
        """
        选取图片处理
        :param html:
        :return:
        """
        imagelinks = html.xpath('//dd[@class="content content-pic"]/p/img/@src')
        for imagelink in imagelinks:
            path = r'./images/'
            self.mkdir(path)
            self.writeImage(path, imagelink)

    def writeImage(self, path, imagelink):
        """
        保存图片
        :param imagelink:
        :return:
        """
        pattern = re.compile(r'[\d]{12}.+')
        imagename = pattern.search(imagelink).group()

        file = open(path + str(imagename), 'wb')
        images = urllib2.urlopen('http://www.neihan.net/' + imagelink).read()
        file.write(images)
        file.close()

    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print u"偷偷新建了名字叫做", path, u'的文件夹'
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print u"名为", path, '的文件夹已经创建成功'
            return False

    def startSpoider(self):
        while self.switch:
            self.loadPage()
            command = raw_input("继续抓取图片按回车，取消输入quit")
            if command == 'quit':
                self.switch = False
            self.page += 1
        print "谢谢使用"

if __name__ == "__main__":
    imageSpider = Spider()
    imageSpider.startSpoider()