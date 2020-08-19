# generator_function.py


# 此示例示意用生成器函数来生成一系列整数
def myinteger(n):
    '''此函数为生成器函数,此函数用来生成从零开始的
    一系列整数'''
    i = 0
    while i < n:
        yield i
        i += 1

for x in myinteger(30000000000000000000000):
    print(x)



