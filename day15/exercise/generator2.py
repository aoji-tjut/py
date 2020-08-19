# 1. 已知有列表:
#     L = [2, 3, 5, 7]
#     1) 写一个生成器函数,让此函数能够动态提供数据, 提供的数据
#       为原列表的数字的平方+1
#     2) 写一个生成器表达式,让此表达式能够动态提供数据,提供的数
#       据依旧为原列表的数字的平方+1
#     3) 写一个列表,此列表内的数据为原列表的数字的平方+1

L = [2, 3, 5, 7]
# 1) 写一个生成器函数,让此函数能够动态提供数据, 提供的数据
#     为原列表的数字的平方+1
def mygenerator(lst):
    for x in lst:
        yield x ** 2 + 1

for x in mygenerator(L):
    print(x)  # 5 10 26 50


# 2) 写一个生成器表达式,让此表达式能够动态提供数据,提供的数
#     据依旧为原列表的数字的平方+1
for x in (y**2+1 for y in L):
    print(x)  # 5, 10, 26, 50

# 3) 写一个列表,此列表内的数据为原列表的数字的平方+1
L2 = [x**2+1 for x in L]
print(L2)
L3 = list(map(lambda x:x**2+1, L))
print(L3)