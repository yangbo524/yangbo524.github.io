#### HotFix热修复调研
阿里有两种Dexposed和Andfix框架<br>
Dexposed由于前一种不支持5.0以上android系统，所以阿里系的方案我们就看Andfix就好。
##### Andfix
###### 引入
框架官网：https://github.com/alibaba/AndFix
介绍是用英文写的，所以附上翻译网址：
http://blog.csdn.net/qxs965266509/article/details/49802429

使用android studio开发，引入如下：

compile ‘com.alipay.euler:andfix:0.4.0@aar‘
##### 原理

下面是个修复的过程图，供我们更好地理解。

![Alt text](/HotFix/hotfix1.png)

可以看出，andfix的修复是方法级的，对有bug的方法进行替换。

###### 使用AndFix修复热修复的整体流程：
![Alt text](/HotFix/hotfix5.png)
###### 方法替换过程：
![Alt text](/HotFix/hotfix6.png)
##### 做补丁

官方有给使用方式，不过比较简略，所以会有些修改。我的思路是把补丁制作好，然后放到服务器上，客户端下载补丁到指定文件夹，然后修复。
首先要有补丁的制作工具，官方也为我们准备好了：这里
解压后，我们把修复前的apk和修复后的apk，keystore（为了方便，我就用debug的keystore了）放到这个文件夹里，如下：

![Alt text](/HotFix/hotfix2.png)

其中需要用命令做补丁文件，就是需要一个修复前的apk和修复后的apk做对比，命令含义如下：

命令 : apkpatch.bat -f new.apk -t old.apk -o output1 -k debug.keystore -p android -a androiddebugkey -e android

-f <new.apk> ：新版本
-t <old.apk> : 旧版本
-o <output> ： 输出目录
-k <keystore>： 打包所用的keystore
-p <password>： keystore的密码
-a <alias>： keystore 用户别名
-e <alias password>： keystore 用户别名密码

![Alt text](/HotFix/hotfix3.png)
技术分享
然后会在outputdic里生成一个后缀是.apatch的文件：
技术分享
改名成out.apatch，这就是我们的补丁。

![Alt text](/HotFix/hotfix4.png)

##### 打补丁
第一步：把补丁放到服务器。
简单起见，用的xampp，写了段php代码，起到下载的功能就可以了。<br>
第二步：下载和打补丁。
回到android，在我们的application里：
~~~ java
public class App extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        YuanAndfix.inject(this);
    }
}

其中，YuanAndfix类：

public class YuanAndfix {
    public static final String apatch_path = "out.apatch";
    public static void inject(final Context context) {

        final PatchManager patchManager = new PatchManager(context);
        patchManager.init(BuildConfig.VERSION_CODE + "");//current version
        patchManager.loadPatch();
        new Thread(new Runnable() {
            @Override
            public void run() {
                HttpDownload httpDownload = new HttpDownload();
                httpDownload.downFile("http://192.168.1.12/download.php", context.getDir("patch", Context.MODE_PRIVATE).getAbsolutePath()+"/",apatch_path);
                try {
                    String patchPath =context.getDir("patch", Context.MODE_PRIVATE).getAbsolutePath()+"/"+apatch_path;
                    File file = new File(patchPath);
                    if (file.exists()) {
                        patchManager.addPatch(patchPath);
                        Toast.makeText(context,"打补丁完成",Toast.LENGTH_SHORT).show();
                    } else {
                        Toast.makeText(context,"失败",Toast.LENGTH_SHORT).show();
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }).start();

    }
}
~~~

这样，热修复就完成了，我这个例子是点击按钮，弹出toast显示文字，修复前是

Toast.makeText(MainActivity.this,"bug",Toast.LENGTH_SHORT).show();

修复后是：

Toast.makeText(MainActivity.this,"fixed",Toast.LENGTH_SHORT).show();

以上就是Andfix的使用，经过我的试验，
为是动态的，所以不需要重启应用就可以生效
支持ART与Dalvik
与multidex方案相比，性能会有所提升(Multi Dex需要修改所有class的class_ispreverified标志位，导致运行时性能有所损失)
支持新增加方法
支持在新增方法中新增局部变量
使用这个框架的局限在于不能修改全局变量,不过可以在现有的方法上做修改，加局部变量。从这方面来看，Andfix其实要求我们只是修改方法里面的bug，不能大规模做更改。如果我们觉得这种修复不能满足修复要求，那么，可以看另外这种，局限更少的热修方案。
