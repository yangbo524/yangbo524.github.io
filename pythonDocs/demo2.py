Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #对List进行排序
>>> sorted([36,5,12,78,4])
[4, 5, 12, 36, 78]
>>> #利用sorted实现倒序排序
>>> def reversed_cmp(x,y):
	if(x > y):
		reteurn -1
	if(x < y):
		return 1
	return 0

>>> sorted([36,5,78,14,6],reversed_cmp)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sorted([36,5,78,14,6],reversed_cmp)
  File "<pyshell#9>", line 3, in reversed_cmp
    reteurn -1
NameError: global name 'reteurn' is not defined
>>> def reversed_cmp(x,y):
	if(x > y):
		return -1
	if(x < y):
		return 1
	return 0

>>> sorted([5,45,21,4,78],reversed_cmp)
[78, 45, 21, 5, 4]
>>> #字符串排序，先忽略大小写
>>> def reversed_char(char1,char2):
	c1 = char1.upper()
	c2 = char2.upper()
	if(c1 < c2):
		return -1
	if(c1 > c2)
	
SyntaxError: invalid syntax
>>> def reversed_char(char1,char2):
	c1 = char1.upper()
	c2 = char2.upper()
	if(c1 < c2):
		return -1
	if(c1 > c2):
		return 1
	return 0

>>> sorted(['ABDHC'，'EDKK','cDED','LJdH'],reversed_char)
SyntaxError: invalid syntax
>>> sorted(['ABDHC','EDKK','cDED','LJdH'],reversed_char)
['ABDHC', 'cDED', 'EDKK', 'LJdH']
>>> #函数作为返回值
>>> def lazy_sum(*args):
	def sum():
		sum_number = 0;
		for n in args:
			sum_number = n +sum_number
		return sum_number
	return sum

>>> fun = lazy_sum([1,2,3,4])
>>> fun
<function sum at 0x02D67C70>
>>> fun()

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    fun()
  File "<pyshell#36>", line 5, in sum
    sum_number = n +sum_number
TypeError: can only concatenate list (not "int") to list
>>> fun = lazy_sum(1,2,3,4)
>>> fun
<function sum at 0x02D64CB0>
>>> fun()
10
>>> fun1 = lazy_sum(1,2,3,4)
>>> fun2 = lazy_sum(1,2,3,4)
>>> fun1 == fun2
False
>>> #匿名函数
>>> map(lambda x:x*x,[123456])
[15241383936L]
>>> f = lambda x:x*x
>>> f
<function <lambda> at 0x02D670B0>
>>> map(f,[123456])
[15241383936L]
>>> #匿名函数作为返回值
>>> def build(x,y):
	return lambda x:x*x

>>> build(1,3)
<function <lambda> at 0x02D67D30>
>>> f = build(x,y)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    f = build(x,y)
NameError: name 'x' is not defined
>>> f = build(4,4)
>>> f
<function <lambda> at 0x02D67D70>
>>> map(f,[1,3,4])
[1, 9, 16]
>>> #装饰器模式
>>> def log(func):
	def wrapper(*args,**kw):
		print 'call ',func._name_
		return func(*args,**kw)
	return wrapper

>>> @log
    def now:
	    
  File "<pyshell#69>", line 2
    def now:
   ^
IndentationError: unexpected indent
>>> @log
    def now:
	    
  File "<pyshell#70>", line 2
    def now:
   ^
IndentationError: unexpected indent
>>> @log
def now:
	
SyntaxError: invalid syntax
>>> @log
def now():
	print '2013-ds'

	
>>> now
<function wrapper at 0x02D67DB0>
>>> now()
call 

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    now()
  File "<pyshell#66>", line 3, in wrapper
    print 'call ',func._name_
AttributeError: 'function' object has no attribute '_name_'
>>> def log(func):
	def wrapper(*args,**kw):
		print 'call ',func.name
		return func(*args,**kw)
	return wrapper

>>> now()
call 

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    now()
  File "<pyshell#66>", line 3, in wrapper
    print 'call ',func._name_
AttributeError: 'function' object has no attribute '_name_'
>>> def log(func):
	def wrapper(*args,**kw):
		print 'call ',func.name
		return func(*args,**kw)
	return wrapper

>>> @log
def now():
	print '1231313'

	
>>> now()
call 

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    now()
  File "<pyshell#81>", line 3, in wrapper
    print 'call ',func.name
AttributeError: 'function' object has no attribute 'name'
>>> deflog(func):
	
SyntaxError: invalid syntax
>>> def log(func):
		def wrapper(*args,**kw):
			print 'call ',func.__name__
			return func(*args,**kw)
		return wrapper

	
>>> @log
def now():
	print '456798'

	
>>> now()
call  now
456798
>>> #如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
>>> def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s,%s():'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log('execute')
def now():
	print '2013-12-25'

	
>>> now()
execute,now():
2013-12-25
>>> def log(text):
	def decorator(func):
		def wrapper(**kw):
			print '%s,%s()'%(text,func.__name__)
			return func(**kw)
		return wrapper
	return decorator

>>> @log('exemytest')
def now():
	print 'yangbo'

	
>>> now()
exemytest,now()
yangbo
>>> import functools
>>> def log(*func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call%s():'func.__name__
		
SyntaxError: invalid syntax
>>> def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call%s():'func.__name__
		
SyntaxError: invalid syntax
>>> def log(*func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call%s():'%func.__name__
		return func(*args,**kw)
	return wrapper

>>> @log()
def now():
	print 'test'

	

Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    @log()
  File "<pyshell#133>", line 2, in log
    @functools.wraps(func)
  File "D:\Python27\lib\functools.py", line 33, in update_wrapper
    setattr(wrapper, attr, getattr(wrapped, attr))
AttributeError: 'tuple' object has no attribute '__module__'
>>> @log
def now():
	print 'test'

	

Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    @log
  File "<pyshell#133>", line 2, in log
    @functools.wraps(func)
  File "D:\Python27\lib\functools.py", line 33, in update_wrapper
    setattr(wrapper, attr, getattr(wrapped, attr))
AttributeError: 'tuple' object has no attribute '__module__'
>>> def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call%s():'%func.__name__
		return func(*args,**kw)
	return wrapper

>>> @log
def now():
	print 'test'

	
>>> now()
callnow():
test
>>> def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log
def now():
	print 'yang test'

	
>>> now()

Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    now()
TypeError: decorator() takes exactly 1 argument (0 given)
>>> now('test')

Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    now('test')
  File "<pyshell#155>", line 3, in decorator
    @functools.wraps(func)
  File "D:\Python27\lib\functools.py", line 33, in update_wrapper
    setattr(wrapper, attr, getattr(wrapped, attr))
AttributeError: 'str' object has no attribute '__module__'
>>> def log(text = None):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator

>>> def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log('123')
def now():
	print 'yangbo'

	
>>> now();
call now():
yangbo
>>> @log
def now():
	print 'ceshi'

	
>>> now();

Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    now();
TypeError: decorator() takes exactly 1 argument (0 given)
>>> def log(text == None):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator
SyntaxError: invalid syntax
>>> def log(text = None):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log
def now():
	print 'yangbo'

	
>>> now()

Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    now()
TypeError: decorator() takes exactly 1 argument (0 given)
>>> def log(text = 'sss'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log
def now():
	print 'yang'

	
>>> now()

Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    now()
TypeError: decorator() takes exactly 1 argument (0 given)
>>> @log()
def now():
	print 'yang'

	
>>> now()
call now():
yang
>>> def log(text = None):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log()
def now():
	print 'bobo'

	
>>> now()
call now():
bobo
>>> now('1456')
call now():

Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    now('1456')
  File "<pyshell#195>", line 6, in wrapper
    return func(*args,**kw)
TypeError: now() takes no arguments (1 given)
>>> @log('456465')
def now():
	print 'bobo'

	
>>> now()
call now():
bobo
>>> 
