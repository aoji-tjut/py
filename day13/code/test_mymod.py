# test_mymod.py

# 此模块将作为主模块来导入mymod模块
# 用mymod 里的函数和数据,组成我的程序

import mymod   # 不加.py,会自动去找mymod.py文件

mymod.myfac(6)
mymod.mysum(100)
print(mymod.name2)

from mymod import name1, mysum
print(name1)  # Audi
mysum(200)  # 正在计算200的和

from mymod import *
myfac(10)
print(name2)

