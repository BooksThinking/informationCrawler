import manageTieBa
from urllib import parse
from bs4 import BeautifulSoup

def init_data(self,kw,beginPage,endPage):
    url = "http://tieba.baidu.com"
    key = parse.urlencode({"kw": kw})  # .encode("utf-8")
    fullurl = url + "/f?" + key
    manageTieBa.tiebaSpider(fullurl, beginPage, endPage)
    for i in range(0, abs(beginPage - endPage) + 1):
        manageTieBa.writeData(i)
    manageTieBa.write_mysql()

if __name__ == '__main__':
    # line = "asdasd'sdaasd\nasds"
    # print(line.replace("\n", "").replace("'",""))
    kw = input("请输入需要爬取的贴吧名:")
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入结束页："))

    url = "http://tieba.baidu.com"
    key = parse.urlencode({"kw": kw})  # .encode("utf-8")
    fullurl = url + "/f?" + key
    manageTieBa.tiebaSpider(fullurl, beginPage, endPage)
    for i in range(0,abs(beginPage - endPage)+1):
        manageTieBa.writeData(i)
    manageTieBa.write_mysql()
