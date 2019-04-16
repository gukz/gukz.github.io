## celery是什么
Celery被用来稍后执行某些代码，或用做调度器调度这些代码。

## 异步任务`celery`是什么，能做什么
- 1.异步执行任务
- 2.周期执行任务
- 3.延时执行任务
- 4.跨项目执行任务
- 5.检查任务执行结果

## 怎么实现的,路由规则
AMQP(AdvancedMessage Queuing Protocol) 高级消息队列协议，是应用层协议的一个开放标准，为面向消息的中间件设计。
[模型参考手册](http://rabbitmq.mr-ping.com/AMQP/AMQP_0-9-1_Model_Explained.html)
RabbitMQ是一个开营的AMQP实现。
```
Publisher---Exchange----Queue---------channel-----Consumer
            --Broker---------
            --Virtual Host---
                                  --connection--
```
Broker: 接受和分发消息的应用
Virtual host: 出于多租户和安全因素的设计，把AMQP的基本组件划分到一个虚拟的分组中，当多个不同的用户使用同一个AMQP提供服务时，
可以划分出多个vhost，每个用户在自己的vhost创建 exchange/queue等。
Channel：轻量级的connection，多个Channel之间完全隔离，可减少TCP Connection的开销。
Exchange：message 到达broker的第一站，根据分发规则，匹配查询表中的routing key，分发消息到queue去。
常用类型有：direct(point-to-point), topic(publish-subscribe), fanout(multicast)
Queue：消息最终被送到这里等待consumer取走，一个message可以被同时拷贝到多个queue中。
Binding：exchange和queue之间的虚拟链接，binding中可以包含routing key。binding信息被保存到exchange中的查询表中，用于message的分发依据。

###### direct
message中的routing key如果和binding中的routing key一致，就会将该message发到对应的queue中。
###### fanout
类型为fanout的exchange会把message转发到绑定的所有的queue上去。
###### topic
类型为topic的exchange会根据routing key以及通配符规则，将message分发到目标queue中。
routing key包含两种通配符 “#”通配任何零个或多个word “*”通配任何单个word

## 可能引发的问题
- 竞争问题
> 如果你的任务A里想要调度任务B，在任务B结束之后，做一些其他的工作，最好创建一个任务C做这些工作，在任务B结束时调度任务C。
- 大量任务，拥堵queue
> 如果你瞬间产生的大量的任务，这些任务对堆积在队列中，业务产生的任务就不能及时得到执行。
