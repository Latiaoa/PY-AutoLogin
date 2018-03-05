from bs4 import BeautifulSoup
import requests

url_1 = "http://image.baidu.com/"
url_2 = "https://e-hentai.org/g/1125545/8fa214c090/"
url ="https://e-hentai.org/"
response = requests.get(url_1)
html = response.text
soup = BeautifulSoup(html,'html.parser')

# 查找所有有关的节点
tags = soup.find_all('a')

#for tag in tags:
 #       img = tag.img['src']
#        print(img)
print(html)