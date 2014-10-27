DroidSailizedIcon
=================


介绍
---------

(英文版请阅读 `README.md`)

厌倦了你Jolla上的不搭调的安卓图标么?

DroidSailzedIcon为你提供了一套SailfishOS风格的安卓图标.

目前只提供了部分app图标. 如果你对这个项目有兴趣, 请帮我做的更好.

使用方法
----------

1. 下载这个项目并解压. 你会得到一个`apkd`文件夹(包含了替代的文件)和`original`
文件夹(包含了原本的图标)

2. 将整个`apkd`文件夹拷贝到你的Jolla手机.(你可以先去除一些你不需要的图标)

3. 使用文件浏览器(`File Browser`, `Cargo Dock`, `Jolla-Fileman`等等.)将`apkd`下
的所有文件拷贝到`/var/lib/apkd`. 或者直接在`Terminal`中执行:

```bash
yes | cp /path/to/DroidSailizedIcon/apkd/* /var/lib/apkd
```

开发
----------

如果你对这个项目有兴趣, 请一起来提交你修改的图标. 请将原图标放在`original`
文件夹下, 替换的图标放在`apkd`文件夹下. 如果你需要提交一个已经存在的图标,
请放在`extra`文件夹下

原创图标请将其名字写在`mit_files.txt`中

你可以直接将你需要的图标邮件给我, 我会帮你制作并提交. 我的邮箱:
[huangling.exe@gmail.com](huangling.exe@gmail.com) .

使用协议
---------

所有`mit_files.txt`中提到的文件使用[MIT-LINCENSE](https://github.com/angular/angular.js/blob/master/LICENSE).

所有其它png文件不得用于商业用途.


日志
------------

添加淘宝图标