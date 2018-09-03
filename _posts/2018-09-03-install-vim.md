install vim
### 编译安装vim主要分为以下几个步骤
+ 下载[源码](ftp://ftp.vim.org/pub/vim/unix/)
+ 使用`tar -xjvf vim-8.0.tar.bz2`解压源码
+ 卸载旧的python3.5
    sudo apt-get autoremove python3
    使用dpkg -l|grep python 查看，发现python3前面的标志为rc，含义是已经卸载来包但是配置文件保留了
    想要删除这些rc可以使用这个命令``
    ```
    dpkg -l | grep ^rc | cut -d' ' -f3 | sudo xargs dpkg --purge
    ```
+ 安装python3.7
```shell
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
xz -d Python-3.7.0.tar.xz
tar -xvf Python-3.7.0.tar
cd Python-3.7.0
./configure
make
sudo make install
```
发现报错 No module named '_ctypes'
安装  sudo apt-get libffi-def 之后重新make install可以安装python3.7
+ 卸载旧的vim

