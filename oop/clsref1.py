#=====================自省机制=======================================
from pprint import pprint

class Some:
    print("fjsdhfhsdhfksdfhj")
    __pppp=""
    def __init__(self,xx,pp):
        self.xx=xx
        self.__pp=pp

    def xxx(self):
        print("---xxx---")
        pass

pprint(dir(Some))
print()
s=Some("aaa","bbb")
s.ppppppp=1000
print(s.__dict__)
print(dir(s))
print(getattr(s,'xx'))
# getattr(s,'__pp')
# True为方法 false为属性
print( callable(getattr(s,'xxx')))
print( callable(getattr(s,'__doc__')))
methodLIst = [method for method in dir(s) if callable(getattr(s,method))]
print(methodLIst)

print("="*50+"1")
#=====================自省机制=======================================

pprint(globals())
print()
import sys

# pprint(globals())
# print()
s = globals()["Some"]
s("aaa","bbb").xxx()
