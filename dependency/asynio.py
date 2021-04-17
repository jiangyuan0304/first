from   urllib.request import  urlopen
from  bs4 import  BeautifulSoup as soup
from pprint import pprint

reponse = urlopen("https://www.kan.cc/view/2275.html")
content_soup = soup(reponse, 'lxml')
# print(content_soup.prettify())
# print(content_soup.title.string)
li_list = content_soup.find_all(class_="myui-content__list scrollbar sort-list clearfix")
url_list = list()
for per_li in li_list[0]:
    link_end = per_li.find_all(name="a")
    url_string = "{}{}".format("https://www.kan.cc", link_end[0].attrs["href"])
    # url_list.append(url_string)

    print(url_string)
# pprint(li_list)