# generator_function2.py


# 此示例示意用生成器函数来生成一系列整数

# 生成器函数调用时返回的生成器是一次性的,
# 当生成结束后将不再提供数据
def myinteger(n):
    '''此函数为生成器函数,此函数用来生成从零开始的
    一系列整数'''
    i = 0
    while i < n:
        yield i
        i += 1

print("-------------第一种写法----------------")
gen1 = myinteger(3)
for x in gen1:
    print(x)  # 0 1 2

print('+++++')
for x in gen1:
    print(x)  # 0 1 2???

print('=============第二种写法==============')
for x in myinteger(4):
    print(x)
print('-------')
for x in myinteger(4):
    print(x)


# for x in myinteger(30000000000000000000000):
#     print(x)



