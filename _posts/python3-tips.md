# python测试编写防坑指南
- `mock.patch` 在mock一些函数后，一般会通过`assert_call_with`来检查调用情况，但是如果你在mock函数后修改了mock函数的参数。那么`assert_call_with`只能标记到修改后的值，而不是调用当时的值。
```python
def func_a():
    data = {'key': 'value1'}
    func_b(data)
    data['key'] = 'value2'
```
在上面的例子中，如果我们想mock`func_b`, 我们如果编写这样的测试：
```python
with mock.patch('func_b') as m:
    func_a()
    m.assert_called_with({'key': 'value1'})  # failed
    m.assert_called_with({'key': 'value2'})  # ok
```
这种情况需要小心应对。
