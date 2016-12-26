Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import functools
>>> def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s func_name %s'%(text,func.__name__)
			return (*args,**kw)
		
SyntaxError: invalid syntax
>>> def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'call %s func_name %s'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

>>> log('df')
<function decorator at 0x02BBB0B0>
>>> @log();
SyntaxError: invalid syntax
>>> @log()
def now(mytest):
	print 'this is my test %s',mytest

	

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    @log()
TypeError: log() takes exactly 1 argument (0 given)
>>> @log('yang')
def now(mytest):
	print 'this is my test %s',mytest

	
>>> now('gogo')
call yang func_name now
this is my test %s gogo
>>> #偏函数，使用functools.partial创建
>>> int2 = funtools.partial(int,base=2)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int2 = funtools.partial(int,base=2)
NameError: name 'funtools' is not defined
>>> int2 = functools.partial(int,base=2)
>>> int('123131')
123131
>>> int2(13465)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int2(13465)
TypeError: int() can't convert non-string with explicit base
>>> int2('13465')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int2('13465')
ValueError: invalid literal for int() with base 2: '13465'
>>> int2(111)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int2(111)
TypeError: int() can't convert non-string with explicit base
>>> int2('111')
7
>>> int2(111)

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int2(111)
TypeError: int() can't convert non-string with explicit base
>>> int2('111',base=16)
273
>>> int2('111',base=10)
111
>>> 
