
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

# 格式化成2016-03-20 11:45:39形式
str1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(str1)
# 格式化成Sat Mar 28 22:24:24 2016形式
str2 =  time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
print(str2)
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
time1 = time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print(time1)
