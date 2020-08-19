#   1. 写一个生成器函数:
#     def even(start, stop):
#         '''此生成器函数生成从start开始,到stop结束(不包含stop)
#          的全部偶数'''
#          ... 以下自己实现

#     for x in even(1, 10):
#        print(x)  # [2, 4, 6, 8]
#     L = [x**2 for x in even(10, 20)]
#     print(L)  # [100, 144, ...]

#     it = iter(even(3, 10))
#     print(next(it))  # 4
#     print(next(it))  # 6
#     print(next(it))  # 8
#     print(next(it))  # StopIteration


def even(start, stop):
    '''此生成器函数生成从start开始,到stop结束(不包含stop)
        的全部偶数'''
    i = start
    while i < stop:
        if i % 2 == 0:  # 是偶数
            yield i
        i += 1

for x in even(1, 10):
    print(x)  # [2, 4, 6, 8]

L = [x**2 for x in even(10, 20)]
print(L)  # [100, 144, ...]

it = iter(even(3, 10))
print(next(it))  # 4
print(next(it))  # 6
print(next(it))  # 8
print(next(it))  # StopIteration
