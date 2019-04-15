# fq
1. 自建shodeworks
2. 搭建VPN, 借助花生壳内网穿透
3. 买云服务器

## 公司网络通知
### 2018-11-01
更新，简化域名了，访问 grafana.shanbay.com @所有人 
访问grafana使用的代理设置方法：

#### 方法一：使用L2TP的VPN（不能翻墙）
特别注意，VPN服务器地址为47.100.76.215
账号为手机号，密码见入职邮件，IPSec PSK为shanbay
L2TP添加方式步骤可以看这个教程 http://s.com/2018vpn.pdf

#### 方法二：HTTP代理方式 (grafana走代理，其他直连）
代理服务器47.100.76.215:8123
账号就是你的VPN账号和密码
代理规则设置如下两个走代理即可
grafana.shanbay.com
prom.shanbay.com

不会配置代理的可以参考如下，HTTP代理设置步骤：
1. Chrome浏览器安装Proxy SwitchyOmega扩展 http://t.cn/EZUPv85
2. 左边 点击“导入导出”，右边在“在线恢复”中输入http://s.com/g.bak 然后点恢复
3. 左边 点击“grafana-squid代理”，右边，分别点击2个绿色的锁的图标，输入你的VPN账号密码
4. 左边 点击 “应用选项”
5. 浏览器右上角找到代理的应用图标，下拉选择“自动切换”，默认grafana页面走代理，其他直连
