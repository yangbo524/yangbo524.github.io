### 用jenkins搭建android自动打包环境

另文档链接地址：http://www.android100.org/html/201506/22/156680.html

下载地址：http://mirrors.jenkins-ci.org/war/latest/jenkins.war。将下载的jenkins.war包直接放到tomcat下的webapps目录，启动tomcat即可安装完成。\
编码问题：进入jenkins系统管理页面，会出现如图提示，可修改tomcat的server.xml配置，在Connector  标签添加上 URIEncoding="UTF-8" 。

![Alt text](/jenkins+Gradle自动打包/jenkins1.jpg)

 安全配置：如图

![Alt text](/jenkins+Gradle自动打包/jenkins2.jpg)

首先的先添加一个administer用户作为超级管理员，全部权限都打勾，如图boluo用户。保存，重启。用刚刚添加的超级管理员作为帐号名注册一个帐号，即可拥有超级管理员权限。
JDK、gradle如果系统环境变量设置的话就不用再设置，用默认的就行。
邮件通知：系统管理>系统设置  如图

![Alt text](/jenkins+Gradle自动打包/jenkins3.jpg)

#### Jenkins gradle插件安装

系统管理>管理插件>可选插件 选中Jenkins Gradle plugin插件安装重启即可。
安装慢的话，可以把插件下载下来，手动上传插件或设置代理。如图

![Alt text](/jenkins+Gradle自动打包/jenkins4.jpg)

#### Jenkins新建任务

点击新Job，输入任务名称选中构建一个自由风格的软件项目，点击OK，跳到配置页面
源码管理:如图。

![Alt text](/jenkins+Gradle自动打包/jenkins5.jpg)

epository URL： svn 的 的地址，如果输入的地址需要输入用户名和密码，将自动跳出红色的提示信息,点击"enter credential" 进入设置svn 用户名。

构建触发器：如图

![Alt text](/jenkins+Gradle自动打包/jenkins6.jpg)

uild periodically：周期进行项目构建（它不关心源码是否发生变化）

    Poll SCM：定时检查源码变更（根据SCM软件的版本号），如果有更新就checkout最新code下来，然后执行构建动作。

    这里我选Poll SCM，（H/5 H(9-23) * * *）

    第一个参数代表的是分钟 minute，取值 0~59；
    第二个参数代表的是小时 hour，取值 0~23；
    第三个参数代表的是天 day，取值 1~31；
    第四个参数代表的是月 month，取值 1~12；
    最后一个参数代表的是星期 week，取值 0~7，0 和 7 都是表示星期天。
    如H/5 * * * * 表示的就是每5分钟检查一次源码变化。

    构建：添加Invoke Gradle script，配置如图

![Alt text](/jenkins+Gradle自动打包/jenkins7.jpg)

Switches ：即gradle 后面所接的命令。上面相当于执行gradle clean build命令。

构建后操作：构建失败可以发送邮件通知，如图

![Alt text](/jenkins+Gradle自动打包/jenkins8.jpg)
