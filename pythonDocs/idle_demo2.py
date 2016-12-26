#IO流读写
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open('E:/Gome文件/myGithub/yangbo524.github.io/pythonDocs/111.txt', 'r') as f:
    print f.read()   
    for line in f.readlines():
        print(line.strip())
with open('E:/Gome文件/myGithub/yangbo524.github.io/pythonDocs/111.txt', 'rb') as ff:
    u = ff.read().decode('GBK')
    print u
    
#读文件时自动转换编码
import codecs
with codecs.open('E:/Gome文件/myGithub/yangbo524.github.io/pythonDocs/111.txt', 'rb','GBK') as m:
    print m.read()
    
    
#写文件
with open('E:/Gome文件/myGithub/yangbo524.github.io/pythonDocs/111.txt','w') as wf:
    print wf.write('我擦')
   
#序列化
try:
    import cPickle as pickle
except ImportError:
    import pickle
d = dict(name='Bob',age = 20,score = 88)
f = open('E:/Gome文件/myGithub/yangbo524.github.io/pythonDocs/111.txt','wb')
pickle.dump(d,f)
f.close()
print d
#将pickle转换为json
import json
print json.dumps(d)


