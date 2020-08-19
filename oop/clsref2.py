#!/usr/bin/env python
#-*- coding:utf-8 -*-
import importlib
import sys

class Foo(object):
    def __init__(self):
        self.name = 'xxx'

    def func(self):
        print("ffffff")
        return 'func'

    def funcParam(self,a):
        print("ffffff",a)
        return 'funcParam'

obj = Foo()#实例化一个对象

# #### 检查是否含有成员 ####
print(hasattr(obj, 'name'))
print(hasattr(obj, 'func'))

# #### 获取成员 ####
print(getattr(obj, 'name'))
print(getattr(obj, 'func'))

f=getattr(obj,'func')
f()

f=getattr(obj,'funcParam')
f("aaa")

# #### 设置成员 ####
setattr(obj, 'age', 18)#添加属性
setattr(obj, 'show', lambda num: num + 1)#添加方法
print(vars(obj))

# # #### 删除成员 ####
print(delattr(obj, 'name'))
print(delattr(Foo, 'func'))

print("="*50+"1")
#===========================================================

# from 包 import 模块名 as 别名 ====等于=== 别名 = __import__("模块名的字符串")
a = __import__('oop.test.test',fromlist=True)#基础的导入
a.xxx()
__import__("oop.test.test1",fromlist=True)#多层级的导入
__import__("oop.test.test2")  #是不对的　只导入了ａ目录包

print("="*50+"2")
#===========================================================

my_moudle_name = "oop.test.test"
aa = importlib.import_module(my_moudle_name)

aa.xxx()


print("="*50+"3")
#===========================================================

data = "abc"


def f1():
    print("f1 function")


def f2():
    print("f2")

class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def f3(self):
        print("f3",self.a,self.b)

this_module = sys.modules[__name__]
print(hasattr(this_module, "data"))  # 使用反射
f1_get = getattr(this_module, "f1")  # 使用反射获取
f1_get()

# s=eval("Test")("111","222")
# s.f3()

print()
print(dir(this_module))
print()
t=getattr(this_module,"Test")
t("aaa","bbb").f3()





class A:
    pass
class B:
    pass

a=A()
b=B()

setattr(a,'xxx','aaa')
setattr(b,'yyy','bbb')
print(a.__dict__,b.__dict__)
setattr(a, 'x', lambda num: num + 1)#添加方法
setattr(b,'y', lambda num: num - 1)
print(a.__dict__,b.__dict__)
