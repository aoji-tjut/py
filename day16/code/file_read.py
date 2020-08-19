# file_read.py


# 此示例示意用文件流对象的读方法来获取myfile.txt内的
# 字符数据
try:
    fr = open("/home/tarena/aid/pbase/day16/code/myfile.txt")

    # 2. 读取文件内容
    s = fr.read()  # 读取全部文件内容
    print(s)
    print("len(s)=", len(s))

    fr.close()
except OSError:
    print("文件打开失败")