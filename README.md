DroidSailizedIcon
=================


Introduce
---------

(For Chinses version, please read `README_zh_cn.md`)

(中文版请阅读 `README_zh_cn.md`)

Tired of the ugly android icon on your Jolla?

DroidSailzedIcon provides the SailfishOS style icons of Android applications
for you Jolla Phone.

Only some icons are provided so far. If you're interested in this, please help
me make it better.

Usage
----------

1. Download this project and unzip. You should get a `apkd` folder (contains
    the replaced icons) and `original` folder (contains the original icons)

2. Copy the whole `apkd` folder to your Jolla Phone. (You can remove some icons
    which are not installed on your phone)

3. Use a file browser(`File Browser`, `Cargo Dock`, `Jolla-Fileman`, etc.) to
    copy all the files under `apkd` to `/var/lib/apkd`. Or simply use command
    in `Terminal`:

```bash
yes | cp /path/to/DroidSailizedIcon/apkd/* /var/lib/apkd
```

Develop
----------

If you're interested in this project, please push your icon here. The original
icons in `original` folder, the replaced icon in `apkd`. If you want to push
an icon which is already in `apkd`, please put it in `extra`

For those png files made by yourself, please list it in `mit_files.txt`

If you want an icon but do not in this project, and you don't know how to Photoshop
it, please email that icon file to me at  [huangling.exe@gmail.com](huangling.exe@gmail.com) .

License
---------

Any png files listed in `mit_files.txt` is under [MIT-LINCENSE](https://github.com/angular/angular.js/blob/master/LICENSE).

Any other png files should never used for a business purpose.

Change log
-------------

Add Taobao Icon