# here is some tips found in code review
- python 单行读取文件写法
需求是读取文件时，一行一行的处理文件内容而不是一次性把文件都读取出来。
```python
f = open(filename)
for line in f:  # python2.2 之后，可以直接对一个file对象使用for实现一行一行读取
    # do something
f.close()
```
- 原则`try`内部代码尽可能的少
- `Dockerfile`中每一行的编写都要考虑这一层能不能缓存
- 变量、函数命名依据含义，不可含义不清
- 如果没有 _十分充足_的理由，不要使用`post-save`
- 数据库加字段如果在`shell`里进行可能会导致锁表，原因未知
- 定时动作精确到秒可以通过`celery`的`count-down`来实现
- 多个异步任务如果都会save同一个对象可能引发竞争的bug
