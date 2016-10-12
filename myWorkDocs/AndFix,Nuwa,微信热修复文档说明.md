## AndFix、Nuwa、微信热补丁修复原理及区别

### AndFix
##### 技术原理

Andfix的修复是方法级的，对有bug的方法进行替换。

![Alt text](/myWorkDocs/HotFix/hotfix1.png)

使用AndFix修复热修复的整体流程：

![Alt text](/myWorkDocs/HotFix/hotfix5.png)

##### 方法替换过程：

![Alt text](/myWorkDocs/HotFix/hotfix6.png)


##### 优缺点
AndFix 采用native hook的方式，这套方案直接使用 dalvik_replaceMethod 替换class中方法的实现。由于它并没有整体替换class, 而field在class中的相对地址在class加载时已确定，所以AndFix无法支持新增或者删除filed的情况(通过替换 init 与 clinit 只可以修改field的数值)。

是动态的，所以不需要重启应用就可以生效<br>
支持ART与Dalvik<br>
支持新增加方法<br>
支持在新增方法中新增局部变量<br>

不支持新加全局变量：

![Alt text](/myWorkDocs/Andfix_nuwa_weixin/result1.PNG)
修改方法里面的bug，不能大规模做更改
### Nuwa
##### 技术原理
其实就是用ClassLoader加载机制，覆盖掉有问题的方法。所以我们的补丁其实就是有问题的类打成的一个包。
将修复的包打包成dex.jar文件

就是把多个dex文件塞入到app的classloader之中一个ClassLoader可以包含多个dex文件，每个dex文件是一个Element，多个dex文件排列成一个有序的数组dexElements，当找类的时候，会按顺序遍历dex文件，然后从当前遍历的dex文件中找类，如果找类则返回，如果找不到从下一个dex文件继续查找。

理论上，如果在不同的dex中有相同的类存在，那么会优先选择排在前面的dex文件的类，如下图：

![Alt text](/myWorkDocs/Andfix_nuwa_weixin/classloaddex1.jpg)

在此基础上，把有问题的类打包到一个dex（patch.dex）中去，然后把这个dex插入到Elements的最前面，如下图：

![Alt text](/myWorkDocs/Andfix_nuwa_weixin/classloaderdex2.jpg)

当一个apk在安装的时候，apk中的classes.dex会被虚拟机(dexopt)优化成odex文件，然后才会拿去执行。
虚拟机在启动的时候，会有许多的启动参数，其中一项就是verify选项，当verify选项被打开的时候，上面doVerify变量为true，那么就会执行dvmVerifyClass进行类的校验，如果dvmVerifyClass校验类成功，那么这个类会被打上CLASS_ISPREVERIFIED的标志

空间使用的是在字节码插入代码,而不是源代码插入，使用的是javaassist库来进行字节码插入的。
作者：MagiLu
链接：https://zhuanlan.zhihu.com/p/20308548
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

所以为了实现补丁方案，所以必须从这些方法中入手，防止类被打上CLASS_ISPREVERIFIED标志。

最终空间的方案是往所有类的构造函数里面插入了一段代码，代码如下：
~~~ java
if (ClassVerifier.PREVENT_VERIFY) {

System.out.println(AntilazyLoad.class);

}
~~~
其中AntilazyLoad类会被打包成单独的hack.dex，这样当安装apk的时候，classes.dex内的类都会引用一个在不相同dex中的AntilazyLoad类，这样就防止了类被打上CLASS_ISPREVERIFIED的标志了，只要没被打上这个标志的类都可以进行打补丁操作。

然后在应用启动的时候加载进来.AntilazyLoad类所在的dex包必须被先加载进来,不然AntilazyLoad类会被标记为不存在，即使后续加载了hack.dex包，那么他也是不存在的，这样屏幕就会出现茫茫多的类AntilazyLoad找不到的log。

所以Application作为应用的入口不能插入这段代码。（因为载入hack.dex的代码是在Application中onCreate中执行的，如果在Application的构造函数里面插入了这段代码，那么就是在hack.dex加载之前就使用该类，该类一次找不到，会被永远的打上找不到的标志)

其中:

![Alt text](/myWorkDocs/Andfix_nuwa_weixin/classloaderdex3.jpg)

之所以选择构造函数是因为他不增加方法数，一个类即使没有显式的构造函数，也会有一个隐式的默认构造函数。

空间使用的是在字节码插入代码,而不是源代码插入，使用的是javaassist库来进行字节码插入的。
隐患:

虚拟机在安装期间为类打上CLASS_ISPREVERIFIED标志是为了提高性能的，我们强制防止类被打上标志是否会影响性能？这里我们会做一下更加详细的性能测试．但是在大项目中拆分dex的问题已经比较严重，很多类都没有被打上这个标志。

打包

１.正式版本发布的时候，会生成一份缓存文件，里面记录了所有class文件的md5，还有一份mapping混淆文件。

２. 在后续的版本中使用-applymapping选项，应用正式版本的mapping文件，然后计算编译完成后的class文件的md5和正式版本进行比较，把不相同的class文件打包成补丁包。

备注:该方案现在也应用到我们的编译过程当中,编译不需要重新打包dex,只需要把修改过的类的class文件打包成patch dex,然后放到sdcard下,那么就会让改变的代码生效。

编译时生成插件包

##### 优缺点

非动态，重启生效<br>
支持ART与Dalvik<br>
支持新增加方法<br>
支持在新增方法中新增局部变量<br>
支持新加全局变量：<br>

### 微信Tinker 热修复
##### 技术原理
简单来说，在编译时通过新旧两个Dex生成差异patch.dex。在运行时，将差异patch.dex重新跟原始安装包的旧Dex还原为新的Dex。这个过程可能比较耗费时间与内存，所以我们是单独放在一个后台进程:patch中。为了补丁包尽量的小，微信自研了DexDiff算法，它深度利用Dex的格式来减少差异的大小。它的粒度是Dex格式的每一项，可以充分利用原本Dex的信息，而BsDiff的粒度是文件，AndFix/Qzone的粒度为class。<br>
git地址：https://github.com/zzz40500/Tinker_imitator
梳理一下过程:<br>
我们通过gradle打包app的时候记录下生成的dex，当线上版本出现问题以后.使用gradle插件打出相对应的dex，并且与之前生成的dex做差分生成patch.dex，将patch.dex push到手机上，在手机端上将patch和旧的dex合成成新的dex.，并且将这个dex放置在classloder的最前面。

在当打完patch后app进入后台以后会kill当前进程。并发起一个NoneService服。然后app会被重新启动，而activiy栈也会被保存起来。重新构建起来
