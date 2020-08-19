#   2. 一个球从100米高空落下,每次落地后反弹高度为原高度的一半
#     再落下,写程序
#        1) 算出皮球第10次落地后反弹多高?
#        2) 算出皮球第10次反弹后经过多少米的路程?

def jump(meter, times):
    '''meter 初始高度(米)
    times 弹跳次数
    '''
    for _ in range(times):  # 循环times次
        meter /= 2
    return meter

def distance(meter, times):
    '''meter 初始高度(米)
    times 弹跳次数
    '''
    s = 0  # 表示最终经过的路程
    for _ in range(times):
        s += meter  # 累加下落过程高度
        meter /= 2  # 先算出反弹高度 
        s += meter  # 累加反弹高度
    return s

print("小球从100米高度下落反弹10次后的高度为:",
      jump(100, 10))

print("小球从100米高度反弹10次后经历的路程是:",
      distance(100, 10))

