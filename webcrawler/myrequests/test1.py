#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests

res=requests.get("https://www.zhipin.com")
print(res)
print("------")
# print(res.text)

print("="*50+"1")
#==========================================


res=requests.get("https://www.zhipin.com/job_detail/1416571896.html?ka=search_list_2")
print(res)
print("---------------------------------------------------------------")
# print(res.text)
# 加入请求头
# chrome->开发者工具->network->打开网页https://www.liepin.com/zhaopin/?key=java&d_sfrom=search_industry->header中找到User-Agent
# User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res=requests.get("https://www.zhipin.com/job_detail/1416571896.html?ka=search_list_2",headers=headers)
print(res)
print("------")
print(res.text)


