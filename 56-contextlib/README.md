# 第 56 关：contextlib

## 🎯 这一关你会学到

- `with` 背后的 `__enter__` / `__exit__` 协议
- 如何用 `@contextmanager` 快速写上下文管理器
- `suppress()` 如何小范围忽略指定异常
- `closing()` 如何给只有 `close()` 的对象补上上下文管理能力
- `redirect_stdout()` 如何临时捕获输出
- `ExitStack` 如何动态管理多个资源

## 🤔 先想一个问题

文件要关闭、连接要释放、锁要解开、临时输出要恢复。很多代码都有一个共同模式：

1. 进入前做准备
2. 中间执行业务
3. 不管成功失败，最后都要清理

`with` 就是为这个模式设计的。`contextlib` 则提供了一组工具，让你不用每次都手写完整类。

## 📖 看代码

```python
# contextlib 上下文管理工具

from contextlib import ExitStack, closing, contextmanager, redirect_stdout, suppress
from io import StringIO


print("=== 手写上下文管理器 ===")


class Resource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # __enter__ 的返回值会绑定给 as 后面的变量。
        print(f"打开 {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # __exit__ 无论 with 内部是否异常都会执行。
        print(f"关闭 {self.name}")
        return False


with Resource("文件") as resource:
    print(f"使用 {resource.name}")  # 使用 文件


print("\n=== @contextmanager 简化写法 ===")


@contextmanager
def managed_resource(name):
    print(f"打开 {name}")
    try:
        # yield 之前相当于 __enter__，yield 的值会交给 as 变量。
        yield name
    finally:
        # finally 里的代码相当于 __exit__，负责清理资源。
        print(f"关闭 {name}")


with managed_resource("数据库连接") as name:
    print(f"使用 {name}")  # 使用 数据库连接


print("\n=== suppress 忽略指定异常 ===")

with suppress(ValueError):
    # 只忽略指定异常，适合“失败也没关系”的小范围代码。
    int("not-a-number")

print("程序继续执行")  # 程序继续执行


print("\n=== closing 自动调用 close() ===")


class Connection:
    def __init__(self):
        print("连接已建立")

    def close(self):
        print("连接已关闭")


with closing(Connection()) as connection:
    print(type(connection).__name__)  # Connection


print("\n=== redirect_stdout 捕获输出 ===")

buffer = StringIO()

# redirect_stdout 临时把 print 输出重定向到 file-like object。
with redirect_stdout(buffer):
    print("第一行")
    print("第二行")

print(buffer.getvalue().splitlines())  # ['第一行', '第二行']


print("\n=== ExitStack 管理多个资源 ===")

with ExitStack() as stack:
    # enter_context 可以动态进入多个上下文管理器。
    first = stack.enter_context(managed_resource("缓存"))
    second = stack.enter_context(managed_resource("日志"))
    print(f"使用 {first} 和 {second}")  # 使用 缓存 和 日志

# ExitStack 退出时会按后进先出的顺序清理资源。
print("全部资源已释放")  # 全部资源已释放
```

## 🔍 师兄给你拆开讲

`with Resource("文件") as resource:` 会先调用 `__enter__()`，把返回值交给 `resource`，代码块结束后再调用 `__exit__()`。`__exit__()` 返回 `False` 表示不吞异常，让异常继续向外抛。

`@contextmanager` 把生成器函数变成上下文管理器。`yield` 之前是进入逻辑，`yield` 的值是 `as` 后面的变量，`finally` 里写清理逻辑。

`suppress(ValueError)` 只适合很小范围、明确可忽略的异常。不要用它包住一大段业务代码，否则真正的问题会被悄悄吞掉。

`closing(obj)` 适合那些有 `close()` 方法但没有实现 `__enter__` / `__exit__` 的老对象或第三方对象。

`redirect_stdout()` 可以临时把 `print()` 输出重定向到文件、内存缓冲区等 file-like object。测试命令行输出时很有用。

`ExitStack` 适合“资源数量运行时才知道”的情况。它会按进入顺序记录清理动作，退出时按后进先出的顺序释放资源。

## 🏃 跑一下试试

```bash
cd 56-contextlib
python contextlib_demo.py
```

输出：

```text
=== 手写上下文管理器 ===
打开 文件
使用 文件
关闭 文件

=== @contextmanager 简化写法 ===
打开 数据库连接
使用 数据库连接
关闭 数据库连接

=== suppress 忽略指定异常 ===
程序继续执行

=== closing 自动调用 close() ===
连接已建立
Connection
连接已关闭

=== redirect_stdout 捕获输出 ===
['第一行', '第二行']

=== ExitStack 管理多个资源 ===
打开 缓存
打开 日志
使用 缓存 和 日志
关闭 日志
关闭 缓存
全部资源已释放
```

## 💡 师兄的提醒

上下文管理器适合管理“成对动作”：打开/关闭、加锁/解锁、进入/恢复、开始/提交或回滚。

如果只是想少写几行 `try/finally`，`@contextmanager` 很合适；如果资源的生命周期和状态比较复杂，手写类会更清楚。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `__enter__()` | 进入 `with` 时执行 |
| `__exit__()` | 离开 `with` 时执行 |
| `@contextmanager` | 用生成器函数创建上下文管理器 |
| `yield` | 分隔进入逻辑和退出逻辑 |
| `suppress()` | 小范围忽略指定异常 |
| `closing()` | 自动调用对象的 `close()` |
| `redirect_stdout()` | 临时重定向标准输出 |
| `ExitStack` | 动态管理多个上下文管理器 |

## ➡️ 下一关

下一关：[requests](../57-requests/README.md)。
