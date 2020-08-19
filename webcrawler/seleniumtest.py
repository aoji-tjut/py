#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 1、sudo pip3 install selenium
# 2、下载phantomjs-2.1.3，并放到/disk/下

from selenium import webdriver

mydriver=webdriver.PhantomJS(executable_path="/disk/phantomjs")
mydriver.get("https://www.zhipin.com/c101030100-p100101/")
mydriver.implicitly_wait(2) #2秒
data=mydriver.find_element_by_id("header")
print(data.text)
