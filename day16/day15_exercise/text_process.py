#   3. 写一个程序, 读入任意行的文字,当输入空行时输入结束.
#     打印带有行号的输入结果
#      如:
#        请输入: hello<回车> 
#        请输入: 你好<回车> 
#        请输入: bye<回车> 
#        请输入: <回车> 
#      打印如下:
#        第1行: hello
#        第2行: 你好
#        第3行: bye

L = []
while True:
    s = input("请输入: ")
    if not s:
        break
    L.append(s)

# 打印:
for t in enumerate(L, 1):  # t = (1, "hello"")
    print("第%d行: %s" % t)

