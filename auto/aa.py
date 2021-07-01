
from lxml import etree, html

selector = etree.parse(
                       "G:/allpython/autotest_pytest/report.html",
                       parser=etree.HTMLParser(encoding="utf-8")
                       )

# # print(selector.xpath('//span[@class="failed"]/text()'))
# print(selector.xpath('//tbody[@class="failed results-table-row"]/tr/td[2]/text()'))
print(selector.xpath('//td[@class="col-result"]/following::td[1]/text()'))
# 下标从1开始的

#
# for content in selector.xpath('//td[@class="col-result"]/following::td'):
#     print(html.tostring(content, encoding="utf-8").decode("utf-8"))
#     # 为什么解码之后  又decode
# text = """
# <td class="col-name">interface/test_interface.py::TestInterface::test_003_interface_qq</td>
#
# <td class="col-duration">2.01</td>
#
# <td class="col-links"></td>
# <td class="extra" colspan="4">
#             <div class="log">self = &lt;test_interface.TestInterface object at 0x0448F290&gt;<br><br>    def test_003_interface_qq(self):<br>        time.sleep(2)<br>&gt;       assert None<br><span class="error">E       assert None</span><br><br>interface\test_interface.py:12: AssertionError<br></div></td>
# <td class="col-result">Failed</td>
#
# """
#
#
# selector = etree.HTML(text) # html  里面是字节流 html 在传输过程中是bytes流
# # print(etree.tostring(selector, encoding="utf-8").decode("utf-8")) # 解析成字符串  编码和解码
# # 高速文件本身解析成我们中文可读的uff-8 格式 然后解码成 32：00
#
# for content in selector.xpath('//td[@class="col-result"]'):
#     print(etree.tostring(content, encoding="utf-8").decode("utf-8"))

