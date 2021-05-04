# -*- coding = utf-8 -*-
# @Time : 2021/4/15 8:44 午後
# @Author : Pan
# @Software: PyCharm

import xlwt

# workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
#
# worksheet = workbook.add_sheet('sheet1') #创建工作表
# worksheet.write(0,0,'hello')  #写入数据，表示在sheet1中的第一行第一列写入hello
# workbook.save('student.xls')  #保存数据表

#居然打开的是wps，不是office，差评。

#向excel写入99乘法表。
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d" %(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')