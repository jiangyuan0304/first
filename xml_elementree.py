from xml.etree.ElementTree import Element, SubElement, ElementTree

# 生成根节点
root = Element('testcase')

# 生成一个跟节点

# 生成第一个子节点 head
head = SubElement(root, 'head', attrib={"name":"jiangyuan", "selected":"false"})
head.text = "heiheihei"
# head 节点的子节点
# title = SubElement(head, 'title')
SubElement(head, 'title').text = "jiangyuan"
# SubElement()是设置子节点 并且第一个参数就是设置是那个节点得子节点，第二个参数是设置标签名字，
# attrib={} 则是设置该标签的各种属性
#


# title.text = 'Well Dola!'
# 生成 root 的第二个子节点 body
body = SubElement(root, 'body')
# body 的内容
body.text = 'I love Dola!'
tree = ElementTree(root)

# 下面是设置新的节点
# 首先创建节点tag  使用Element
newEle = Element("newLElement")
# 设置节点属性
newEle.attrib = {"name":"wangjiaming"}
newEle.text = "jiangyiheng"
body.append(newEle)

# 修改节点属性很方便
root.set("name", "jiangleyi")

tree.write('result.xml', encoding='utf-8')

# import xml.etree.ElementTree as ET
# tree = ET.parse('result.xml')
# root = tree.getroot()
# for child in root:
#     print(child, child.tag, child.attrib, child.text)
#     # child 元素在地址的位置， child的标签， child 的属性 child 内的标签
#     for child_child in child:
#         print(child_child, child_child.tag, child_child.attrib, child_child.text)
