#   写一个成生器函数myenumerate,要求此函数的功能与内建的
#       enumerate 函数功能完全相同
#     如:
#         def myenumerate(iterable, start=0):
#              .... 以下自己实现
#     测试:
#         d = dict(myenumerate("ABCDE", 1))
#         print(d)  # {1:'A', 2:'B', 3:'C', ...}


# 方法1 返回一个zip对象
# def myenumerate(iterable, start=0):
#     end = start + len(iterable)  # 求终止点
#     return zip(range(start, end), iterable)

# 方法2
def myenumerate(iterable, start=0):
    i = start  # 开始索引
    for x in iterable:
        yield (i, x)  # 生成一个元组
        i += 1


d = dict(myenumerate("ABCDE", 1))
print(d)  # {1:'A', 2:'B', 3:'C', ...}