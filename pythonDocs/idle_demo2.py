#IO����д
#����ļ���С��read()һ���Զ�ȡ��㣻�������ȷ���ļ���С����������read(size)�Ƚϱ��գ�����������ļ�������readlines()���
with open('E:/Gome�ļ�/myGithub/yangbo524.github.io/pythonDocs/111.txt', 'r') as f:
    print f.read()   
    for line in f.readlines():
        print(line.strip())
with open('E:/Gome�ļ�/myGithub/yangbo524.github.io/pythonDocs/111.txt', 'rb') as ff:
    u = ff.read().decode('GBK')
    print u
    
#���ļ�ʱ�Զ�ת������
import codecs
with codecs.open('E:/Gome�ļ�/myGithub/yangbo524.github.io/pythonDocs/111.txt', 'rb','GBK') as m:
    print m.read()
    
    
#д�ļ�
with open('E:/Gome�ļ�/myGithub/yangbo524.github.io/pythonDocs/111.txt','w') as wf:
    print wf.write('�Ҳ�')
   
#���л�
try:
    import cPickle as pickle
except ImportError:
    import pickle
d = dict(name='Bob',age = 20,score = 88)
f = open('E:/Gome�ļ�/myGithub/yangbo524.github.io/pythonDocs/111.txt','wb')
pickle.dump(d,f)
f.close()
print d
#��pickleת��Ϊjson
import json
print json.dumps(d)


