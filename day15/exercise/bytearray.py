# 练习:
#   写一个程序,从键盘输入一段字符串,用变量s绑定
#     1. 将此字符串转为字节串用变量b绑定,并打印出来
#     2. 打印字符串s的长度和字节串的长度
#     3. 将字节串再转换为字符串变量s2绑定,判断s2与s是否相同
#     再将上述字节串改为字节数组完成上面的练习

s = input("请输入字符串: ")
b = bytearray(s, 'utf-8')
print("str(s)=", len(s))
print("len(b)=", len(b))
s2 = b.decode()  # 等同于 s2 = b.decode('utf-8')
if s == s2:
    print("s == s2")
else:
    print("s != s2")



