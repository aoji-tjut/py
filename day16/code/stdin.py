# stdin.py

# 此示例示意标准输入文件的用法
import sys

s = sys.stdin.readline()

print(s)
print("len(s)=", len(s))

sys.stdin.close()  # 一旦关闭,input函数将不再可用

s2 = input("请输入文字: ")  # 内部会间接调用sys.stdin.readline
print("s2=", s2)
