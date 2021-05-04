# -*- coding = utf-8 -*-
# @Time : 2021/3/12 8:25 下午
# @Author : Pan
# @Software: PyCharm

from bs4 import BeautifulSoup          #数据获取，网页解析
import re                              #正则表达式，进行文字匹配
import urllib.request,urllib.error     #指定url，获取网页数据
import xlwt                            #进行excel操作
import sqlite3                         #进行sqlite数据库操作


#先搞出一个item，放到temp.html，然后看里面的规则，写findlink，findImgsrc
findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串模式),这里是找<a href="https://movie.douban.com/subject/1292052/">
                                            #因为里面有双引号，外面直接用单引号  ?是懒惰模式
findImgsrc = re.compile(r'<img.*src="(.*?)"',re.S) #re.S忽略换行符。a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab和ab。所以要加括号？
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)  #导演，主演，类型。 后面有两个</p>，加上问号表示到第一个</p>完事

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        every_url = baseurl + str(i*25)       #调用一次循环爬取下25本电影
        html = askURL(every_url)              #保存获取到的网页源码，（接收return）

        #逐一解析（弄到一个网页就解析一下）
        soup = BeautifulSoup(html,"html.parser")              #用"html.parser"这个解析器，放入内存形成树形结构对象
        for item in soup.find_all('div',class_ = "item"):     #查找符合内容的字符串(返回电影图片和介绍的那个div)！！**** 先取一块，再循环取里面的
            #print(item)  #测试查看电影item的全部信息
            data = []         #保存一部电影的所有信息
            item = str(item)

            link = re.findall(findLink,item)[0]  #拿出那个div里的指定的字符串，[0]表示只要第一个链接，就是电影描述的链接，后面没用的链接拿掉。 findlink全局定义
            data.append(link)                         #拿出一页25部电影的描述链接

            imgsrc = re.findall(findImgsrc,item)
            data.append(imgsrc)

            titles = re.findall(findTitle,item)
            if len(titles)==2:                 #如果有中文名和英文名
                chinese_title = titles[0]
                data.append(chinese_title)
                foreign_title = titles[1].replace("/","")
                data.append(foreign_title)
            else:
                data.append(titles[0])
                data.append(" ")      #留空，因为要放到excle表里。不然格式错位

            reating = re.findall(findRating,item)[0]
            data.append(reating)

            judgeMent = re.findall(findJudge,item)[0]
            data.append(judgeMent)

            inq = re.findall(findInq,item)
            if len(inq) != 0:                     #一句话的那个评价也不一定有，可能为空
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ",bd)  #去掉br
            bd = re.sub('/'," ",bd)
            data.append(bd.strip())   #strip去掉前后空格。

            datalist.append(data)  #把处理好的一部电影信息放入datalist
    print(datalist)  #这玩意是列表套列表
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
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)             #code如果连不上，会有状态码和原因，返回出来
        if hasattr(e,"reason"):
            print(e.reason)
    return html


#保存数据

def saveData(datalist,savepath):
    movie_content = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = movie_content.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)
    col = ('电影详情链接','图片链接','影片中文名','影片英文名','评分','评价数','概况','相关信息')
    for i in range(0,8):
        sheet.write(0,i,col[i]) #把列名写入
    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    movie_content.save(savepath)

if __name__ == "__main__":
        baseurl = "https://movie.douban.com/top250?start=0"
        datalist = getData(baseurl)
        savepath = "./豆瓣电影top250.xls"
        saveData(datalist,savepath)     #command+鼠标点击函数，快速跳转

