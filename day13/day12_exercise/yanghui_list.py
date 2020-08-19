#   4. 写程序打印杨辉三角(只打印6层)
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#   1 5 10 10 5 1

# 1. 先写一个给出当前行的列表,求下一行的列表的函数
def get_next_line(L):
    '''如果L=[1, 2, 1], 返回
    [1, 3, 3, 1]
    '''
    RL = [1]  # 最左侧的1# 将要返回的列表
    # 求中间的数
    for i in range(len(L)-1):  # i 代表索引
        x = L[i] + L[i + 1]
        RL.append(x)
    # 在最后加一个1
    RL.append(1)
    return RL

# 2 给出一个整数,返回当前所有行的列表
def get_yanghui_list(n):
    '''如果n为4,
    返回: 
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]'''
    L = []  # 最终要返回的列表
    line = [1]  # 初始化为第一行
    while len(L) < n:
        L.append(line)
        # 求取下一行,准备加入
        line = get_next_line(line)
    return L


# 3把列表转为字符串
def get_yanghui_string(L):
    '''如果L为:
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]
    返回
    [
        "1",
        "1 1",
        "1 2 1",
        "1 3 3 1"
    ]
    '''
    RL = []  # 最终要返回的列表
    for line in L:  # line 绑定一个行列表line = [1, 2, 1]
        temp = [str(x) for x in line]  # ['1', '2', '1']
        s = ' '.join(temp)  # s = '1 2 1'
        RL.append(s)
    return RL

# 4. 居中显示得到的字符串
def print_yanghui(L):
    ''' 如果L = ['1', '1 1', '1 2 1', '1 3 3 1']
    打印成为三角形'''
    w = len(L[-1])  # 算出三角形的宽度
    for s in L:
        print(s.center(w))

L = get_yanghui_list(6)
L2 = get_yanghui_string(L)
print_yanghui(L2)


