# iterator.py

# 此示例示意用迭代器来代替for语句实现对可迭代对象的数据遍历
L = [11, 13, 17, 19]

# 1. 用for实现遍历
for x in L:
    print(x)  # 11 13 17 19

print('-----------------------------')
# 2. 用迭代器,while循环等实现与1相同的功能
it = iter(L)  # 先从L中拿到L的迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
