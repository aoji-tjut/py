#   3. 编写一个闹种程序,启动时设定时间(小时,分钟)
#     到时间后打印一句"时间到!!!" 然后退出程序


import time

def alarm(h, m):
    # 循环一直来判断时间是否到
    while True:
        # 得到当前时间元组
        t = time.localtime()
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        time.sleep(1)
        if t[3] == h and t[4] == m:
            print("时间到!!!")
            return


hour = int(input('请输入定时的小时: '))
minute = int(input('请输入定时的分钟: '))

alarm(hour, minute)
