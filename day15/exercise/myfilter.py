# 2. 试写一个生成器函数 myfilter,要求此函数与系统内建的
#     filter函数功能相同
#     如:
#     def myfilter(fn, iterable):
#         ..... # 此处自己实现
    
#     for x in myfilter(lambda y:y%2==1, range(10)):
#         print(x)  # 1 3 5 7 9
    
# 方法1 用 for 语句实现
# def myfilter(fn, iterable):
#     for x in iterable: 
#         if fn(x):
#             yield x

# 方法2,用while语句实现
def myfilter(fn, iterable):
    it = iter(iterable)  # 先拿到迭代器
    while True:
        try:
            x = next(it)  # 取值
            if fn(x):
                yield x
        except StopIteration:
            return  # 生成结束

for x in myfilter(lambda y: y % 2 == 1, range(10)):
    print(x)  # 1 3 5 7 9
    