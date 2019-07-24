redis应用场景：
对于速度要求严格，数据频繁被修改的场景下。

redis的api中的数据结构主要有以下几种：
1.string
2.list
3.hash
4.set
5.sorted set
这些api提供的数据结构的内部底层实现为：
1.sds
2.quicklist
3.dict
4.skiplist
5.intset
6.ziplist
7.object
在学习了解 redis的几个底层数据结构的过程中，处处可以体会到作者在设计redis时对于性能和空间的思考。
## sds
simple dynamic string （简单动态字符串）
典型数据结构如下：其中16表示len和alloc的数据结构大小，还有8，32，64等
```
struct __attribute__ ((__packed__)) sdshdr16 {
    uint16_t len;  /* used */
    uint16_t alloc;  /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
}
```
不同于c语言的字符串表示方式（以'\0'结尾），redis自己构建了一种名为简单动态 字符串的抽象类型，并
将sds用作redis的默认字符串表示。
c语言的字符串本身不记录字符串长度，为了获取一个字符串的长度消息需要耗费O(N)的时间复杂度。
sds中有len字段记录字符串的长度，此外alloc属性记录了总分配空间。获取字符串的长度不会成为redis的瓶颈。
sds有自己独特的header（5种），之所以有5种，是为了能让不同长度的字符串使用不同大小的header。

很多语言的字符串会分为mutable和immutable两种类型，sds属于mutable类型，sds表示的字符串可以修改 也可以追加，
当sds API需要对sds进行修改时，API会先检查sds的空间是否满足修改所需的要求。如果不满足，API将会自动将sds的 
空间扩展至足以执行修改所需的大小，然后才执行实际的修改操作，所以使用 sds即不需要手动修改sds的空间大小，
也不会出现c语言中可能面临的缓冲区溢出的问题。
### 结尾添加'\0', 遵循c惯例
alloc用于计算未使用空间，解除字符串长度与底层数组长度之间的关联。buf的长度不一定是就是字符串的长度，buf内
可能包含未使用的字节。
通过alloc，sds实现了空间预分配和惰性释放(sds提供了相应的API，以便真正释放sds里的未使用空间)。
### 空间预分配：
每次sds的alloc默认为len+len，当len超过1MB时，alloc为len+1MB。 
buf数组的实际长度为alloc + 1byte（额外的一个字节用于保存空字符串）额外保存一个空字符串的好处是sds可以直接重用
一部分C字符串函数库里面的函数。
### 二进制安全
c字符串中的字符必须符合某种编码 ，并且不能包含'\0'，因此c字符串只能保存文本，不能保存图片、视频等二进制数据。
sds使用字节数组保存数据，默认数据为二进制。
### 总结
redis只会使用c字符串作为字面量，大多数情况下，redis使用sds作为字符串表示。
比起c字符串，sds具有如下优点：

- 1.O(1)获取字符串长度
- 2.杜绝缓冲区溢出
- 3.减少修改字符串长度时，内存重分配次数。
- 4.二进制安全。
- 5.兼容部分c字符串函数。

## ziplist
压缩链表
ziplist是一个经过特殊编码的双向链表，设计的目的是为了提高存储效率。可用于存储字符串和整数。
整数是以二进制的形式保存，而不是字符串。
支持O(1)时间复杂度的在表两端提高push和pop操作。
但是ziplist的每次变更操作都需要一次内存重分配，因此实际复杂度与ziplist实际使用的内存量有关。
ziplist不同于普通的双向链表，链表中每一项都占用独立的一块内存，各项之间用地址指针链接，这样
会带来大量的内存碎片，而且地址指针也会占用额外内存。而ziplist却是将表中 每一项存放在前一项后续的地址空间
一个ziplist整体占用一大块内存，它是一个表（list），不是链表（linked list）
