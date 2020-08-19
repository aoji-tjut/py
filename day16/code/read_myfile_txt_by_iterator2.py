# read_myfile_txt_by_iterator.py


# 此示例示意文件流对象是可迭代对象
try:
    f = open("myfile.txt")
    # 在此处读取所有的行,打印在屏幕上
    # 1. 用循环方式来读
    # while True:
    #     s = f.readline()
    #     if s == '': # 到达行尾
    #         break
    #     print(s)
    # 2. 用迭代方式读,见read_myfile_txt_by_iterator2.py
    for s in f:
        print(s)

    f.close()
except OSError:
    print("打开文件失败")