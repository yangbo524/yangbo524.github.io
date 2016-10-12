#### Tinker 补丁插件

##### 1、Project的build.gradle文件引入tinker gradle-plugin 插件
~~~ java
dependencies {
       classpath 'com.android.tools.build:gradle:2.2.0'
       classpath "com.tencent.tinker:tinker-patch-gradle-plugin:1.6.2"
   }
~~~
##### 2、配置app工程的build.gradle

- 引入tinker依赖库
~~~java
compile("com.tencent.tinker:tinker-android-lib:${TINKER_VERSION}") { changing = true }
compile("com.tencent.tinker:tinker-android-anno:${TINKER_VERSION}") { changing = true }
~~~

- 设置tinkerId （由git自动产生，直接写死）
~~~ java
def gitSha() {
return "8d27a3a"
//    try {
//        String gitRev = 'git rev-parse --short HEAD'.execute().text.trim()
//        if (gitRev == null) {
//            throw new GradleException("can't get git rev, you should add git to system path or just input test value, such as 'testTinkerId'")
//        }
//        return gitRev
//    } catch (Exception e) {
//        throw new GradleException("can't get git rev, you should add git to system path or just input test value, such as 'testTinkerId'")
//    }
}
~~~
- 添加 multiDexKeepProguard 主dex拆分设置
~~~ java
/**
 * not like proguard, multiDexKeepProguard is not a list, so we can't just
 * add for you in our task. you can copy tinker keep rules at
 * build/intermediates/tinker_intermediates/tinker_multidexkeep.pro
 */
  multiDexKeepProguard file("keep_in_main_dex.txt")
~~~
- 设置buildconfig输出信息（可选）
~~~ java
/**
 * buildConfig can change during patch!
 * we can use the newly value when patch
*/
buildConfigField "String", "MESSAGE", "\"I am the base apk\""
//buildConfigField "String", "MESSAGE", "\"I am the patch apk\""
/**
 * client version would update with patch
 * so we can get the newly git version easily!
*/
buildConfigField "String", "CLIENTVERSION", "\"${gitSha()}\""
buildConfigField "String", "PLATFORM",  "\"all\""
~~~
- 声明bugApk相关属性
~~~ java
def bakPath = file("${buildDir}/bakApk/")
/**
 * you can use assembleRelease to build you base apk
 * use tinkerPatchRelease -POLD_APK=  -PAPPLY_MAPPING=  -PAPPLY_RESOURCE= to build patch
 * add apk from the build/bakApk
 */
ext {
    //for some reason, you may want to ignore tinkerBuild, such as instant run debug build?
    tinkerEnabled = true
    //you should bak the following files
    //old apk file to build patch apk    apk文件
    tinkerOldApkPath = "${bakPath}/app-debug-1010-15-41-50.apk"
    //proguard mapping file to build patch apk    混淆文件
    tinkerApplyMappingPath = "${bakPath}/"
    //resource R.txt to build patch apk, must input if there is resource changed
    tinkerApplyResourcePath = "${bakPath}/"   R 文件（处理资源补丁）
}
~~~

- 创建获取bugApk方法
~~~ java
def getOldApkPath() {
    return hasProperty("OLD_APK") ? OLD_APK : ext.tinkerOldApkPath
}
def getApplyMappingPath() {
    return hasProperty("APPLY_MAPPING") ? APPLY_MAPPING : ext.tinkerApplyMappingPath
}
def getApplyResourceMappingPath() {
    return hasProperty("APPLY_RESOURCE") ? APPLY_RESOURCE : ext.tinkerApplyResourcePath
}
def getTinkerIdValue() {
    return hasProperty("TINKER_ID") ? TINKER_ID : gitSha()
}
def buildWithTinker() {
    return hasProperty("TINKER_ENABLE") ? TINKER_ENABLE : ext.tinkerEnabled
}
~~~
- 补丁输出配置
~~~java
tinkerPatch {
        /**
         * necessary，default 'null'
         * the old apk path, use to diff with the new apk to build
         * add apk from the build/bakApk
         */
        oldApk = getOldApkPath()
        /**
         * optional，default 'false'
         * there are some cases we may get some warnings
         * if ignoreWarning is true, we would just assert the patch process
         * case 1: minSdkVersion is below 14, but you are using dexMode with raw.
         *         it must be crash when load.
         * case 2: newly added Android Component in AndroidManifest.xml,
         *         it must be crash when load.
         * case 3: loader classes in dex.loader{} are not keep in the main dex,
         *         it must be let tinker not work.
         * case 4: loader classes in dex.loader{} changes,
         *         loader classes is ues to load patch dex. it is useless to change them.
         *         it won't crash, but these changes can't effect. you may ignore it
         * case 5: resources.arsc has changed, but we don't use applyResourceMapping to build
         */
        ignoreWarning = false
        /**
         * optional，default 'true'
         * whether sign the patch file
         * if not, you must do yourself. otherwise it can't check success during the patch loading
         * we will use the sign config with your build type
         */
        useSign = true

        /**
         * Warning, applyMapping will affect the normal android build!
         */
        buildConfig {
            /**
             * optional，default 'null'
             * if we use tinkerPatch to build the patch apk, you'd better to apply the old
             * apk mapping file if minifyEnabled is enable!
             * Warning:
             * you must be careful that it will affect the normal assemble build!
             */
            applyMapping = getApplyMappingPath()
            /**
             * optional，default 'null'
             * It is nice to keep the resource id from R.txt file to reduce java changes
             */
            applyResourceMapping = getApplyResourceMappingPath()

            /**
             * necessary，default 'null'
             * because we don't want to check the base apk with md5 in the runtime(it is slow)
             * tinkerId is use to identify the unique base apk when the patch is tried to apply.
             * we can use git rev, svn rev or simply versionCode.
             * we will gen the tinkerId in your manifest automatic
             */
            tinkerId = getTinkerIdValue()
        }

        dex {
            /**
             * optional，default 'jar'
             * only can be 'raw' or 'jar'. for raw, we would keep its original format
             * for jar, we would repack dexes with zip format.
             * if you want to support below 14, you must use jar
             * or you want to save rom or check quicker, you can use raw mode also
             */
            dexMode = "jar"
            /**
             * necessary，default '[]'
             * what dexes in apk are expected to deal with tinkerPatch
             * it support * or ? pattern.
             */
            pattern = ["classes*.dex",
                       "assets/secondary-dex-?.jar"]
            /**
             * necessary，default '[]'
             * Warning, it is very very important, loader classes can't change with patch.
             * thus, they will be removed from patch dexes.
             * you must put the following class into main dex.
             * Simply, you should add your own application {@code tinker.sample.android.SampleApplication}
             * own tinkerLoader, and the classes you use in them
             *
             */
            loader = ["com.tencent.tinker.loader.*",
                      "tinker.sample.android.SampleApplication",
                      //use sample, let BaseBuildInfo unchangeable with tinker
                      "tinker.sample.android.app.BaseBuildInfo"
            ]
        }

        lib {
            /**
             * optional，default '[]'
             * what library in apk are expected to deal with tinkerPatch
             * it support * or ? pattern.
             * for library in assets, we would just recover them in the patch directory
             * you can get them in TinkerLoadResult with Tinker
             */
            pattern = ["lib/armeabi/*.so"]
        }

        res {
            /**
             * optional，default '[]'
             * what resource in apk are expected to deal with tinkerPatch
             * it support * or ? pattern.
             * you must include all your resources in apk here,
             * otherwise, they won't repack in the new apk resources.
             */
            pattern = ["res/*", "assets/*", "resources.arsc", "AndroidManifest.xml"]

            /**
             * optional，default '[]'
             * the resource file exclude patterns, ignore add, delete or modify resource change
             * it support * or ? pattern.
             * Warning, we can only use for files no relative with resources.arsc
             */
            ignoreChange = ["assets/sample_meta.txt"]

            /**
             * default 100kb
             * for modify resource, if it is larger than 'largeModSize'
             * we would like to use bsdiff algorithm to reduce patch file size
             */
            largeModSize = 100
        }

        packageConfig {
            /**
             * optional，default 'TINKER_ID, TINKER_ID_VALUE' 'NEW_TINKER_ID, NEW_TINKER_ID_VALUE'
             * package meta file gen. path is assets/package_meta.txt in patch file
             * you can use securityCheck.getPackageProperties() in your ownPackageCheck method
             * or TinkerLoadResult.getPackageConfigByName
             * we will get the TINKER_ID from the old apk manifest for you automatic,
             * other config files (such as patchMessage below)is not necessary
             */
            configField("patchMessage", "tinker is sample to use")
            /**
             * just a sample case, you can use such as sdkVersion, brand, channel...
             * you can parse it in the SamplePatchListener.
             * Then you can use patch conditional!
             */
            configField("platform", "all")

        }
        //or you can add config filed outside, or get meta value from old apk
        //project.tinkerPatch.packageConfig.configField("test1", project.tinkerPatch.packageConfig.getMetaDataFromOldApk("Test"))
        //project.tinkerPatch.packageConfig.configField("test2", "sample")

        /**
         * if you don't use zipArtifact or path, we just use 7za to try
         */
        sevenZip {
            /**
             * optional，default '7za'
             * the 7zip artifact path, it will use the right 7za with your platform
             */
            zipArtifact = "com.tencent.mm:SevenZip:1.1.10"
            /**
             * optional，default '7za'
             * you can specify the 7za path yourself, it will overwrite the zipArtifact value
             */
//        path = "/usr/local/bin/7za"
        }
    }
~~~

- 执行bakApk输出gradle任务
~~~java
/**
   * bak apk and mapping
   */
android.applicationVariants.all { variant ->
/**
 * task type, you want to bak
*/
def taskName = variant.name
tasks.all {
  if ("assemble${taskName.capitalize()}".equalsIgnoreCase(it.name)) {
      it.doLast {
      copy {
           def date = new Date().format("MMdd-HH-mm-ss")
           from "${buildDir}/outputs/apk/${project.getName()}-${taskName}.apk"
           into bakPath
           rename { String fileName ->
               fileName.replace("${project.getName()}-${taskName}.apk", "${project.getName()}-${taskName}-${date}.apk")
           }

           from "${buildDir}/outputs/mapping/${taskName}/mapping.txt"
           into bakPath
           rename { String fileName ->
               fileName.replace("mapping.txt", "${project.getName()}-${taskName}-${date}-mapping.txt")
           }

           from "${buildDir}/intermediates/symbols/${taskName}/R.txt"
           into bakPath
           rename { String fileName ->
               fileName.replace("R.txt", "${project.getName()}-${taskName}-${date}-R.txt")
           }
          }
        }
       }
      }
   }
~~~
##### 3、代码编写工作
###### 1、 自定义继承DefaultApplicationLike类 如demo SampleApplicationLike 类
 注：Application类不再引用，原来的application中的初始化工作在此类中处理
- 声明注入的application
~~~
 @DefaultLifeCycle(application = "tinker.sample.android.app.SampleApplication",flags = ShareConstants.TINKER_ENABLE_ALL,loadVerifyFlag = false)
~~~

- 初始化创建tinker
~~~java
@TargetApi(Build.VERSION_CODES.ICE_CREAM_SANDWICH)
   @Override
   public void onBaseContextAttached(Context base) {
       super.onBaseContextAttached(base);
       //you must install multiDex whatever tinker is installed!
       MultiDex.install(base); //分包声明

       SampleApplicationContext.application = getApplication(); //获取application
       SampleApplicationContext.context = getApplication();
       //设置TinkerManger的ApplicationLike
       TinkerManager.setTinkerApplicationLike(this);
       //设置异常处理
       TinkerManager.initFastCrashProtect();
       //should set before tinker is installed
       //设置是否校验
       TinkerManager.setUpgradeRetryEnable(true);
       //日志输出
       //optional set logIml, or you can use default debug log
       TinkerInstaller.setLogIml(new MyLogImp());
       //执行安装
       //installTinker after load multiDex
       //or you can put com.tencent.tinker.** to main dex
       TinkerManager.installTinker(this);
   }
~~~
###### 2、 执行安装tinker
~~~java
public static void installTinker(ApplicationLike appLike) {
        if (isInstalled) {
            TinkerLog.w(TAG, "install tinker, but has installed, ignore");
            return;
        }
        //or you can just use DefaultLoadReporter
        LoadReporter loadReporter = new SampleLoadReporter(appLike.getApplication());//result 状态码
        //or you can just use DefaultPatchReporter
        PatchReporter patchReporter = new SamplePatchReporter(appLike.getApplication());//
        //or you can just use DefaultPatchListener
        PatchListener patchListener = new SamplePatchListener(appLike.getApplication()); //回调函数
        //you can set your own upgrade patch if you need
        AbstractPatch upgradePatchProcessor = new UpgradePatch(); //主要的打补丁类
        //you can set your own repair patch if you need
        AbstractPatch repairPatchProcessor = new RepairPatch(); //主要的打补丁类

        TinkerInstaller.install(appLike,
            loadReporter, patchReporter, patchListener,
            SampleResultService.class, upgradePatchProcessor, repairPatchProcessor);

        isInstalled = true;
    }
~~~
###### 3、加载补丁
~~~java
TinkerInstaller.onReceiveUpgradePatch(getApplicationContext(), Environment.getExternalStorageDirectory().getAbsolutePath() + "/patch_signed_7zip.apk");
~~~
##### 4、加载so库
~~~java
TinkerInstaller.loadArmLibrary(getApplicationContext(), "stlport_shared");
~~~
