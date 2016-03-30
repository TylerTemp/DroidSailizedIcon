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

**Use it directly on Jolla Terminal:**

1.  Open Jolla Terminal and enter the superuser mode:

   ```bash
   devel-su
   Password: # enter your developer mode password
   ```

2.  run this command:

    ```bash
    python -c "$(curl -fsSL https://raw.githubusercontent.com/TylerTemp/DroidSailizedIcon/master/cp.py)"
    ```


It will backup the original icons and change it into the new icons

If you want to undo the change, do(in developer mode)

```bash
python -c "$(curl -fsSL https://raw.githubusercontent.com/TylerTemp/DroidSailizedIcon/master/cp.py)" restore
```

If you don't want to back original icons up, do(in developer mode)

```bash
python -c "$(curl -fsSL https://raw.githubusercontent.com/TylerTemp/DroidSailizedIcon/master/cp.py)" copy
```

Development
----------

If you're interested in this project, please put your icon into `apkd` folder

For those png files made by yourself, please name it in `mit_files.txt`

If you want an icon which is not contained in this project, and you don't know how to Photoshop, please email that icon file to me at  [tylertempdev@gmail.com](mailto:tylertempdev@gmail.com)

License
---------

Any png files listed in `mit_files.txt` is under [MIT-LINCENSE](https://github.com/angular/angular.js/blob/master/LICENSE).

Any other png files should never used for a business purpose.
