# 练习:
#   写一个函数 get_score() 来获取学生输入的成绩(0~100的整数)
#     如果输入出现异常,则此函数返回0,否则返回用户输入的成绩
#     如:
#       def get_score():
#           ....  # 此处自己实现

#       score = get_score()
#       print("学生的成绩是:", score)


def get_score():
    s = input("请输入成绩(0~100): ")
    score = int(s)
    if 0 <= score <= 100:
        return score
    return 0  # 如果这个数不在0~100之间返回0

try:
    score = get_score()
except ValueError:
    score = 0

print("学生的成绩是:", score)


