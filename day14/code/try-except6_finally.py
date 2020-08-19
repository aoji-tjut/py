
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
    print("分苹果失败,苹果不分了")
finally:
    print("我是finally子句里的语句,我一定会被执行!")


print("程序结束")

