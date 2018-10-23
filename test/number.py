from random import randint

#生成一个1000到9999之间的随机整数
verify = randint(1000,9999)
print(u"生成的随机数：%d"%verify)

number = input("请输入随机数：")
print(number)
number = int(number) #input接收到的数据是以字符串的形式返回的

if number == verify:
    print("登录成功！")
elif number == 132741:
    print("登录成功！！")
else:
    print("验证码输入有误！")

