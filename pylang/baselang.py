#!/usr/bin/python3

#coding=utf-8

#这是个注释

'''
这个是多行注释
'''
import json
from pprint import pprint

"""
这个是多行注释
"""

print("+++++++++++++++")
pprint(str.__dict__)
print("这个是不换行的",end=" ")
print("helloworld!!")

from pylang.pkg import hello
print("+++++: "+hello.xxx())

import pylang.pkg.hello
print("+++++: "+pylang.pkg.hello.xxx())

import keyword

print(keyword.kwlist)

name=input("请输入姓名: ")
print("您的输入是: "+name)

num=input("请输入数字: ")
print("您输入的数字+1后是: ",(int(num)+1))


import sys;
print("请输入一个字符串:",end=" ")
sys.stdout.flush();
line=sys.stdin.readline().strip();
sys.stdout.write("您输入的字符串是: "+line+"\n")


from sys import path

pprint(path)

print(r"aaa\nbbb")
print(R"aaa\nbbb")

print(u"我")
print(U"我".encode("utf-8"))

print(b"abc".decode("utf-8"))


sys.exit(100)