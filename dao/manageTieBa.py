from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

def loadPage(url, filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
        filename : 处理的文件名
    """
    print("正在下载 " + filename)
    # request = urllib.Request(url, headers = headers)
    html = urlopen(url).read().decode("utf-8")
    # print(html.read().decode("utf-8"))
    print(html)
    return html


def writePage(html, filename):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    print("正在保存 " + filename)
    # 文件写入
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print("-" * 30)


def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = str(page) + ".html"
        fullurl = url + "&pn=" + str(pn)
        print(fullurl)
        html = loadPage(fullurl, filename)
        print("网站内容：", html)
        writePage(html, filename)
        print("谢谢使用")
