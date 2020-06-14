from selenium import webdriver
import snownlp
import time


def postTiezi(word):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://passport.baidu.com/v2/?login')
    time.sleep(2)
    driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()
    driver.find_element_by_name("userName").clear()
    driver.find_element_by_name("userName").send_keys('13009806115')
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys('1245586921')
    driver.find_element_by_id("TANGRAM__PSP_3__submit").click()
    time.sleep(50)
    driver.get('https://tieba.baidu.com/f?kw=万元归一诀&fr=index')
    time.sleep(6)
    if snownlp.SnowNLP(word).sentiments > 0.5:
        for i in range(0,10):
            driver.find_element_by_name("title").send_keys('怎么会有这么弱智的问题')
            driver.find_element_by_id("ueditor_replace").send_keys('爬爬爬')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]').click()
    else:
        for i in range(0,10):
            driver.find_element_by_name("title").send_keys('是个好问题')
            driver.find_element_by_id("ueditor_replace").send_keys('赞赞赞')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]').click()

postTiezi("好弱智")