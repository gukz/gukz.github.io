# 第1章
使用 `*` 和 `_` 来获取任意数量的变量，忽略特定数量的变量。
获取一个集合中获得最大或者最小的N个元素
- N=1时，使用min或者max会更快
- N接近集合大小时，使用排序配合切片会更快 `sorted(items)[:N]`
- `heapq` 最大堆nlargest  最小堆nsmallest
- `heapify` 返回堆, 使用 `heappop`推出堆顶元素
使用 `from collections import defaultdict` 来导入数据
有序字典`OrderDict`来创建有序字典 `from collections import OrderDict`
当代码中需要大量使用切片时，可以采用切片定义提高代码可读性
```python
SHARDS = slice(20, 40)
val = int(record[SHARDS])
```
找出一个序列中出现次数最多的元素
使用 `collections.Counter` 来找出频次最高的n个元素。
```python
words = []
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
```
根据某个或某几个字段字段来排序这个列表。
```python
from operator import itemgetter
rows_by_name = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('fname', 'uid'))
```
类似的还有`attrgetter` 用于获取对象的属性。
`(x * x for x in nums)` 表示一个生成器对象，而`[x * x for x in nums]` 则表示一个列表。
```python
from collections import ChainMap
a = {1: 1}
b = {2: 2}
c = ChainMap(a, b)
```
# 第2章
# 第3章
# 第4章
# 第5章
# 第6章
# 第7章
# 第8章
# 第9章
# 第10章
# 第11章
# 第12章
# 第13章
# 第14章
# 第15章
