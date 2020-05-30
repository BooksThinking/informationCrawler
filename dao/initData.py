import manageTieBa
from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

if __name__ == '__main__':
    filename2 = "tiezi" + str(1) + ".html"
    HTMLFile2 = open(filename2, 'r', encoding='utf-8')
    htmlhandle2 = HTMLFile2.read()
    soup2 = BeautifulSoup(htmlhandle2, 'html.parser')
    test_list = soup2.find_all(name="div",attrs={"class": "j_lzl_container core_reply_wrapper"})
    for test in test_list:
        print(test)
    # div_list = soup2.find_all(name="div",attrs={"class": "l_post l_post_bright j_l_post clearfix"})
    # for div in div_list:
    #     soup2 = BeautifulSoup(str(div), 'html.parser')
    #     print(soup2.find_all(name="li", attrs={"class": "lzl_single_post j_lzl_s_p"}))
    #     print("\n")
    # tieziNumber = soup2.find(name="li", attrs={"class": "l_reply_num"})
    # print(tieziNumber)
    # a = int(tieziNumber.contents[2].text)
    # print(a)
    # tiezi_list = soup2.find_all(name="div", attrs={"class": "d_badge_lv"})
    # tiezi_name_list = soup2.find_all(name="a", attrs={"class": ["p_author_name j_user_card",
    #                                                             "user_badge d_badge_bright d_badge_bawu1"]})
    # tiezi_content_list = soup2.find_all(name="div",attrs={"class": "d_post_content j_d_post_content"})
    # print(len(tiezi_list))
    # print(len(tiezi_name_list))
    # print(len(tiezi_content_list))
    # for i in range(0,29):
        # print(tiezi_list[i])
        # print(tiezi_name_list[i])
        # print(tiezi_content_list[i].text)


    # kw = input("请输入需要爬取的贴吧名:")
    # beginPage = int(input("请输入起始页："))
    # endPage = int(input("请输入结束页："))
    #
    # url = "http://tieba.baidu.com"
    # key = parse.urlencode({"kw": kw})  # .encode("utf-8")
    # fullurl = url + "/f?" + key
    # manageTieBa.tiebaSpider(fullurl, beginPage, endPage)
    # for i in range(0,abs(beginPage - endPage)+1):
    #     filename = "tieba" + str(i+1) + ".html"
    #     HTMLFile = open(filename, 'r', encoding='utf-8')
    #     htmlhandle = HTMLFile.read()
    #     soup = BeautifulSoup(htmlhandle, 'html.parser')
    #     # tag_a_list用来表示这个贴吧有多少的帖子的列表
    #     tag_a_list = soup.find_all(name='a', attrs={"class": "j_th_tit"})
    #     # 开始遍历这一页所有的帖子
    #     for tag_a in tag_a_list:
    #         tieZiUrl = url + tag_a.attrs['href']
    #         manageTieBa.tieziSpider(tieZiUrl,1,1)
    #         filename2 = "tiezi" + str(1) + ".html"
    #         HTMLFile2 = open(filename2, 'r', encoding='utf-8')
    #         htmlhandle2 = HTMLFile2.read()
    #         soup2 = BeautifulSoup(htmlhandle2, 'html.parser')
    #
    #
    #         # count用来表示这个帖子有多少页
    #         tieziNumber = soup2.find(name="li",attrs={"class": "l_reply_num"})
    #         count = int(tieziNumber.contents[2].text)
    #         # 把所有楼层的div父标签给读取出来，具体的信息要读这些div标签
    #         floor_list = soup2.find_all(name="div",attrs={"class": "l_post l_post_bright j_l_post clearfix"})
    #         # lv和name分别表示每一楼的等级和姓名，content表示的是没有喽的内容
    #         tiezi_lv_list = soup2.find_all(name="div", attrs={"class": "d_badge_lv"})
    #         tiezi_name_list = soup2.find_all(name="a",attrs={"class": ["p_author_name j_user_card",
    #                                                                    "user_badge d_badge_bright d_badge_bawu1"]})
    #         tiezi_content_list = soup2.find_all(name="div", attrs={"class": "d_post_content j_d_post_content"})
    #         print(tieziNumber)
    #         # for tiezi_page in range(2,count+1):
    #         #     url = tieZiUrl + "?pn=" + str(tiezi_page)
    #         #     manageTieBa.tieziSpider(url)
    #         #     filename3 = "tiezi" + str(tiezi_page) + ".html"
    #         #     HTMLFile3 = open(filename3, 'r', encoding='utf-8')
    #         #     htmlhandle3 = HTMLFile3.read()
    #         #     tiezi_lv_list = tiezi_lv_list + soup2.find_all(name="div", attrs={"class": "d_badge_lv"})
    #         #     tiezi_name_list = tiezi_name_list + soup2.find_all(name="a", attrs={"class": ["p_author_name j_user_card",
    #         #                                                                 "user_badge d_badge_bright d_badge_bawu1"]})
    #         #     tiezi_content_list = tiezi_content_list + soup2.find_all(name="div", attrs={"class": "d_post_content j_d_post_content"})
    #
    #     print(len(tiezi_lv_list))
    #     print(len(tiezi_name_list))
    #     print(len(tiezi_content_list))