# mymod.py

'''此示例示意自定义模块

此模块内有两个函数和两个字符串
.... 此下省略20字
'''

def myfac(n):
    print("正在计算%d!的阶乘" % n)

def mysum(n):
    print("正在计算%d的和" % n)

name1 = "Audi"
name2 = "BYD"

print("mymod 模块被加载,模块文件为:", __file__)
print("mymod模块里的__name__属性值为:", __name__)

if __name__ == '__main__':
    # 判断 当前是否是主模块
    print("hello world!")
