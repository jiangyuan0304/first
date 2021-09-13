
import urllib
import requests
from bs4 import BeautifulSoup as bf
# post_param = {'action': '', 'start': '0', 'limit': '1'}
param = {"pageSize": 20, "pageContext": 72}
return_data = requests.get("https://sj.qq.com/myapp/detail.htm?apkName=com.gtgj.view&info=24B8C841A038B746D19B6F7F3D47EF1F",
                           verify=False)
# print(return_data.text)
# print(type(return_data.text))
soup = bf(return_data.text, "lxml")
print("********")
app_message_list = []
print()

with open("G:\\transmissions\\gaotie.apk", 'wb+') as f:
    f.write(requests.get(soup.find("a", attrs={"appname": "高铁管家"}).attrs["ex_url"]).content)

# for i in soup.find_all("div", "app-info-desc"):
#     # print(i.find_all("li"), end="\n\n")
#     app_message_list.append([i.find_all("a")[0].string,
#                              i.find_all("span", "size")[0].string,
#                              i.find_all("span", "download")[0].string.strip(),
#                              i.find_all("a")[0].attrs["href"],
#                              ])
#     # print(i.find_all("a")[0].string)
#     # print(i.find_all("span", "size")[0].string)
#     # print(i.find_all("span", "download")[0].string.strip())
#
# from pprint import pprint
# pprint(app_message_list)









#
# from urllib.parse import urlparse
# import requests
# import re
# from pprint import pprint
# from bs4 import BeautifulSoup as bf
# # param = {"pageSize": 20, "pageContext": 10}
# return_data = requests.get("https://sj.qq.com/myapp/category.htm?orgame=1&categoryId=-10",
#                            verify=False)
# soup = bf(return_data.text, "lxml")
# app_message_list = []
# for i in soup.find_all("li", id=re.compile(r'^cate-\d+$')):
#     href = i.find("a").attrs["href"]
#     print(i.find("a").string)
#     print("".join(["https://sj.qq.com/myapp/category.htm", href]))
#






