#   1. 使用随机模块,随机生成6位的密码
#      可以作为密码的字符有:
#        a-z  A-Z 0-9
#      写一个程序,每次调用时能随机生成一个密码

# 生成数据源
L = [chr(x) for x in range(97, 97 + 26)] # 生成a-z
L += [chr(x) for x in range(65, 65 + 26)] # 生成A-Z
L += [chr(x) for x in range(ord('0'), ord('0')+ 10)]
# print(L)
assert len(L) == (26+26+10), "有错"

# 从数据源选择6次,每次选一个
import random
passwd_list = []
for _ in range(6):
    achar = random.choice(L)
    passwd_list.append(achar)

# 把passwd_list 转为字符串
passwd = ''.join(passwd_list)
print(passwd)

