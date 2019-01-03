# tup="a","b","c","d"
# print(tup[0])
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# tup1 = tup1 + tup2
# print(tup1)
import time, datetime

# dict= {'name': 'Zara', 'age': 7, 'class': 'First'}
# print(dict['age'])
# dict['age']=27
# print(dict['age'])
# dict['school']='wutong'
# print(dict)
# del dict['name']
# print(str(dict))
# print(dict.values())
# localtime = time.localtime(time.time())
# print(localtime)
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# oneday = datetime.timedelta(days=1)
# today = datetime.date.today()
# yesterday = datetime.date.today()-oneday
# print(yesterday)
# tomorrow = datetime.date.today()+oneday
# print(tomorrow)
# yesterday1=datetime.datetime.today()-oneday
# print(yesterday1)
# txt = list('123456')
# print(txt)
# txt1=[1,2,3,4,5,6]
# txt1.append('7')
# print(txt1)
# x = {'username': 'Genal','phone':['123','456','789']}
# y = x.copy()
# y['username'] = 'jack'
# y['phone'].remove('456')
# print(x)
# print(y)
# phonetxt = {'Genal':'123','Alix':'456','Jack':'789'}
# print(phonetxt)
# from math import pi
# print('%10.5f' %pi)
# class Fruit():
#     def __init__(self, color):
#         self.color = color
#         print('fruit color:%s' %self.color)
#     def grow(self):
#         print()


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
