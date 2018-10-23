from xml.dom import minidom
#获得标签信息
#打开文档
dom = minidom.parse('info.xml')

#得到文档元素对象
root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
