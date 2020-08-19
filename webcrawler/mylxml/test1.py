#! /usr/bin/env python
# -*- coding: utf-8 -*-

# lxml可以修正错误的页面
import requests
from lxml import etree

str1='''
<div>
    <ul>
        <li>哈哈</li>
        <li>bbb</li>
        <li>ccc
    </ul>
</div>
'''
html=etree.HTML(str1)
print(html)
print("---------")
res=etree.tostring(html, encoding = "utf-8", pretty_print = True, method = "html")
print(res.decode("utf-8"))

print("="*50+"1")
#==========================================

html=etree.parse("/home/andilyliao/PycharmProjects/iotest-py/webcrawler/mylxml/test.html")
res=etree.tostring(html, encoding = "utf-8", pretty_print = True, method = "html")
print(res.decode("utf-8"))


print("="*50+"2")
#==========================================

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/job_detail/1416571896.html?ka=search_list_2",headers=headers)
html=etree.HTML(res.text)
res2=etree.tostring(html, encoding = "utf-8", pretty_print = True, method = "html")
# print(res2.decode("utf-8"))

print("="*50+"3")
#===================xpath=======================
# chrome->开发者工具->elements->通过鼠标选择网页中需要的内容->chrome定位到内容的源码->在选中的源码上右键->copy xpath
# //*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/h3/a/span
# 通过text()获取内容
# //*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/h3/a/span/text()

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/c101030100-p100101/",headers=headers)

selector=etree.HTML(res.text)
price=selector.xpath('//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/h3/a/span/text()')[0]
print(price)

print("="*50+"4")
#===================xpath=======================
# 连续获取两次，看规律
# //*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/h3/a/span
# //*[@id="main"]/div/div[2]/ul/li[2]/div/div[1]/h3/a/span


headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/c101030100-p100101/",headers=headers)
selector=etree.HTML(res.text)
# 根据循环内容获取条目循环次数
urls=selector.xpath('//div[@class="job-list"]/ul/li')
i=len(urls)
print(i)
for j in range(i):
    j=j+1
    price=selector.xpath('//*[@id="main"]/div/div[2]/ul/li['+str(j)+']/div/div[1]/h3/a/span/text()')[0]
    print(price)