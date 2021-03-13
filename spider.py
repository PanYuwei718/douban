# -*- coding = utf-8 -*-
# @Time : 2021/3/12 8:25 下午
# @Author : Pan
# @Software: PyCharm

from bs4 import BeautifulSoup          #数据获取，网页解析
import re                              #正则表达式，进行文字匹配
import urllib.request,urllib.error     #指定url，获取网页数据
import xlwt                            #进行excel操作
import sqlite3                         #进行sqlite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start=0"
    datalist = getData(baseurl)
    savepath=".\\豆瓣电影top250.xls"
    saveData(savepath)
   #askURL(baseurl)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)       #调用一次循环爬取下25本电影
        html = askURL(url)              #保存获取到的网页源码

        #逐一解析（弄到一个网页就解析一下）



    return datalist


#得到指定一个url的网页内容
def askURL(url):
    head = {        #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
            #用户代理表示告诉豆瓣服务器我们是什么类型的机器，浏览器。本质上告诉浏览器我们可以接收什么水平的文件内容

    request=urllib.request.Request(url=url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html





#保存数据
def saveData(savepath):
    pass


if __name__ == "__main__":
    main()

