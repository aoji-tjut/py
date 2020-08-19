# file_open.py

# 此示例示意读取当前文件夹下myfile.txt这个记录文字信息的
# 文件

# 1.打开文件
try:
    # myfile = open('myfile.txt')  # 相对路径
    # myfile = open('/home/tarena/aid/pbase/day16/code/myfile.txt')  # 绝对路径
    myfile = open('../code/myfile.txt')  # 相对路径
    print("文件打开成功")
    # 2. 读/写文件

    # 3. 关闭文件
    myfile.close()
    print("文件关闭成功")
except OSError:  # OSError表示无法进行输入输出
    print('文件打开失败!')

