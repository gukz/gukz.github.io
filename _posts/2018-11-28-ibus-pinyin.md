1、安装语言包

左下角showApplications 点击弹出应用，打开Language Support→Install/RemoveLanguages
选中chinese，点击Apply应用即可，等待下载安装完成。

2、安装ibus框架

sudo apt-get install ibus ibus-clutter ibus-gtk ibus-gtk3 ibus-qt4

3、启动ibus框架：im-config-s ibus

im-switch: command not found，找现在改成im-config了。

4、安装拼音引擎

我用的是IBus拼音：sudoapt-get install ibus-pinyin

5、设置ibus框架

sudo ibus-setup

在弹出到对话框中选中inputmethod，Add刚才安装的中文拼音就行了。

6、添加输入法

Settings→Region and language→ Input Sources点击“+”，添加Chinese(pinyin)

PC右上角就会出现输入法选择

7、输入法切换快捷键设置

Settings→Devices→ Keyboard 在右侧菜单中点击Typing下到Switchto next input source，按照提示按下快捷键，点击set完成。
