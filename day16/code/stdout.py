# stdout.py

# 此示例示意标准输出和标准错误输出的用法

import sys

sys.stdout.write("你好!")
sys.stdout.write("ABC")
sys.stdout.writelines(['abc', '123'])

sys.stdout.close() # 关闭这个文件!
# sys.stdout.write("AAAAAAA")  # 出错
# print("hello world!")

sys.stderr.write("我的出现是个错误!")



