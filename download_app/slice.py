
import urllib
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup as bf

param = {"pageSize": 20, "pageContext": 100}
return_data = requests.get("https://sj.qq.com/myapp/category.htm?orgame=1&categoryId=105", params=param,
                           verify=False)
soup = bf(return_data.text, "lxml")
app_message_list = []
for i in soup.find_all("div", "app-info-desc"):
    # print(i.find_all("li"), end="\n\n")
    apk_download_url = "".join(["https://sj.qq.com/myapp/", i.find_all("a")[0].attrs["href"]])
    # print(apk_download_url)
    return_data1 = requests.get(apk_download_url, verify=False)
    print(return_data1.status_code)
    soup1 = bf(return_data1.text, 'lxml')
    apk_name = i.find_all("a")[0].string
    try:
        download_url = soup1.find("a", attrs={"appname": apk_name,
                                                        "class": "det-down-btn"}).attrs["data-apkurl"]
        app_message_list.append([apk_name,
                                 i.find_all("span", "size")[0].string,
                                 i.find_all("span", "download")[0].string.strip().replace("下载", ""),
                                 i.find_all("a")[0].attrs["href"],
                                 download_url,
                                 download_url.split("=")[1].split("&")[0]
                                 ])
    except:
        print( apk_name + "*****")

#
from pprint import pprint
pprint(app_message_list)



