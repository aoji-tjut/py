#   2. 输入任意一个字符串,判断这个字符串是否是回文
#     回文是指中心对称的文字
#       如:
#         上海自来水来自海上
#         ABCCBA
#     随意输入一个字符串,判断是否为回文
  
#思路, 原字符串 反转 后等于源字符串,则是回文
s1 = input("请输入字符串: ")
s2 = s1[::-1]  # 反转后用s2绑定
if s1 == s2:
    print(s1, '是回文')
else:
    print(s1, '不是回文')


    