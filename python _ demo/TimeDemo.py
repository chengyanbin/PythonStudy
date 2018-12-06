
#!/usr/bin/python

import time
localTime = time.localtime(time.time())
print("本地时间为:",localTime)

#----------格式化时间--------------
localtime1 = time.asctime(time.localtime(time.time()))
print("本地格式化时间:",localtime1)

#----------格式化时间1--------------
# 不能直接print
#格式化成 2018---6---21 10:56:20格式
print(time.strftime("%Y---%m---%d %H:%M:%S",time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S",time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
