#   2. 写一个程序,以电子时间的格式显示时间
#      HH:MM:SS 
#      如:
#        17:52:23

import time

def clock():
    while True:
        # 得到当前时间元组
        t = time.localtime()
        # 显示到屏幕上
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        time.sleep(1)


clock()
