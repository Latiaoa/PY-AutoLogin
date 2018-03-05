import requests
import time
from selenium import webdriver
chromePath = r'D:\Programing\chromedriver_win32\chromedriver.exe'
wd = webdriver.Chrome(executable_path= chromePath)
loginPath = r'http://www.baidu.com/'
wd.get("loginPath")
keywords = 'MrLevo520 CSDN'
send_keywords=keywords.decode('utf-8')#中英混输入可防止乱码
wd.find_element_by_id("sb_form_q").send_keys(send_keywords)
time.sleep(1)
#----------操作一：进行对关键字MrLevo520 CSDN搜索----------------
wd.find_element_by_id("sb_form_go").click()#执行此操作会进行搜索，但是没有弹出新窗口，所以句柄不用重定位
time.sleep(3)
#----------操作二：对搜索页面第一项进行点击操作--------------
wd.find_element_by_xpath("/html/body/div/ol/li/h2/a").click()#进行当前页面点击第一项

#--------操作三：对新弹出的页面再点击"我的头像"选项-----
#注意此时已经是弹出的第一个窗口了，需要重新定位句柄
'''browser.switch_to_window(browser.window_handles[1])#方法一'''
for handle in wd.window_handles:#方法二，始终获得当前最后的窗口
    wd.switch_to_window(handle)

wd.find_element_by_xpath("//div[@id='body']/div[2]/div/div/ul[2]/div/a").click()

wd.switch_to_window(wd.window_handles[2])#方法一，注意window_handles[2]变成了2
'''for handle in browser.window_handles:#方法二，始终获得当前最后的窗口
    browser.switch_to_window(handle)'''

wd.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/a[3]").click()

time.sleep(5)
