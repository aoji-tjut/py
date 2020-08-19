# file_write.py


try:
    fw = open("mynote.txt", 'w')
    print("打开文件成功!")

    fw.write("你好!")
    print("写入文件成功能")
    fw.write("ABC")
    fw.writelines( ["这是第一个字符串", '这是第二个字符串'])
    fw.write("1234\n")
    fw.write("这是第二行!")

    fw.close()
    print("关闭文件成功")
except OSError:
    print("打开写文件失败!")