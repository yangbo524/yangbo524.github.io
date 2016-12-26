# -*- coding: cp936 -*-
#使用模块
#!/usr/bin/env python
#-*-coding:utf-8-*-

'a test module'

__author_='yangbobo'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello word ',args
    elif len(args) == 2:
        print 'hello %s' % args[1]
    else:
        print 'Too many arguments'

import Image
def myTestImage():
    im = Image.open('timg.jpg')
    print im.format,im.size,im.mode

class Student(object):
    #相当构造函数
    def __init__ (self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s,%s'%(self.name,self.score)

class Children(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_mychild(self):
        print '测试相关'

#类中定义 __slots__  限制实例属性
class MyChild(object):
    __slots__ =('name','age')
    

    
class Student1(object):
    def get_score(self):
        return self._score
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must')
        if score < 0 or score > 100:
            raise ValueError('score between 1 ~ 100')
        self._score = score
        
#使用@property
class Student2(object):
    
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        print 'this is the default age ',self._birth
        return 2014-self._birth
            

    def printmyLog(self):
        print 'gotomyself'

        
#多重继承
class Animal(object):
    def printAnimalMySelf(self):
         print 'this is Animal'
class mammal(Animal):
    pass
class Runnable(object):
    def printRunnable(self):
        print 'this is runnable'
class Dog(Runnable,Animal):
    def printDog(self):
        print 'this is Dog'

#定制类
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self

    def next(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a #返回下一个值
    
#按下标取元素
class Fib2(object):
    def __getitem__(self,n):
        a,b = 1,1
        for m in range(n):
            a,b = b,a+b
        return a
#定制类
class Fib3(object):
    
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            a,b = 1,1
            L = []
            for x in range(stop+1):
                if x >= start:
                    L.append(a)
                    a,b = b,a+b
            return L
#动态返回一个属性
class Student4:

    def __init__(self,myname):
        self.name = myname

    def __getattr__(self,attr):
        if attr == 'score':
            return 89

        
class Student5:
    def __init__(self,myname = 10,*name):
        self.name = name;
        self.myname = myname
    def printMyLog(self):
        print self.name,self.myname
                               
#使用元素 type() 动态创建一个Hello的class对象
class Hello(object):
    def hello(self,name='word'):
        print('Hello,%s'%name)
        

h = Hello();
print(type(Hello))
print(type(h))

#通过type创建动态创建Hello类
#先定义函数
def fn(self,name = 'bobo'):
    print('hello %s'%name)
def fn2(self,age = 14):
    print('hello %d'%age)
    
Hello = type('Hello',(object,),dict(hello = fn,hello2 = fn2))     
h = Hello()
h.hello()
h.hello2()


def myclasstest():
   # stu1 = Student('yangbo','sdsd')
   # stu1.print_score()
   # ch1 = Children('ss','dd')
   # ch1.print_mychild()
   # myChild1 = MyChild()
   # myChild1.name = '4545'
   # myChild1.age = 22

   # student11 = Student1()
   # student11.set_score(100)

   #student12 = Student2()
   #student12.birth = 45
   #print student12.birth
   #print student12.age
   #student12.printmyLog()

   #dog1 = Dog()
    #dog1.printDog()
    #dog1.printAnimalMySelf()

    #Fib()
    
    #for n in Fib():
    #    print n
        
    #f = Fib2()
    #print f[6]

    f3 = Fib3()
    print f3[0:3]    

    stu4 = Student4('yangbo')
    print stu4.name
    print stu4.score

    stu5 = Student5()
    print stu5.printMyLog()

        
if __name__ == '__main__':
    myclasstest()
    


    

    
