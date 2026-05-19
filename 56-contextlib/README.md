# 第 56 关：contextlib（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解上下文管理器的原理
- 用 `@contextmanager` 简化上下文管理器
- 用 `closing()` 包装只有 close() 的对象
- 实现实用的上下文管理器

## 🤔 先想一个问题

写 `with open() as f:` 时，文件会自动关闭。但如果你有自己的资源（数据库连接、网络连接、计时器）也想用 `with` 自动管理，得写 `__enter__` 和 `__exit__` 两个方法，太麻烦了。`@contextmanager` 让你用一个函数就搞定。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# contextlib

from contextlib import contextmanager, closing

# 回顾：with 语句需要上下文管理器（__enter__ + __exit__）
class MyResource:
    def __enter__(self):
        print("打开资源")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭资源")
        return False    # 不吞掉异常

with MyResource() as r:
    print("使用资源")

# 用 @contextmanager 简化！
@contextmanager
def my_resource():
    print("打开资源")
    try:
        yield "资源对象"    # yield 之前是 __enter__
    finally:
        print("关闭资源")    # yield 之后是 __exit__

with my_resource() as r:
    print(f"使用: {r}")

# 实用例子：计时器
import time

@contextmanager
def timer(name):
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"{name} 耗时: {elapsed:.3f}s")

with timer("计算"):
    total = sum(range(1000000))
    print(f"结果: {total}")

# 实用例子：临时修改工作目录
import os

@contextmanager
def change_dir(path):
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

# closing()：为没有 __exit__ 的对象加上 close() 调用
class Connection:
    def __init__(self):
        print("连接已建立")

    def close(self):
        print("连接已关闭")

with closing(Connection()) as conn:
    print("使用连接")
# 自动调用 conn.close()
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `@contextmanager` 装饰器把生成器函数变成上下文管理器
- `yield` 之前是 `__enter__`，`yield` 之后是 `__exit__`
- `yield` 的值就是 `with ... as x:` 中的 `x`
- `closing(obj)` 会在 `with` 结束时自动调用 `obj.close()`
- 上下文管理器适合管理任何「打开-使用-关闭」模式的资源

## 🏃 跑一下试试

```bash
cd 56-contextlib
python contextlib_demo.py
```

## 💡 师兄的碎碎念

- `@contextmanager` 装饰器把生成器函数变成上下文管理器
- `yield` 之前是 `__enter__`，`yield` 之后是 `__exit__`
- `yield` 的值就是 `with ... as x:` 中的 `x`
- `closing(obj)` 会在 `with` 结束时自动调用 `obj.close()`
- 上下文管理器适合管理任何「打开-使用-关闭」模式的资源

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `@contextmanager` | 用生成器函数创建上下文管理器 |
| `yield` | 分隔 enter 和 exit 逻辑 |
| `closing(obj)` | 自动调用 close() 的包装器 |
| `__enter__ / __exit__` | 上下文管理器协议 |

## ➡️ 下一关

下一关我们学习 [requests](../57-requests/README.md)，继续加油！
