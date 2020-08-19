class Some:
    __slots__ = ['a','b']

s=Some()
s.a="aaa"
s.b="bbb"
print(s.a+"\t"+s.b)

# s.c="xxx" #此属性由于slots没有预先配置，因此不可加入

print("="*50+"1")
#=======================================================

class Some:
    __slots__ = ['a','b','__dict__']

s=Some()
s.a="aaa"
s.b="bbb"

s.c="xxx"

print(s.__dict__)
print(s.a+"\t"+s.b+"\t"+s.c)
print(Some.__dict__)
