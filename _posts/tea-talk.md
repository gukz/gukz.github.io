## 数据库sharding之后，失去了什么
数据库提供的能力：原子性，一致性，隔离性，持久性。

User表，4000万 sharing id 使用user_id的hash

kingshard 分发sql, 无状态
最好不影响数据库的能力, 但实际上是不可能的
问题：insert vs 自增id  mysql 单独一张表支持自增
id = BigInt(default=partial(redis.incr, key))
可靠的mysql依赖了redis单点
select vs 索引
sql不带sharing key，一个select会操作所有的表
分页请求 每个表都limit（10），分页越往后越糟糕

insert/update vs 唯一键
方案一：写入前先select检查一下  并发下回有问题
方案二：user_name作为单独一张表, 写之前先插入


失去唯一索引和事物之后
with db.transaction():
    user = User.create()
    user_social = UserSocial.create()
把transaction换成redis锁，

TiDB 天然分布式数据库
支持水平扩展
兼容mysql大部分语法
分布式事物
高可用

自增id
每个tidb-server实例自己保留一段id A 1-30000 30001-60000 id 不连续

## QUIC
基于UDP的多路复用

SCTP 不兼容 NAT

WebRTC

Candy Server


1, 分清主次，沟通能力
