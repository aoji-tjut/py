# mymod3.py

'''此__all__列表只限制from import *语句的导入
当用from mymod3 import *时,只导入 f1和name1
'''

__all__ = ['f1', 'name1']
def f1():
    f2()
    f3()

def f2():
    pass

def f3():
    pass

name1 = 'aaaaa'
name2 = 'bbbbb'

