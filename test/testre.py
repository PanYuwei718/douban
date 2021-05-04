# -*- coding = utf-8 -*-
# @Time : 2021/3/16 11:43 下午
# @Author : Pan
# @Software: PyCharm

#正则表达式

import re

#创建模式对象
pat = re.compile("AA")      #创建对象，然后对这个对象用search方法
m = pat.search("CBA")       #search字符串是被校验的内容
print(m)                    #返回None，因为CBA里没AA

n = pat.search("ABCAA")     #返回 <re.Match object; span=(3, 5), match='AA'>
print(n)

print("---------------------------------------")

#无模式对象*****
m = re.search("asd","bjgasdg")  #  <re.Match object; span=(3, 6), match='asd'>
print(m)

print(re.findall("a","ADGHaBHJa")) #['a', 'a']    findall返回的就是列表

print(re.findall("[A-Z]","ADGHaBHJa"))  #['A', 'D', 'G', 'H', 'B', 'H', 'J']

print(re.findall("[A-Z]+","ADGHaBHJa"))  # ['ADGH', 'BHJ']    比如abc+ 表示abc，abcc，abccc。。。

#sub 替换
print(re.sub("a","A","asdasda")) #找到a，用a来替换

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
