from urllib.request import urlopen
import pymysql
import os
from bs4 import BeautifulSoup

def loadPage(url, filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
        filename : 处理的文件名
    """
    # print("正在下载 " + filename)
    # request = urllib.Request(url, headers = headers)
    # html = urlopen(url).read().decode("utf-8")
    request = urlopen(url)
    html = request.read().decode("utf-8")
    # print(html.read().decode("utf-8"))
    # print(html)
    return html


def writePage(html, filename):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    # print("正在保存 " + filename)
    # 文件写入
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    # print("-" * 30)

def writeData(tieba_number):
    filename = "tieba" + str(tieba_number + 1) + ".html"
    HTMLFile = open(filename, 'r', encoding='utf-8')
    htmlhandle = HTMLFile.read()
    soup = BeautifulSoup(htmlhandle, 'html.parser')
    # tag_a_list用来表示这个贴吧有多少的帖子的列表
    tag_a_list = soup.find_all(name='a', attrs={"class": "j_th_tit"})
    # 开始遍历这一页所有的帖子
    for tag_a in tag_a_list:
        url = "http://tieba.baidu.com"
        # data_file_number = data_file_number + 1
        # data_file_name = open("../data/data" + str(data_file_number) + ".txt", "w",encoding='utf-8')
        data_file_name = open("../data/data" + tag_a.attrs['href'][3:] + ".txt", "w", encoding='utf-8')
        tieZiUrl = url + tag_a.attrs['href']
        tieziSpider(tieZiUrl, tag_a.attrs['href'], 1, 1)


        filename2 = tag_a.attrs['href'][3:] + "tiezi" + str(1) + ".html"
        HTMLFile2 = open(filename2, 'r', encoding='utf-8')
        htmlhandle2 = HTMLFile2.read()
        soup2 = BeautifulSoup(htmlhandle2, 'html.parser')

        # count用来表示这个帖子有多少页
        tieziNumber = soup2.find(name="li", attrs={"class": "l_reply_num"})
        count = int(tieziNumber.contents[2].text)
        tieziSpider(tieZiUrl, tag_a.attrs['href'], 2, count)
        # 把所有楼层的div父标签给读取出来，具体的信息要读这些div标签
        # floor_list = soup2.find_all(name="div",attrs={"class": "l_post l_post_bright j_l_post clearfix"})
        # lv和name分别表示每一楼的等级和姓名，content表示的是没有喽的内容
        tiezi_lv_list = soup2.find_all(name="div", attrs={"class": "d_badge_lv"})
        tiezi_name_list = soup2.find_all(name="li", attrs={"class": "d_name"})
        tiezi_content_list = soup2.find_all(name="div", attrs={"class": "d_post_content j_d_post_content"})
        # 注意时间
        tiezi_time_list = soup2.find_all(name="div", attrs={"class": "post-tail-wrap"})
        for tiezi_page in range(2, count + 1):
            filename3 = tag_a.attrs['href'][3:] + "tiezi" + str(tiezi_page) + ".html"
            HTMLFile3 = open(filename3, 'r', encoding='utf-8')
            htmlhandle3 = HTMLFile3.read()
            soup3 = BeautifulSoup(htmlhandle3, 'html.parser')
            tiezi_lv_list = tiezi_lv_list + soup3.find_all(name="div", attrs={"class": "d_badge_lv"})
            tiezi_name_list = tiezi_name_list + soup3.find_all(name="li", attrs={"class": "d_name"})
            tiezi_content_list = tiezi_content_list + soup3.find_all(name="div",
                                                                     attrs={"class": "d_post_content j_d_post_content"})
            tiezi_time_list = tiezi_time_list + soup3.find_all(name="div", attrs={"class": "post-tail-wrap"})
        for size in range(0, len(tiezi_lv_list)):
            write_line = str(tiezi_name_list[size].text.replace("\n", "")) + "#" + str(
                tiezi_lv_list[size].contents[0]) + "#" + tiezi_content_list[size].text + "#" + \
                         tiezi_time_list[size].contents[-1].text
            data_file_name.write(write_line + "\n")
        data_file_name.close()


def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "tieba" + str(page) + ".html"
        fullurl = url + "&pn=" + str(pn)
        print(fullurl)
        html = loadPage(fullurl, filename)
        # print("网站内容：", html)
        writePage(html, filename)
        # print("谢谢使用")

def tieziSpider(url, append, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endPage + 1):
        filename = append[3:] + "tiezi" + str(page) + ".html"
        # print(url)
        fullurl = url + append + "?pn=" + str(page)
        html = loadPage(fullurl, filename)
        # print("网站内容：", html)
        writePage(html, filename)
        # print("谢谢使用")

def write_mysql():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1245586921',
        db='crawler',
        charset='utf8mb4'
    )

    # 获取游标
    cursor = conn.cursor()
    # sql = "INSERT INTO crawler.crawlerdata(userName,userLevel,userMessage,userTime) values (%s,%s,%s,%s)"
    # line = ['可可麦茶', '1', '            这一话当年在日本被骂惨了…日本别的不说，主流观念“我戳你伤口可以，但是你揭我伤疤绝对不行！(▼皿▼', '")”真的是挺恶心（这跟文化还有背景教育有关，无关其他，理性看待）', '2020-02-08 20:38']
    # cursor.execute(sql, (line[0], line[1], line[2], line[3]))
    # conn.commit()
    file_path = "../data/"
    dirs = os.listdir(file_path)
    for file in dirs:
        file = open(file_path + file, encoding='UTF-8')
        while True:
            line = file.readline().replace("\n", "").split("#")
            if line == ['']:
                break
            else:
                sql = "INSERT INTO crawler.crawlerdata(userName,userLevel,userMessage,userTime) values (%s,%s,%s,%s)"
                for i in range(0, 2):
                    cursor.execute(sql, (line[0], line[1], line[2], line[-1]))
                    print("正在操作")
                print("commit 成功")
                conn.commit()


if __name__ == '__main__':
    file = "6720490845tiezi1.html"
    HTMLFile2 = open(file, 'r', encoding='utf-8')
    htmlhandle2 = HTMLFile2.read()
    soup2 = BeautifulSoup(htmlhandle2, 'html.parser')
    tiezi_lv_list = soup2.find_all(name="div", attrs={"class": "d_badge_lv"})
    print(len(tiezi_lv_list))
    # 建立数据库连接
    # conn = pymysql.Connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     passwd='1245586921',
    #     db='crawler',
    #     charset='utf8mb4'
    # )
    #
    # # 获取游标
    # cursor = conn.cursor()
    # # sql = "INSERT INTO crawler.crawlerdata(userName,userLevel,userMessage,userTime) values (%s,%s,%s,%s)"
    # # line = ['可可麦茶', '1', '            这一话当年在日本被骂惨了…日本别的不说，主流观念“我戳你伤口可以，但是你揭我伤疤绝对不行！(▼皿▼', '")”真的是挺恶心（这跟文化还有背景教育有关，无关其他，理性看待）', '2020-02-08 20:38']
    # # cursor.execute(sql, (line[0], line[1], line[2], line[3]))
    # # conn.commit()
    # file_path = "../data/"
    # dirs = os.listdir(file_path)
    # for file in dirs:
    #     file = open(file_path + file, encoding='UTF-8')
    #     while True:
    #         line = file.readline().replace("\n", "").split("#")
    #         if line == ['']:
    #             break
    #         else:
    #             sql = "INSERT INTO crawler.crawlerdata(userName,userLevel,userMessage,userTime) values (%s,%s,%s,%s)"
    #             for i in range(0, 2):
    #                 cursor.execute(sql, (line[0], line[1], line[2], line[-1]))
    #                 print("正在操作")
    #             print("commit 成功")
    #             conn.commit()

