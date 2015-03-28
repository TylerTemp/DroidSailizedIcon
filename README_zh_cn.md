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

1. 克隆项目到手机:

   ```bash
   git clone https://github.com/TylerTemp/DroidSailizedIcon.git .droid
   ```

2. 执行脚本

   ```bash
   cd .droid
   devel-su
   Password: # enter your developer mode password
   python copy.py
   ```

它将自动备份源图标并更新为新图标

如果你想撤消, 请在开发者模式下执行:

```bash
python copy.py  restore
```

如果你不想备份原图标, 请在开发者模式下执行:

```bash
python copy.py copy
```

如果你不信任这个脚本想自己动手, 可以执行:

```bash
yes | cp /path/to/DroidSailizedIcon/apkd/* /var/lib/apkd
```

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
