# Linux 系统使用的一些技巧和注意点
- 在类unix系统中，unix保护1024以下的端口，如果web服务端口号低于1024则需要超级用户权限

## 安装中文输入法 ibus-pinyin
+ 安装语言包
左下角showApplications 点击弹出应用，打开Language Support→Install/RemoveLanguages
选中chinese，点击Apply应用即可，等待下载安装完成。
+ 安装ibus框架
```shell
sudo apt-get install ibus ibus-clutter ibus-gtk ibus-gtk3 ibus-qt4
```
+ 启动ibus框架：im-config-s ibus
im-switch: command not found，找现在改成im-config了。
+ 安装拼音引擎
我用的是IBus拼音：sudoapt-get install ibus-pinyin
+ 设置ibus框架
```
sudo ibus-setup
```
在弹出到对话框中选中inputmethod，Add刚才安装的中文拼音就行了。
+ 添加输入法
Settings→Region and language→ Input Sources点击“+”，添加Chinese(pinyin)
PC右上角就会出现输入法选择
+ 输入法切换快捷键设置
Settings→Devices→ Keyboard 在右侧菜单中点击Typing下到Switchto next input source，按照提示按下快捷键，点击set完成。

## 安装vim
### 编译安装vim主要分为以下几个步骤
+ 下载[源码](ftp://ftp.vim.org/pub/vim/unix/)
+ 使用`tar -xjvf vim-8.0.tar.bz2`解压源码
+ 卸载旧的python3.5
sudo apt-get autoremove python3
使用dpkg -l|grep python 查看，发现python3前面的标志为rc，含义是已经卸载来包但是配置文件保留了
想要删除这些rc可以使用这个命令
```
dpkg -l | grep ^rc | cut -d' ' -f3 | sudo xargs dpkg --purge
```
+ 安装python3.7
```
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
xz -d Python-3.7.0.tar.xz
tar -xvf Python-3.7.0.tar
cd Python-3.7.0
./configure
make
sudo make install
```
- 发现报错 No module named '_ctypes'
- 安装  sudo apt-get libffi-def 之后重新make install可以安装python3.7
+ 卸载旧的vim

## linux cmd
### chmod 修改文件权限
`chmod +x [filename]` 
`chmod ([ugo][+-][rwx])+ filename`u-当前用户, g-当前用户所在的组, o-不与用户在同一个组的用户(不限定用户则为所有的用户). rwx-读,写,执行
递归修改子文件及文件夹的权限
### 解除端口占用
+ 查看8080端口是否开启 ` sudo netstat -anp | grep 8080`
``` 
netstat -anp | grep 8080
tcp        0      0 :::8080                     :::*                        LISTEN      3000/java   
```
+ 查看占用8080端口的进程 ` sudo fuser -v -n tcp 8080`
```
fuser -v -n tcp 8080
  USER        PID   ACCESS COMMAND   8080/tcp:       
  zhu        1154    F.... java
```
+ 杀死占用8080端口的进程
` kill -s 9 1154`

### tar
