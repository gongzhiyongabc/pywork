#获得任意标签名
from xml.dom import minidom

#打开xml文档
dom = minidom.parse('info.xml')

#得到文档元素对象
root = dom.documentElement

tagname = root.getElementByTagName('browser')
print(tagname[0].tagName)

tagname = root.getElementByTagName('login')
print(tagname[1].tagName)

tagname = root.getElementByTagName('province')
print(tagname[2].tagName)

