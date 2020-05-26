from bs4 import BeautifulSoup

HTMLFile = open("1.html", 'r', encoding='utf-8')
htmlhandle = HTMLFile.read()
soup = BeautifulSoup(htmlhandle, 'html.parser')
tag_a_list = soup.find_all(name='a', attrs={"class":"j_th_tit"})
for tag_a in tag_a_list:
    print(tag_a.attrs['href'])





# soup = BeautifulSoup()