# raise.py

def make_exception():
    print("开始....")
    # 触发ValueError类型的异常
    # raise ValueError  # ValueError是错误类型
    # raise ZeroDivisionError
    raise ImportError


    print("结束!")

try:
    make_exception()
except ValueError:
    print("接收到ValueError类型的异常,程序已转为正常状态")

print("程序结束")

