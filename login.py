import requests
from selenium import webdriver
chromePath = r'D:\Programing\chromedriver_win32\chromedriver.exe'
wd = webdriver.Chrome(executable_path= chromePath) #构建浏览器
loginUrl = 'http://www.weibo.com/login.php'
wd.get(loginUrl) #进入登陆界面
wd.maximize_window()
print(wd.current_window_handle)
wd.find_element_by_xpath('//*[@id="loginname"]').send_keys('phone') #输入用户名
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('password') #输入密码
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click() #点击登陆
print(wd.current_window_handle)
req = requests.Session() #构建Session
cookies = wd.get_cookies() #导出cookie
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value']) #转换cookies
wd.find_element_by_xpath("//*[@id='v6_pl_content_publishertop']/div/div[2]/textarea").send_keys("谷大白话")