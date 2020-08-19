class MyIter:
    def __init__(self,id):
        self.__id=id
    def __iter__(self):
        print("执行了iter")
        return self
    def __next__(self):
        print("执行了next")
        if self.__id+1>10:
            raise StopIteration
        self.__id+=1
        return self.__id

myiter=MyIter(1)
print("==========")
for i in myiter:
    print(i,end=" ")



print("==========")
myiter=MyIter(1)
it=iter(myiter)
for i in it:
    print(i)

print("==========")
myiter=MyIter(1)
while True:
    try:
        i=next(myiter)
    except StopIteration:
        break
    print(i)

print("==========")
def myyield():
    i=0
    while i<10:
        q=yield i
        print("yield:"+str(q))
        i=i+1
    q = yield i#如果没有这个，下面的send还没结束的时候，这个yield已经结束了，于是就会报错了
    print("yield:" + str(q))

m=myyield()

print(dir(m))

# print("send:"+str(next(m)))
print("send:"+str(m.__next__()))#__next__就是next函数
j=100
while j<110:
    print("send:"+str(m.send(j)))
    j=j+1