#   2. 输入任意一个整数,代表结束值:
#     求:
#       1 + 2 + 3 + 4 + .... + n 的和
#     并打印

s = 0  # 用来记录和
n = int(input("请输入一个结束的整数:"))

for x in range(1, n + 1):
    # print(x)
    s += x

print("1+2+3+....+", n, '=', s)

