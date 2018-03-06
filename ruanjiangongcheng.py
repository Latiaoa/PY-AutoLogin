import requests
from selenium import webdriver
chromepath="D:\Programing\chromedriver_win32\chromedriver.exe"
wd=webdriver.Chrome(executable_path=chromepath)
url="http://www.icourse163.org/"
wd.get(url)
wd.find_element_by_class_name("class='m-index-person-loginBtn'").click()
