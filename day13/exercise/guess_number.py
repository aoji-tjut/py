# 练习:
#   1. 猜数字游戏
#      随机生成一个0~100的整数,用变量x绑定
#      让用户输入一个数y,输出猜数字的结果
#        如果y大于x,则提示"您猜大了", 继续让用户输入
#        如果y小于x,则提示"您猜小了", 继续猜
#        如果y等于x,则提示"恭喜您猜对了", 打印出猜数字的次数
#          然后退出程序
#     注:
#       直到猜对才退出

import random as R
x = R.randint(0, 100)
# print(x)
times = 0  # 记录猜数字的次数 
while True:
    y = int(input("请输入(0~100)的整数: "))
    times += 1  #次数加1
    if y > x:
        print('您猜大了!')
    elif y < x:
        print('您猜小了!')
    else: # 相等
        print("恭喜您猜对了")
        break

print("您共猜了%d次" % times)



