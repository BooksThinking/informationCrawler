import manageTieBa
import os
from urllib import parse
from bs4 import BeautifulSoup

if __name__ == '__main__':
    kw = input("请输入需要爬取的贴吧名:")
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入结束页："))
    data_file_number = 0

    url = "http://tieba.baidu.com"
    key = parse.urlencode({"kw": kw})  # .encode("utf-8")
    fullurl = url + "/f?" + key
    manageTieBa.tiebaSpider(fullurl, beginPage, endPage)
    for i in range(0,abs(beginPage - endPage)+1):
        manageTieBa.writeData(i)

