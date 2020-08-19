# 练习:
#   写一个电话号码本存储程序,程序启动时循环输入
#      姓名和电话号码,把姓名和电话号码存入文件phone_book.txt
#     如:
#       请输入姓名: 小张
#       请输入电话号码: 13888888888
#       请输入姓名: 小赵
#       请输入电话号码: 13999999999
#       请输入姓名: <回车>结束输入
#     保存后文件内容如下:
#       小张,13888888888
#       小赵,13999999999

def input_info():
    L = []  # 用来保存 ('姓名', '电话号码')
    while True:
        name = input("请输入姓名: ")
        if not name:
            break
        number = input("请输入电话号码: ")
        t = (name, number)  # 创建个元组
        L.append(t)  # 加入列表
    return L

def write_to_file(L):
    try:
        f = open("phone_book.txt", 'w')
        # 开始写
        for name, number in L:
            f.write(name)
            f.write(',')
            f.write(number)
            f.write('\n')

        f.close()
    except OSError:
        print("写文件失败!")

L = input_info()
print(L)

write_to_file(L)




