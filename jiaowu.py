import requests
from selenium import webdriver
chromePath = r'D:\Programing\chromedriver_win32\chromedriver.exe'
wd = webdriver.Chrome(executable_path= chromePath)
loginPath = r'http://jiaowu.pdsu.edu.cn'
wd.get(loginPath)
wd.maximize_window()
current_window = wd.current_window_handle
all_windows = wd.window_handles
for window in all_windows:
    if window != current_window:
        wd.switch_to.window(window)
wd.close()                              #清除所有弹出窗口

wd.switch_to.window(current_window)
print(current_window)
wd.switch_to.frame(wd.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr/td/iframe"))
#切换到登录窗口
wd.find_element_by_id("txt_asmcdefsddsd").send_keys('1512101xx')
wd.find_element_by_id("txt_pewerwedsdfsdff").send_keys('password')
wd.find_element_by_id("btn_login").submit()
req=requests.Session()
cookies=wd.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])

import time
time.sleep(1)
#wd.find_element_by_tag_name("frame")
wd.switch_to.frame("frmbody")
print(current_window)
wd.find_element_by_id("memuBarText6").click()
time.sleep(1)
wd.find_element_by_xpath('//*[@id="memuLinkDiv6"]/table/tbody/tr[6]/td[2]/span').click()
wd.switch_to.frame("frmMain")
wd.find_element_by_name("btn_search").submit()
