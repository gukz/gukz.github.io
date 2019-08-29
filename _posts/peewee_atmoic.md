记录一次数据迁移时，必须要用atmoic包裹。
添加atmoic后，迁移不再出问题，理论上不需要添加atmoic。
添加atmoic，peewee做了什么事？

正常执行insert_many时，发生了什么？
peewee默认时候是autocommit
```python
class _atomic(_callable_context_manager):
    def __init__(self, db, lock_type=None):
        self.db = db
        self._lock_type = lock_type
        self._transaction_args = (lock_type,) if lock_type is not None else ()

    def __enter__(self):
        if self.db.transaction_depth() == 0:
            self._helper = self.db.transaction(*self._transaction_args)
        elif isinstance(self.db.top_transaction(), _manual):
            raise ValueError('Cannot enter atomic commit block while in '
                             'manual commit mode.')
        else:
            self._helper = self.db.savepoint()
        return self._helper.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._helper.__exit__(exc_type, exc_val, exc_tb)
```

1, init 函数
db -数据库对象
lock_type -事物锁定模式

2，enter
首先transaction_depth的作用是：

