# mymod4.py

''' 下划线开头的属性,将在
from mymod4 import * 语句导入时,不会导入
'''

def f():
    pass

def _f1():
    pass

def __f2():
    pass

name1 = "aaaaa"
_name1 = 'bbbbb'

