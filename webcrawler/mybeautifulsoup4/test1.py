#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/job_detail/1416571896.html?ka=search_list_2",headers=headers)

soup=BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())

print("="*50+"1")
#==========================================

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/job_detail/1416571896.html?ka=search_list_2",headers=headers)

soup=BeautifulSoup(res.text,'html.parser')
res=soup.find_all("div",attrs={"class":"text"})
print(res)

print("="*50+"2")
#==========================================

# chrome->开发者工具->elements->通过鼠标选择网页中需要的内容->chrome定位到内容的源码->在选中的源码上右键->copy->copy selector
# #main > div > div.job-list > ul > li:nth-child(1) > div > div.info-primary > h3 > a > span

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/c101030100-p100101/",headers=headers)

soup=BeautifulSoup(res.text,'html.parser')

# price=soup.select("#main > div > div.job-list > ul > li:nth-child(1) > div > div.info-primary > h3 > a > span")
# li:nth-child(1)必须换成li:nth-of-type(1) 框架问题
price=soup.select("#main > div > div.job-list > ul > li:nth-of-type(1)> div > div.info-primary > h3 > a > span")
print(price)

print("="*50+"2")
#==========================================
# 获取连续两条的内容，看下规律
# #main > div > div.job-list > ul > li:nth-child(1) > div > div.info-primary > h3 > a > span
# #main > div > div.job-list > ul > li:nth-child(2) > div > div.info-primary > h3 > a > span
# 所以修改为获取全部
# #main > div > div.job-list > ul > li > div > div.info-primary > h3 > a > span

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/c101030100-p100101/",headers=headers)

soup=BeautifulSoup(res.text,'html.parser')

prices=soup.select("#main > div > div.job-list > ul > li > div > div.info-primary > h3 > a > span")
for price in prices:
    print(price.get_text())