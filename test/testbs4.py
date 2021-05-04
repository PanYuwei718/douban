# -*- coding = utf-8 -*-
# @Time : 2021/3/13 3:24 下午
# @Author : Pan
# @Software: PyCharm


#bs4就是把html文档转化成一个结，有下面四种Tag NavigableString BeautifulSoup Comment
from bs4 import BeautifulSoup
import re

file = open("./baidu.html","rb")   #../ 表示当前文件所在的目录的上一级目录     ./ 表示当前文件所在的目录(可以省略)
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")  #！！！！最关键就是拿到这个bs

print(bs.a)  #拿出到第一个标签和里面的内容

print(bs.title.string)      #标签+string 打出内容


print(bs.a.attrs) #{'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'} 拿到标签所有的属性，键值对形式


# print(type(bs)) #自身的类型，表示整个文档
# print(bs.name) #document
# print(bs)      #直接是html里面的所有代码
#
# print(bs.a.string) #拿出注释里面的"新闻"Comment类型,不包含注释符号

#-————————————————————————————————————————————————————————————————
#文档的遍历
#print(bs.head.contents) #返回列表，head里面的所有属性都返回
#print(bs.head.contents[1]) #已经是列表了，直接加下标取出东西 ，更多内容搜索文档

#文档的搜索（有针对性的爬取）
# t_list = bs.find_all("a")   #返回所有"a标签"的东西，也叫字符串搜索
# print(t_list)

#正则表达式搜索，使用search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)                           #标签带a这个字符，就返回

#用方法来搜索，传入一个函数，根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")      #内容里含有"name"就返回
# t_list = bs.find_all(name_is_exists) #传入函数名。
#
# for item in t_list:           #列表换行打印出元素。看起来爽
#     print(item)                        #内容里含有"name"就返回

#kwargs 参数搜索

# t_list = bs.find_all(id="head")
# for item in t_list:
#      print(item)

# t_list = bs.find_all(class_=True)
# for item in t_list:
#      print(item)

# t_list = bs.find_all(href="http://news.baidu.com")
# for item in t_list:
#      print(item)



#文本参数
# t_list = bs.find_all(text=["hao123","贴吧"])
# for item in t_list:
#      print(item)


# t_list = bs.find_all(text=re.compile("\d"))
# for item in t_list:
#      print(item)                             #返回 好123（标签里的字符串）


#limit参数
# t_list = bs.find_all("a",limit=3)  #只要前三个a
# for item in t_list:
#      print(item)




#css选择器 select后面可以跟标签，类名，id  .是类名，#是id ～找兄弟

# print(bs.select("title"))  # [<title>百度一下，你就知道 </title>]

# t_list = bs.select(".mnav",limit=3)  #class="mnav"的前三条返回
# for item in t_list:
#      print(item)

# t_list = bs.select("#u1")  #（div里）id等于u1的返回
# for item in t_list:
#      print(item)

# t_list = bs.select("a[class='bri']")  #a标签中类名为bri的返回
# for item in t_list:
#      print(item)

# t_list = bs.select("head>title")   #通过自标签来查找（head标签里面的title标签）
# for item in t_list:
#      print(item)

t_list = bs.select(".mnav ~ .bri")  #.mnav类名的兄弟类名为.bri的东西返回    #更多产品

print(t_list[0].get_text())







