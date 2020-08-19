# 示例:
#   自己实现myzip 函数 功能与zip完全相同,要求只传入两个可迭代对象
#     def myzip(iter1, iter2):
#         .... # 此处自己实现
    
#     d = dict(myzip("ABC", "123"))
#     print(d)  # {'A': '1', 'B': '2', 'C': 3}

# 方法1
# def myzip(iter1, iter2):
#     return zip(iter1, iter2)

# 方法2
def myzip(iter1, iter2):
    it1 = iter(iter1)  # 拿到第一个参数的迭代器
    it2 = iter(iter2)
    while True:
        try:
            v1 = next(it1)  # 从第一个可迭代对象取一个值
            v2 = next(it2)
        except StopIteration:
            return  # 当其中任意一个迭代器不再提供数据时,结束生成
        yield (v1, v2)

d = dict(myzip("ABC", "123"))
print(d)  # {'A': '1', 'B': '2', 'C': 3}

