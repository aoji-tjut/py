#! /usr/bin/env python
# -*- coding: utf-8 -*-

# chrome->开发者工具->network->选择xhr标签
# 例子查看的是简书，用的冉小龙的页面https://www.jianshu.com/u/336e6a2afb16
# 进入后查看他的动态，清空监控，然后开始滚动鼠标，观察分页请求
# 然后分页的链接是：
# https://www.jianshu.com/u/336e6a2afb16
# https://www.jianshu.com/u/336e6a2afb16?order_by=shared_at&page=2
# https://www.jianshu.com/u/336e6a2afb16?order_by=shared_at&page=3
from lxml import etree

import requests

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

titles=[]

try:
    for i in range(1,10):
        res=requests.get("https://www.jianshu.com/u/336e6a2afb16?order_by=shared_at&page="+str(i))
        selector=etree.HTML(res.text)
        infos=selector.xpath('//ul[@class="note-list"]/li/div[@class="content"]')
        for info in infos:
            # //*[@id="note-22257386"]/div/a
            # //*[@id="note-22587020"]/div/a
            # //*[@id="note-21825052"]/div/a
            title=info.xpath("a/text()")[0]
            titles.append(title)
except:
    pass

context=[]
for title in titles:
    if context.__contains__(title):
        pass
    else:
        print(title)
        context.append(title)
