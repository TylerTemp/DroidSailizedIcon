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


**打开Jolla控制台:**

1.  进入开发者模式:
    
    ```bash
    devel-su
    ```

    (注: 请先在设置中开启开发者模式)

2.  执行代码
    
    ```bash
    python -c "https://raw.githubusercontent.com/TylerTemp/DroidSailizedIcon/master/cp.py"
    ```

如果不想备份原有图标, 在第二步代码后加空格并加上`copy`即可(将无法撤销)

如果需要恢复图标，在第二步代码后加空格并加上`restore`即可

开发
----------

如果你对这个项目有兴趣, 请一起来提交你修改的图标到`apkd`文件夹下

原创图标请将其名字写在`mit_files.txt`中

你可以直接将你需要的图标邮件给我, 我会帮你制作并提交. 我的邮箱:
[tylertempdev@gmail.com](mailto:tylertempdev@gmail.com).

使用协议
---------

所有`mit_files.txt`中提到的文件使用[MIT-LINCENSE](https://github.com/angular/angular.js/blob/master/LICENSE).

所有其它png文件不得用于商业用途.
