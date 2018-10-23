import csv

#读取本地csv文件
date = csv.reader('info.csv','r')
#循环输出每一行信息
for user in date:
    print(user)
