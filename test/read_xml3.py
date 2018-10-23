#获得标签的属性值
from xml.dom import minidom

#打开xml文档
dom = minidom.parse('info.xml')

#得到文档元素对象
root = dom.documentElement

logins = root.getElementByTagName('login')

#获得login标签的username属性值
username = logins[0].getAttribute('username')
print(username)

#获得login标签的password属性值
password = logins[0].getAttribute('password')
print(password)

#获得第二个login标签的username属性值
username = logins[1].getAttribute('username')
print(username)

#获得第二个login标签的password属性值
password = logins[1].getAttribute('password')
print(password)
