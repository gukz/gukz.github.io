# tea talk2
## mysql 卡死时最快恢复服务需要做的事情：
1, 找出慢查询的语句并优化掉。
2, 把服务停掉、数据库连接kill掉，部署新服务。
#### 优化数据库慢查询
一个业务操作一张数据量为5w的表，从其中选出1w数据，再对其按照updated_at 排序。
如果对updated_at增加索引进行查询就会缓解这个慢查询。(order by 是Using filesort所以是慢查询，相当于对1w的数据排序)
一条sql只会使用一条索引所以当sql为where(A).order_by(B)时，只会用到一个索引(A)。但是如果有联合索引(A,B)，这种情况下还是会走索引的。

## requests 的一些默认行为：
1, 当response里没有charset时，requests会尝试用常用编码解码内容。如果用gb2312解码utf-8，你会得到乱码。
2, 微信的response为204，但是带有错误信息

## elasticsearch有可能导致数据丢失：
1, elasticsearch数据录入时，先进入内存，然后大约1s(可配置)后会落盘，如果在第999ms时这个节点崩溃，过去999ms的数据就会丢失。
但是，es的index可以保证是实时的，因为Get请求会直接读取内存中尚未Flush到磁盘的TransLog。
[详细资料](https://zhuanlan.zhihu.com/p/34669354)
