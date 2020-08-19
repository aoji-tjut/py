# try_finally_embed.py

# 此示例以控制天燃气为例,执行必须要关闭的动作
def fry_egg():
    try:
        print("打开天燃气,点燃...")
        try:
            count = int(input("请输入鸡蛋个数: "))
            print("完全煎鸡蛋,共煎好", count, '个鸡蛋')
        finally:
            print("关闭天燃气")
    except ValueError:
        print("煎蛋过程中发生错误,程序已转为正常状态!")

fry_egg()

print('程序结束')

