## TODO list
- 本地搭建kingshard
- 将无状态迁移数据的思想实现成一个轮子
- 使用css美化列表页
- 动态渲染网页

## 20190522
- css 实现列表页

神策分享
1.打点工作流
产品(运营)确定分析什么->设计事件->
2.公共属性


## 20190829
mysql server autocommit=0时，什么时候进行commit？
一个insert语句执行结束后如果没有冲突，会进行commit。
什么样的冲突会导致不commit

事情经过：
1，第一次迁移数据，报错，因为没有按照user_id分node。
2，第二次分了node之后，迁移数据仍然报错（688个）同时数据磁盘满了。
3，把每个insert_many放在db.atomic()内，强制提交。迁移没有报错。
考虑的点：
   insert_many直接执行和放在db.atomic内执行有什么区别


及时同步
