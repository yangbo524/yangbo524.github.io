Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #��ͨ���
>>> print

>>> #����ַ���
>>> print 'yangbo'
yangbo
>>> #���int����
>>> print 78979
78979
>>> #���boolean����
>>> print True
True
>>> print False
False
>>> #���float��
>>> print 2.123
2.123
>>> #unicode����
>>> ord('A')
65
>>> chr(65)
'A'
>>> #�ַ�ƴ��
>>> print 'my name is %s' % 'yangbo'
my name is yangbo
>>> print 'my name is ','yangbo'
my name is  yangbo
>>> #list
>>> classmates=['a','b','c']
>>> classmates
['a', 'b', 'c']
>>> #list ����
>>> len(classmates)
3
>>> #����������listԪ��
>>> classmates[0],classmates[1]
('a', 'b')
>>> classmates[2]
'c'
>>> #�����һ��Ԫ����ǰȡ
>>> classmates[-1]
'c'
>>> classmates[-2]
'b'
>>> #׷��listԪ�ص�ĩβ
>>> classmates.append('e')
>>> classmates
['a', 'b', 'c', 'e']
>>> #��Ԫ�ز���ָ����ְ
>>> #��Ԫ�ز���ָ��λ��
>>> classmates.insert(1,'f')
>>> classmates
['a', 'f', 'b', 'c', 'e']
>>> #ɾ��listĩβԪ��
>>> classmates.pop()
'e'
>>> classmates
['a', 'f', 'b', 'c']
>>> #ɾ��ָ��λ��Ԫ��
>>> classmates.pop(1)
'f'
>>> classmates
['a', 'b', 'c']
>>> #��ĳ��Ԫ���滻�ɱ��Ԫ��
>>> classmates[0] = 'f'
>>> classmates
['f', 'b', 'c']
>>> #list�п��԰�����ͬ���͵�Ԫ��
>>> L = ['a',1,True]
>>> L
['a', 1, True]
>>> #list�п��԰�����һ��list
>>> s = ['333',['a',b]]

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s = ['333',['a',b]]
NameError: name 'b' is not defined
>>> s = ['333',['a','b']]
>>> s
['333', ['a', 'b']]
>>> p = ['asp','php']
>>> s = ['python','java',p,'scheme']
>>> s
['python', 'java', ['asp', 'php'], 'scheme']
>>> #tuple Ԫ�飬��list���ƣ�һ����ʼ�������޸�
>>> classmates = ('a','b','c')
>>> classmates
('a', 'b', 'c')
>>> #����յ�tuple
>>> t = ()
>>> t
()
>>> #����ֻ��1��Ԫ�ص�tuple
>>> t = (1,)
>>> t
(1,)
>>> #tuple�п��԰���list
>>> mylist = ['a',False]
>>> mytuple = ('tuple',False,mylist)
>>> mytuple
('tuple', False, ['a', False])
>>> #list�а���tuple
>>> mytuple = ('ddd',True)
>>> mylist = ['bbb','ooo',mytuple]
>>> mylist
['bbb', 'ooo', ('ddd', True)]
>>> #�����ж�
>>> age = 18
>>> if age >= 10 ��
SyntaxError: invalid syntax
>>> age = 18
>>> if age >= 10 :
	print 'your age is ',age
else:
	print 'laster age',age

	
your age is  18
>>> 
>>> age = 35
>>> if 10 <= age < 15:
	print 'age < 15',age
elif 15<= age < 20:
	print 'age < 20',age
else age >= 20:
	
SyntaxError: invalid syntax
>>> if 10 <= age < 15:
	print 'age < 15',age
elif 15<= age < 20:
	print 'age < 20',age
else :
	print 'age else',age

	
age else 35
>>> #if����д �жϷǿ�
>>> if x:
	print True

	

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    if x:
NameError: name 'x' is not defined
>>> ifx:
	print True
	
SyntaxError: invalid syntax
>>> x = '10'
>>> if x:
	print True

	
True
>>> #for ѭ��
>>> names = ['78',True,90]
>>> for name in names:
	print name

	
78
True
90
>>> #�ֵ�dict
>>> d = {'key1':'value1','key2':'value2'}
>>> d
{'key2': 'value2', 'key1': 'value1'}
>>> print d['key1']
value1
>>> #�ֵ�Ԫ�ظ�ֵ
>>> d['key1'] = value56

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    d['key1'] = value56
NameError: name 'value56' is not defined
>>> d['key1'] = 'value56'
>>> d
{'key2': 'value2', 'key1': 'value56'}
>>> #��ȡkey��value
>>> d.get('key1')
'value56'
>>> #�ж�key�Ƿ����
>>> d.has_key('key2')
True
>>> #ɾ��ĳ��
>>> d.pop('key1')
'value56'
>>> d
{'key2': 'value2'}
>>> #set ��һ��key�ļ��ϣ������洢value�� key���ظ�
>>> #����set����Ҫ�ṩlist��Ϊ���뼯��
>>> s = set([1,2,3])
>>> s
set([1, 2, 3])
>>> #���Ԫ�ص�set��
>>> s.add(0)
>>> s
set([0, 1, 2, 3])
>>> s.add(9)
>>> s
set([0, 1, 2, 3, 9])
>>> #ɾ��Ԫ��
>>> s.r

Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    s.r
AttributeError: 'set' object has no attribute 'r'
>>> s.remove(1)
>>> s
set([0, 2, 3, 9])
>>> #list����
>>> a = ['c','b','a']
>>> a.sort()
>>> a
['a', 'b', 'c']
>>> #�ַ����滻
>>> a = 'abcdef'
>>> b = a.replace('a','A')
>>> b
'Abcdef'
>>> #���ú���
>>> abs(100)
100
>>> #���庯��
>>> def my_abs(x):
	if x>= 0:
	    return x
	else:
	    return -x

	
>>> my_abs(10)
10
>>> my_abs(-10)
10
>>> #����һ��ʲô�¶������պ�������pass���
>>> def nop():
	pass

>>> nop()
>>> #�����������������ͼ��
>>> def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operandtype')
	if x>= 0:
		return x
	else:
		return -x

	
>>> my_abs(10)
10
>>> my_abs('10')

Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    my_abs('10')
  File "<pyshell#164>", line 3, in my_abs
    raise TypeError('bad operandtype')
TypeError: bad operandtype
>>> #���庯��Ĭ�ϲ������˲����ɴ��ɲ���
>>> def power(x,n = 2):
	s = 1
	while n>0:
		n = n - 1
		s = s * x
	return s

>>> power(5)
25
>>> power(5,2)
25
>>> power(5,9)
1953125
>>> power(5,1)
5
>>> #����Ĭ�ϲ�������ָ�򲻱����
>>> def add_end(L = None):
	if L is None:
		L = []
	L.
	
SyntaxError: invalid syntax
>>> def add_end(L = None):
	if L is None:
		L = []
	return L

>>> add_end(['a','b','c'])
['a', 'b', 'c']
>>> add_end()
[]
>>> #�ɱ����
>>> def calc(*number):
	sum = 0
	for in number:
		
SyntaxError: invalid syntax
>>> def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	reteurn sum
	
SyntaxError: invalid syntax
>>> def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

>>> # ����ǰ��* ����ɱ����������ʱҲ���*
>>> calc(1,2,3)
14
>>> calc(1,2)
5
>>> #����list��tupleʱ���*
>>> s = ['1','3','5']
>>> calc(*s)

Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    calc(*s)
  File "<pyshell#197>", line 4, in calc
    sum = sum + n*n
TypeError: can't multiply sequence by non-int of type 'str'
>>> s = [1,3,5]
>>> calc(*s)
35
>>> m = (1,2,3)
>>> calc(*m)
14
>>> #�ؼ��ֲ���
>>> def person(a,b,**kw):
	print 'a:',a,'b:',b,"other:",kw

	
>>> person('A','B')
a: A b: B other: {}
>>> person('A','B',mykey='myvalue')
a: A b: B other: {'mykey': 'myvalue'}
>>> dist = {'key1':'value1','key2':'value2'}
>>> person('A','B',**dist)
a: A b: B other: {'key2': 'value2', 'key1': 'value1'}
>>> person('A','B',mykey1 ='first1',mykey2 = 'first2',mykey3 = 'first3')
a: A b: B other: {'mykey3': 'first3', 'mykey2': 'first2', 'mykey1': 'first1'}
>>> person('A','B',mykey1 = dist.get('key1'),mykey2 = dist.get('key2'))
a: A b: B other: {'mykey2': 'value2', 'mykey1': 'value1'}
>>> #���庯���������ñ�ѡ������Ĭ�ϲ������ɱ�����͹ؼ��ֲ�������4�ֲ���������һ��ʹ�ã�����ֻ������ĳЩ��������ע�⣬���������˳������ǣ���ѡ������Ĭ�ϲ������ɱ�����͹ؼ��ֲ�����
>>> def func(a,b,c =0,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

	
>>> func(1,2)
a= 1 b= 2 c= 0 args= () kw= {}
>>> func(1,2,33,'a','v','m',key = 'mykey')
a= 1 b= 2 c= 33 args= ('a', 'v', 'm') kw= {'key': 'mykey'}
>>> my_tuple = ('a','b','java','php','python')
>>> my_dict = {'key1':'value1','key2':'value2'}
>>> func(*my_tuple,**my_dict)
a= a b= b c= java args= ('php', 'python') kw= {'key2': 'value2', 'key1': 'value1'}
>>> my_list = ['a','b','java','php','python']
>>> func(*my_list,**my_dict)
a= a b= b c= java args= ('php', 'python') kw= {'key2': 'value2', 'key1': 'value1'}
>>> 
my_list.append('Android')
>>> func(*my_list,**my_dict)
a= a b= b c= java args= ('php', 'python', 'Android') kw= {'key2': 'value2', 'key1': 'value1'}
>>> #�ݹ麯��
>>> def fuct(n):
	if n == 1
	
SyntaxError: invalid syntax
>>> def fuct(n):
	if n == 1:
		return 1
	return n*fuct(n-1)

>>> fuct(10)
3628800
>>> def fuct_def(product,count,max):
	if(count > max):
		return product
	return fuct_def(product*count,count+1,max)

>>> def fuct(n)
SyntaxError: invalid syntax
>>> def fuct(n):
	return fuct_def(1,1,10)

>>> fuct(10)
3628800
>>> fuct(1000)
3628800
>>> def fuct(n):
	return fuct_def(1,1,n)

>>> fuct(10)
3628800
>>> fuct(1000)

Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    fuct(1000)
  File "<pyshell#252>", line 2, in fuct
    return fuct_def(1,1,n)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
RuntimeError: maximum recursion depth exceeded
>>> def fuct_2(n):
	return fuct_def(1,1,n)

>>> fuct_2(1000)

Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    fuct_2(1000)
  File "<pyshell#257>", line 2, in fuct_2
    return fuct_def(1,1,n)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
  File "<pyshell#243>", line 4, in fuct_def
    return fuct_def(product*count,count+1,max)
RuntimeError: maximum recursion depth exceeded
>>> fuct(10)
3628800
>>> fuct(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L
>>> L = []
>>> n = 1
>>> while n<=99:
	L.append(n)
	n = n+2

	
>>> print L
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> #��Ƭȡlist�е�Ԫ��
>>> L[0:5]
[1, 3, 5, 7, 9]
>>> L[9:10]
[19]
>>> L[::]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> L[:10]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> L[:10:4:2]
SyntaxError: invalid syntax
>>> L[:10:4]
[1, 9, 17]
>>> L[:10:1]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> #ȡǰ10��Ԫ��
>>> L[:10]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> #ǰ10��Ԫ��ÿ2��ȡ
>>> L[:10:2]
[1, 5, 9, 13, 17]
>>> #ȡ��20�������һ��
>>> L[10:]
[21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> #���10��Ԫ��
>>> L[-10:]
[81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> #ȡ��9������20��
>>> L[9:20]
[19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
>>> #����
>>> #���list���±��value
>>> my_list = ['a','b','c']
>>> for x,y in my_list:
	print x,y

	

Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    for x,y in my_list:
ValueError: need more than 1 value to unpack
>>> for x,y in enumerate(my_list):
	print x,y

	
0 a
1 b
2 c
>>> my_dist = {'key1':'value1','key2':'value2'}
>>> for key,value in my_dist
SyntaxError: invalid syntax
>>> for key,value in my_dist:
	print key,value

	

Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    for key,value in my_dist:
ValueError: too many values to unpack
>>> for key in my_dist:
	print key

	
key2
key1
>>> for key,value in my_dist.iteritems:
	print key,value

	

Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    for key,value in my_dist.iteritems:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for key,value in my_dist.iteritems:
	print key,value

	

Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    for key,value in my_dist.iteritems:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for k,v in my_dist.iteritems:
	print k,v

	

Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    for k,v in my_dist.iteritems:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for k,v in my_dist.items:
	print k,v

	

Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    for k,v in my_dist.items:
TypeError: 'builtin_function_or_method' object is not iterable
>>> #�ж��Ƿ��ܵ���
>>> isinstance('aaaaa',Iterable)

Traceback (most recent call last):
  File "<pyshell#313>", line 1, in <module>
    isinstance('aaaaa',Iterable)
NameError: name 'Iterable' is not defined
>>> isinstance('aaaaa',Iterable)

Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    isinstance('aaaaa',Iterable)
NameError: name 'Iterable' is not defined
>>> from collections import Iterable
>>> isinstance('aaa',Interable)

Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    isinstance('aaa',Interable)
NameError: name 'Interable' is not defined
>>> isinstance('aaa',Iterable)
True
>>> #����list�а���fuple
>>> my_list = [(1,2),(2,3),(3,4)]
>>> for x,y in my_list:
	print x,y

	
1 2
2 3
3 4
>>> #����tuple�а���list
>>> my_tuple = ([2,3],[5,6],[8,9])
>>> for x,y in my_tuple:
	print x,y

	
2 3
5 6
8 9
>>> #�б�����ʽ
>>> my_createList = [x*x for x in range(1,11)]
>>> my_createList
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> range(1,33)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
>>> my_createList = range(0,3)
>>> my_createList
[0, 1, 2]
>>> my_createList = [m+n,for m in 'abc' for n in 'xyz']
SyntaxError: invalid syntax
>>> my_createList = [m+n for m in 'abc' for n in 'xyz']
>>> my_createList
['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']
>>> import os
>>> [d for d in os.listdir('.')]
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'pythonw.exe', 'README.txt', 'tcl', 'Tools', 'w9xpopen.exe']
>>> #�г���ǰĿ¼�µ������ļ���Ŀ¼
>>> [d for d in os.listdir('.')]
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'pythonw.exe', 'README.txt', 'tcl', 'Tools', 'w9xpopen.exe']
>>> d = {'x':'A','y':'B','z':'C'}
>>> for k,v in d.iteritems():
	print k,'=',v

	
y = B
x = A
z = C
>>> #��list�������ַ������Сд
>>> L = ['HELLO','WORLD','IBM','APPLE']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
>>> #�ж��Ƿ���һ���ַ���
>>> x = '123465'
>>> y = 'abcd'
>>> isinstace(x,str)

Traceback (most recent call last):
  File "<pyshell#351>", line 1, in <module>
    isinstace(x,str)
NameError: name 'isinstace' is not defined
>>> isinstance(x,str)
True
>>> isinstance(y,str)
True
>>> z = 789456;
>>> isinstance(z,str)
False
>>> g = (x*x for x in range(10))
>>> g
<generator object <genexpr> at 0x02C77D00>
>>> g.next()
0
>>> g.next()
1
>>> #����Generator ������
>>> g = (x for x in range(10))
>>> g
<generator object <genexpr> at 0x02C771C0>
>>> g.next()
0
>>> g.next()
1
>>> for n in g:
	print n

	
2
3
4
5
6
7
8
9
>>> g.close()
>>> 
>>> for n in g:
	print n

	
>>> g.gi_running()

Traceback (most recent call last):
  File "<pyshell#373>", line 1, in <module>
    g.gi_running()
TypeError: 'int' object is not callable
>>> g = (x*x for x in range(14))
>>> g
<generator object <genexpr> at 0x02C77BC0>
>>> for item in g:
	print item

	
0
1
4
9
16
25
36
49
64
81
100
121
144
169
>>> #yield ���� �� Generator ����
>>> def odd():
	print 'step1'
	yield 1
	print 'step2'
	yield 2
	print 'step3'
	yield 5

	
>>> o = odd()
>>> o.next()
step1
1
>>> o.next()
step2
2
>>> odd()
<generator object odd at 0x02C77918>
>>> #����yield�����˺���Ϊһ��Generator
>>> odd()
<generator object odd at 0x02C763C8>
>>> for n in odd()
SyntaxError: invalid syntax
>>> o = odd()
>>> for n in odd():
	print n

	
step1
1
step2
2
step3
5
>>> #�߽׺���
>>> def f(x):
	x*x

>>> map(f,range(10))
[None, None, None, None, None, None, None, None, None, None]
>>> map(f,[1,2,3,4,5,6])
[None, None, None, None, None, None]
>>> def f(x):
	return x*x

>>> map(f,range(9))
[0, 1, 4, 9, 16, 25, 36, 49, 64]
>>> map(f,range(1,10))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> #��������Ϊ������map ������
>>> #reduce �÷�
>>> def add(x,y):
	return x+y

>>> reduce(add,range(10))
45
>>> def fn(x,y):
	return x*10+y

>>> reduce(fn,[1,3,5])
135
>>> reduce(fn,range(10))
123456789
>>> def str2int(s):
	return reduce(lambda x,y:x*10+y,map(int,s))

>>> str2int('789456')
789456
>>> str2int('aaa')

Traceback (most recent call last):
  File "<pyshell#427>", line 1, in <module>
    str2int('aaa')
  File "<pyshell#425>", line 2, in str2int
    return reduce(lambda x,y:x*10+y,map(int,s))
ValueError: invalid literal for int() with base 10: 'a'
>>> str2int(ord('A'))

Traceback (most recent call last):
  File "<pyshell#428>", line 1, in <module>
    str2int(ord('A'))
  File "<pyshell#425>", line 2, in str2int
    return reduce(lambda x,y:x*10+y,map(int,s))
TypeError: argument 2 to map() must support iteration
>>> str2int('156456')
156456
>>> 
