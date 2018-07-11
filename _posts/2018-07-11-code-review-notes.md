here is some tips found in code review
### python 单行读取文件写法
 难道不能写中文吗需求是读取文件时，一行一行的处理文件内容而不是一次性把文件都读取出来
```
f = open(filename)
for line in f:  # python2.2 之后，可以直接对一个file对象使用for实现一行一行读取
    # do something
f.close()
```
### 原则
+ ```try```内部代码近

### docker file 中每一行的编写都要考虑这一层能不能缓存
