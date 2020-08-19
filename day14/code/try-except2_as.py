# try-except.py


def div_apple(n):  # 分苹果
    print("现在有%d个苹果,您想分给几个人" % n)
    s = input("请输入人数: ")
    cnt = int(s)  # <<-- 可能会触发ValueError类型的错误
    result = n / cnt  # <<-- 可能触发ZeroDivisionError错误
    print("每个人分了", result, '个苹果!')

try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError as err:
    print("分苹果时的数字输入不正确,苹果被收回!")
    print("引起错误的原因是:", err)
except ZeroDivisionError:
    print("分苹果时没有人来,分苹果失败!!!")

print("程序结束")

