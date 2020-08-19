# 练习:
#   写一个函数 get_age() 用来获取一个人的年龄信息
#     此函数规定用户只能输入 1~140之间的整数,如果用户输入其它
#     的数则直接触发ValueError类型的错误!
#     如:
#         def get_age()
#             ...  # 此处自己实现
#         try:
#             age = get_age()
#             print("用户输入的年龄是", age)
#         except ValueError as err:
#             print("获取年龄时发生错误,错误的原因是", err)


def get_age():
    try:
        a = int(input("请输入年龄: "))
    except ValueError:
        raise ValueError("输入内容无法转为数字!")
    if 1 <= a <= 140:
        return a
    raise ValueError("年龄值不在1~140之间")
try:
    age = get_age()
    print("用户输入的年龄是", age)
except ValueError as err:
    print("获取年龄时发生错误,错误的原因是", err)
