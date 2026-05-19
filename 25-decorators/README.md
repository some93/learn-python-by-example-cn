# 第 25 关：装饰器（师兄带你学 Python）

## 🎯 这一关你会学到

- Decorator 装饰器
- @语法糖的本质：高阶函数
- functools.wraps 保留原函数信息
- 带参数的装饰器（三层嵌套）

## 🤔 先想一个问题

装饰器就像手机壳——不改变手机本身，但加了保护和新功能。@decorator 就是给函数「套壳」。

## 📖 看代码

```python
# 装饰器（Decorator）

import functools
import time

# 最基本的装饰器：打印日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper

@log
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# 调用 say_hello()
# Hello!

# @log 等价于 say_hello = log(say_hello)

# 带参数的装饰器
def log_with_prefix(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] 调用 {func.__name__}()")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_prefix("DEBUG")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 计时装饰器
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时 {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(0.1)
    return "done"

print(slow_func())

# functools.wraps 保留原函数信息
print(say_hello.__name__)   # say_hello（不是 wrapper）
```

## 🔍 师兄给你逐行拆

装饰器本质是一个接收函数并返回新函数的高阶函数——在不修改原函数代码的情况下，给函数添加额外功能（日志、计时、权限检查等）。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python decorators.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **@decorator 等价于 func = decorator(func)**
- **functools.wraps 保留 __name__ 等信息**
- **带参数装饰器需要三层函数嵌套**
- **实用装饰器：计时、日志、重试**

## 🎓 这一关的知识点清单

- **Decorator 装饰器**
- **@语法糖的本质：高阶函数**
- **functools.wraps 保留原函数信息**
- **带参数的装饰器（三层嵌套）**

## ➡️ 下一关

本关搞定！接下来学 偏函数 👉 [下一关：偏函数 →](../26-partial-functions/)
