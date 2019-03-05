
# 对架构的理解
+ 项目分层的结构，数据和逻辑层+中间层
+ 基础项目是rpc项目，中间层调用基础项目，通信使用grpc
+ k8s的一些名词：pod/node/deploy/secret/job；pod/node在docker里的对应关系
+ 微服务架构，服务注册和服务发现，servicemesh结构里通信的方式，每个node上都有反向代理
+ 异步任务和消息队列
# 学习一些原理
+ 计算机网络，传输层TCP、UDP和端口，应用层的HTTP/websocket，HTTP状态码
+ 跨域
+ HTTPS和证书体系，中间人劫持
+ web安全常见的防护，XSS，CSRF
+ 操作系统，线程进程调度，锁，进程间通信
+ 并发模型，Python协程的实现原理
+ 数据库原理，king-shard, 范式，扇贝数据库设计规范（在teambition上写过）
+ redis的使用和设计规范（teambition上写过），缓存命中率，缓存穿透
+ 基本的算法知识，时间复杂度
+ 熟悉Python语法
+ elasticsearch的基本使用方法
+ 常见的哈希和加密

# 辅助信息
- 单元测试环节，仔细看代码报错信息，手动断点打印信息，用pdb调试；
- 看sentry上的报错信息；
- 看kibana上的请求日志；
- 看grafana的统计信息，CPU内存使用量。
