

# 此示例示意用raise 来传递错误消息

def f1():
    print("f1开始!")
    # 此处可能触发异常
    raise ValueError("f1里的值错误!")
    print("f1结束!")

def f2():
    print("f2开始!")
    try:
        f1()  # 调用f1
    except ValueError as err:
        print("f1里发生了错误!已解决")
        raise   # 等同于 raise err
    print("f2结束!")

try:
    f2()
except ValueError as err:
    print("f2内发生错误,错误对象是", err)

print("程序结束")