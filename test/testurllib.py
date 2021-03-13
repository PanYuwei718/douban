# -*- coding = utf-8 -*-
# @Time : 2021/3/13 12:26 上午
# @Author : Pan
# @Software: PyCharm

import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))


#获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8") #模拟用户登陆
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheaders())       #把respoense header的信息全部返回



# headers = {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
# }  #去浏览器找出来，模拟浏览器发送的请求
#
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"name":"pan"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)        #把封装的对象传进去，访问网址
# print(response.read().decode("utf-8"))


url = "https://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))



