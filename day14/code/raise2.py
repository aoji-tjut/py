# raise2.py

def make_exception():
    print("开始....")

    error = ValueError("这是我故意制造的一个错误")
    raise error  # 触发错误对象

    print("结束!")

try:
    make_exception()
except ValueError as err:  # err用来绑定错误对象
    print("接收到ValueError类型的异常,程序已转为正常状态")
    print("发生错误的原因是:", err)

print("程序结束")

