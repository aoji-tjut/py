#   1. 写一个程序,输入一个字符串,把字符串的第一个字符和最后
#     一个字符去掉后, 打印出处理后的字符串

s = input('请输入一个比较长的字符串: ')
# s2 = s[1:-1]
s2 = s[1:len(s)-1]
print("结果是:", s2)