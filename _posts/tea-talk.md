
[一些有用的git命令](https://blog.zengrong.net/post/1746.html) [一篇有用的docker博客](http://blog.csdn.net/21cnbao/article/details/56275456) [介绍docker的网站](http://dockone.io/article/111 ) [vim练习游戏](https://vim-adventures.com)


# tea talk1
## hbase
- 文档型数据库: mongodb
- 图数据库: Neo4j 数据结构比较复杂
- 推荐书籍 编程之法：算法与面试心得 七周七数据库
- 推荐网站 infoQ CAP理论：规则变了
- 支持并发的数据库

## csrf 攻击原理与防护
跨站请求伪造攻击

## es 选型：APM, JAEGER
- 可以给出一个请求的时间线，
- 脱敏，接入有性能损耗，可以设置采样率
- JAEGER 是一个对open tracing的实现

# tea talk2
## mysql 卡死时最快恢复服务需要做的事情：
1. 找出慢查询的语句并优化掉。
2. 把服务停掉、数据库连接kill掉，部署新服务。
## 优化数据库慢查询
> 一个业务操作一张数据量为5w的表，从其中选出1w数据，再对其按照updated_at 排序。

- 如果对updated_at增加索引进行查询就会缓解这个慢查询。(order by 是Using filesort所以是慢查询，相当于对1w的数据排序)
- 一条sql只会使用一条索引所以当sql为where(A).order_by(B)时，只会用到一个索引(A)。但是如果有联合索引(A,B)，这种情况下还是会走索引的。
## requests 的一些默认行为：
1. 当response里没有charset时，requests会尝试用常用编码解码内容。如果用gb2312解码utf-8，你会得到乱码。
2. 微信的response为204，但是带有错误信息
## elasticsearch有可能导致数据丢失：
1. elasticsearch数据录入时，先进入内存，然后大约1s(可配置)后会落盘，如果在第999ms时这个节点崩溃，过去999ms的数据就会丢失。
2. 但是，es的index可以保证是实时的，因为Get请求会直接读取内存中尚未Flush到磁盘的TransLog。
[详细资料](https://zhuanlan.zhihu.com/p/34669354)
## cdn有一个特性，url没有改变下载的资源就不变。

# tea talk3
## 数据库sharding之后，失去了什么
数据库提供的能力：原子性，一致性，隔离性，持久性。
User表，4000万 sharing id 使用user_id的hash
### kingshard 分发sql, 无状态
最好不影响数据库的能力, 但实际上是不可能的
问题：insert vs 自增id  mysql 单独一张表支持自增
id = BigInt(default=partial(redis.incr, key))
### 可靠的mysql依赖了redis单点
### select vs 索引
sql不带sharing key，一个select会操作所有的表
分页请求 每个表都limit（10），分页越往后越糟糕
### insert/update vs 唯一键
1. 写入前先select检查一下  并发下回有问题
2. user_name作为单独一张表, 写之前先插入

### 失去唯一索引和事物之后
```python
with db.transaction():
    user = User.create()
    user_social = UserSocial.create()
```
- 把transaction换成redis锁，
- TiDB 天然分布式数据库
- 支持水平扩展
- 兼容mysql大部分语法
- 分布式事物
- 高可用
- 自增id
- 每个tidb-server实例自己保留一段id A 1-30000 30001-60000 id 不连续

## QUIC
- 基于UDP的多路复用
- SCTP 不兼容 NAT
- WebRTC
- Candy Server

# tea talk4
## 运维分享
1. 运维指标 SLA
2. 脚本build一个vagrant镜像
## python自动格式化代码工具
- black
- mypy

# tea talk5
batch insert
两个费时操作：建索引 一致性检查

utf8 utf8mb4
utf8mb4_general_ci(排序性能更好) utf8mb4_unicode_ci(只针对德语 法语 优化) utf8mb4_bin(大小写敏感)

datetime timestamp(时区敏感 底层使用数字 只能保存一定范围的时间)

极客时间 数据库 文章
有联合索引但是没有使用，原因未知
