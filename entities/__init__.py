from selenium import webdriver
import time

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
# #手动输入验证码
# driver.find_element_by_id("TANGRAMPSP_3__submit").click()
# print("what the fuck had happened")
# time.sleep(25)
driver.get('https://tieba.baidu.com/f?kw=万元归一诀&fr=index')
time.sleep(6)
driver.find_element_by_name("title").send_keys('自动发帖测试')
driver.find_element_by_id("ueditor_replace").send_keys('发帖测试')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]').click()