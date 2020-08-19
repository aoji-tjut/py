#=====================函数装饰函数===============================
import sys


def decorate(func):
    def wrapper():
        print("定义一个装饰器")
        func()
    return wrapper
def text1():
    print("text1")

decorate(text1)()

print("="*50+"1")
#=======================================================

def decorate(func):
    def wrapper():
        print("定义一个装饰器")
        func()
    return wrapper
@decorate             #@xxx其实就是 xxx(),并且把紧随的内容当做参数传入
def text1():
    print("text1")

text1()

print("="*50+"2")
#=======================================================

def decorate(name):
    def wrapper(func):
        def sub_wrapper():
            print("定义一个带参数的装饰器",name)
            func()
        return sub_wrapper
    return wrapper

def text1():
    print("text1")

decorate(name="python")(text1)()

print("="*50+"3")
#=======================================================

def decorate(name):
    def wrapper(func):
        def sub_wrapper():
            print("定义一个带参数的装饰器",name)
            func()
        return sub_wrapper
    return wrapper

@decorate(name="python")
def text1():
    print("text1")

text1()



print("="*50+"4")
#=======================================================

def decorate(name):
    def wrapper(func):
        def sub_wrapper(arg):
            print("定义一个带参数的装饰器",name)
            func(arg)
        return sub_wrapper
    return wrapper

def text1(arg):
    print("text1",arg)

decorate(name="python")(text1)("xxx")

print("="*50+"5")
#=======================================================

def decorate(name):
    def wrapper(func):
        def sub_wrapper(arg):
            print("定义一个带参数的装饰器",name)
            func(arg)
        return sub_wrapper
    return wrapper

@decorate(name="python")
def text1(arg):
    print("text1",arg)

text1("xxx")

print("="*50+"6")

#=======================================================

def wrapper(func):
    def sub_wrapper(arg):
        print("定义一个带参数的装饰器",arg)
        func(arg)
    return sub_wrapper

@wrapper
def text1(arg):
    print("text1",arg)


text1("xxx")

print("="*50+"7")
#===========================================
def decorate(func):
    def wrapper():
        func()
    return wrapper

def decoratex(func):
    def wrapper():
        func()
    return wrapper

def test11():
    print("lllll")

decorate(decoratex(test11))()

print("="*50+"8")
#===========================================
def decorate(func):
    def wrapper():
        func()
    return wrapper

def decoratex(func):
    def wrapper():
        func()
    return wrapper

@decorate
@decoratex
def test11():
    print("lllll")

test11()

print("="*50+"9")
#===========================================
class DDD():
    @staticmethod
    def decorate(func):
        def wrapper():
            func()
        return wrapper


@DDD.decorate
def test11():
    print("oooo")

test11()

# print(DDD.__dict__)

print("="*50+"10")
#=====================首先来了解call的作用======================
class Testcall:
    def __init__(self):
        print("init")
    def __call__(self, *args, **kwargs):
        print("call")

testcall=Testcall()

testcall() #call其实就是运算符-> '()'
print("="*50+"10.1")

#=====================后面是类装饰器======================
#=====================函数装饰类===============================

def clsdeco(clz):
    class Test:
        def __init__(self):
            self.couse=clz()

        def getContent(self):
            return "couse: "+self.couse.getContent()

    return Test

@clsdeco
class Eng:
    def getContent(self):
        return "ENG"

s=Eng()
print(s.getContent())

# c=clsdeco(Eng)
# s=c()
# print(s.getContent())

print("="*50+"11")
#=========================================================
#==================类装饰函数－－－－－需要实现call,调用被装饰者call会被调用===============================

class desc1:
    def __init__(self,func):
        print("￥￥￥￥￥")
        self.func=func
    def __call__(self, *args, **kwargs):
        print("～～～～")
        res=self.func(args[0])
        return res

@desc1
def some(arg):
    return arg+1

r=some(1)
print(r)

# s=desc1(some)
# r=s.__call__(1)
#
# print(r)


print("="*50+"12")
#=========================================================
#==================类装饰类－－－－－被装饰类定义对象的时候，装饰器的call会被调用===============================

class decro1:
    def __init__(self,clz):
        self.clz=clz #Eng1

    def __call__(self, *args, **kwargs):
        class prof:
            def __init__(self,couse):
                self.couse=couse     #couse存储了Eng1的对象

            def getContent1(self):
                return self.couse.getContent1()+"|ZH|MATH"
        return prof(self.clz())

@decro1
class Eng1:
    def __init__(self):
        print("00000000")
    def getContent1(self):
        return "ENG"

class Eng2:
    def getContent1(self):
        return "ENG2"

c=Eng1()
print(c.getContent1())
print("--------------------------")

d=decro1(Eng2)
c=d.__call__()
print(c.getContent1())

print("="*50+"13")
#=========================================================
#=====================对象装饰方法－－－－－call被调用===============================
class Xxx():
    def __init__(self):
        pass

    def __call__(self, func):
        def _call(*args, **kw):
            return func(*args, **kw)

        return _call

class Yyy(object):
    @Xxx()                   #执行顺序是:Xxx()得到一个对象x,然后再@x相当于执行了对象x的call方法，并且将被修饰方法的类对应的方法传入了call，为了可以调用方法，因此隐含的实现了被修饰方法的类对象
    def dis(self, test, ids):
        print('yyyyyyy: '+test+" "+ids)

Xxx().__call__(Yyy().dis)("aaa","bbb")

Yyy().dis("aaa","bbb")

print("="*50+"14")
#=========================================================
#=====================函数装饰方法===============================


def log(mth):
    def wrapper(self,*args,**kwargs):
        print(self,args,kwargs)
        return mth(self,*args,**kwargs)#mth(s,1,2)
    return wrapper

class Some:
    @log
    def doit(self,a,b):
        return a+b

    def doit2(self,a,b):
        return a+b

s=Some()
print(s.doit(1,2))

s=Some()
print(log(Some.doit2)(s,1,2))

print("="*50+"15")
#=========================================================
#=====================类装饰方法－－－－－这个例子要先看discriptor后才能看懂===============================
class lazy():
    def __init__(self, func):
        print("#####")
        self.func = func

    def __get__(self, instance, cls):
        print("=====",instance,cls)
        val = self.func(instance)
        setattr(instance, self.func.__name__, val) #相当于在get中将Circle类的方法area修改位名字相同的属性，并且值是恒定的(调用原area返回的值)
        return val


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @lazy
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2


c = Circle(4)
print("+++++")
print(c.radius)
print("-----")
print(c.area)
print("111")
print(c.area)
print("222")
print(c.area)

print("="*50+"16")
#===========模仿classmethod===============================
class classmath:
    def __init__(self,mth):
        self.mth=mth

    def __get__(self, instance, owner):  #利用get的第三个参数，来修改调用类方法的第一个参数，来实现类方法
        def wrapper(*args,**kwargs):
            return self.mth(owner,*args,**kwargs)

        return wrapper




class Other:
    @classmath
    def doit(clz,a,b):
        print(clz,a,b)
        return a+b

class Other1:
    def doit(clz,a,b):
        print(clz,a,b)
        return a+b

print(Other.doit(1,2))
o=Other1()
c=classmath(Other1.doit)
print(classmath.__get__(c,o,Other1)(1,2))

o=Other()
print(o.doit(1,2))

print("="*50+"17")
#===========模仿staticmethod===============================

class my_staticmethod(object):
    def __get__(self, obj, type=None):     #遇上一个例子实际是一样的思路
        def wrapper(*args, **kwargs):
            return self.function(*args, **kwargs)
        return wrapper

    def __init__(self, function):
        self.function = function


class Class2(object):
    @my_staticmethod
    def get_user(x):
        return x, "get_user"

print(Class2.get_user("###"))

print("="*50+"18")
#===========模仿ContextManager===============================

class MyException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Res:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print(self.name+" enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.name+" exit")
        return False

class MyGeneratorContextManager():
    def __init__(self, gen):
        print("__init__ called")
        self.gen = gen

    def __enter__(self):
        print("__enter__ called")
        return self.gen.__next__()

    def __exit__(self, type, value, traceback):#__exit__如果return true就会结束掉异常
        # if type is None:
        #     try:
        #         next(self.gen)
        #     except StopIteration:
        #         return
        # else:
        try:
            self.gen.throw(type, value, traceback)
        except:
            return True


def MyContextManager(func):
    def tmpf(*args):
        print("func info:", func)
        return MyGeneratorContextManager(func(*args))

    return tmpf


@MyContextManager
def foo(ex):
    try:
        yield
    except ex as e:
        print("+++++",e)

i=0
with foo(MyException),Res("withtest")  as tmp:
    print("+++")
    if i == 0:
        raise MyException("错了错了错了")
    print("---")


print("end!!")

