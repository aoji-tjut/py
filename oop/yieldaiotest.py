import queue
import time

myque = queue.Queue(1)
def runner():
    print("start...")
    yield getinput()
    print("ok")


def getinput():
    time.sleep(1)
    print("xxxx")
    time.sleep(1)
    myque.put("xxx")

if __name__=="__main__":

    r=runner()
    next(r)
    res=""
    while(res!="xxx"):
        res = myque.get()
    try:
        next(r)
    except:
        pass
#==================================================================
print("="*50)
def mycoroutines(mth):
    def wrapper(self,*args,**kwargs):
        print(mth)
        return mth(self,*args,**kwargs)#mth(s)
    return wrapper

def getinput():
    time.sleep(1)
    print("xxxx2")
    time.sleep(1)
    myque.put("xxx2")

class Some:
    @mycoroutines
    def runner(self):
        print("start2...")
        yield getinput()
        print("ok2")

if __name__=="__main__":

    s=Some()
    p=s.runner()
    next(p)
    res=""
    while(res!="xxx2"):
        res = myque.get()
    try:
        next(p)
    except:
        pass


