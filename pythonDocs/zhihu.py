#֪��ͷ��
import requests
import urllib
import re
import random
from time import sleep
def main():
    url='https://www.zhihu.com'
    #�о��������������Ů��
    headers={'ʡ��'}
    i=1
    for x in xrange(20,3600,20):
        data={'start':'0','offset':str(x),'_xsrf':'a128464ef225a69348cef94c38f4e428'}
        #֪����offset���Ƽ��صĸ�����ÿ����Ӧ����20
        content=requests.post(url,headers=headers,data=data,timeout=10).text
        #��post�ύform data
        imgs=re.findall('<img src=\\\\\"(.*?)_m.jpg',content) 
        #����������json����������ȡͼƬ��ַ��ȥ��_mΪ��ͼ 
        for img in imgs:
            try:
                img=img.replace('\\','')
                #ȥ��\�ַ�������ųɷ�
                pic=img+'.jpg'
                path='d:\\bs4\\zhihu\\jpg\\'+str(i)+'.jpg'
                #�����洢��ַ��ͼƬ����
                urllib.urlretrieve(pic,path)
                #����ͼƬ
                print u'�����˵�'+str(i)+u'��ͼƬ'
                i+=1
                sleep(random.uniform(0.5,1))
                #˯�ߺ������ڷ�ֹ��ȡ���챻��IP
            except:
                print u'ץ©1��'
        pass
        sleep(random.uniform(0.5,1))


if __name__=='__main__':
    main()


