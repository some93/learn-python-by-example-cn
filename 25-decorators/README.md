# 第 25 关：装饰器（师兄带你学 Python）

## 🎯 这一关你会学到

- 装饰器的本质：接收函数，返回新函数
- `@decorator` 语法糖背后发生了什么
- 为什么 wrapper 要接收 `*args, **kwargs`
- 为什么要用 `functools.wraps`
- 带参数装饰器为什么需要三层函数

## 🤔 先想一个问题

装饰器像给手机套壳。手机还是那台手机，但套壳后多了保护、支架、卡槽。

函数也是一样：你不想改原函数代码，但想在它执行前后加日志、鉴权、计数、缓存、重试。装饰器就是给函数“套壳”的工具。

## 📖 看代码

```python
# 装饰器（Decorator）

import functools


print("=== 最基本的装饰器 ===")


def log(func):
    # wrapper 会包住原函数，在调用前后插入额外逻辑。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}()")
        # 装饰器要把原函数的返回值继续返回出去。
        return func(*args, **kwargs)

    return wrapper


# @log 等价于 say_hello = log(say_hello)。
@log
def say_hello():
    print("Hello!")


say_hello()
print(say_hello.__name__)


print("\n=== @ 语法糖的本质 ===")


def greet(name):
    print(f"Hello, {name}!")


# 手动改写函数变量，可以看清 @ 语法糖的本质。
greet = log(greet)
greet("Alice")


print("\n=== 装饰器必须返回原函数结果 ===")


@log
def add(a, b):
    return a + b


print(add(3, 5))


print("\n=== 带参数的装饰器 ===")


def log_with_prefix(prefix):
    # 带参数的装饰器需要多包一层，用来接收装饰器自己的参数。
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] 调用 {func.__name__}()")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_with_prefix("DEBUG")
def fetch_data(url):
    return f"数据来自 {url}"


print(fetch_data("https://example.com"))


print("\n=== 统计调用次数的装饰器 ===")


def count_calls(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # count 在外层函数里，修改它需要 nonlocal。
        nonlocal count
        count += 1
        print(f"{func.__name__} 第 {count} 次调用")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def double(x):
    return x * 2


print(double(10))
print(double(20))
```

## 🔍 师兄给你逐行拆

### `log(func)` —— 装饰器本体

```python
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}()")
        return func(*args, **kwargs)

    return wrapper
```

**这行在干嘛？**

`log()` 接收一个函数 `func`，内部定义一个新函数 `wrapper()`，最后返回 `wrapper`。

以后调用被装饰的函数时，实际先执行的是 `wrapper()`。它先打印日志，再调用原函数。

**为什么 `wrapper` 要写 `*args, **kwargs`？**

因为装饰器不知道将来会装饰什么函数。有的函数没参数，有的有位置参数，有的有关键字参数。

`*args, **kwargs` 相当于万能转发器：调用方传什么参数，wrapper 就原样转给原函数。

---

### `@log` —— 语法糖

```python
@log
def say_hello():
    print("Hello!")
```

**这行在干嘛？**

这段代码等价于：

```python
def say_hello():
    print("Hello!")


say_hello = log(say_hello)
```

也就是说，`say_hello` 这个名字后来指向的已经不是原始函数，而是 `log()` 返回的 `wrapper`。

**生活类比**

原函数是手机，`log` 是手机壳工厂。`@log` 表示手机出厂前先套一层壳，然后你拿到的是套壳后的手机。

---

### `functools.wraps` —— 保留原函数身份信息

```python
@functools.wraps(func)
def wrapper(*args, **kwargs):
    ...
```

**这行在干嘛？**

`functools.wraps(func)` 会把原函数的名字、文档等元信息复制到 `wrapper` 上。

所以：

```python
print(say_hello.__name__)
```

输出的是 `say_hello`，不是 `wrapper`。

**为什么重要？**

调试、日志、测试框架、Web 框架路由经常依赖函数名和元信息。如果不用 `wraps`，很多工具看到的都是 `wrapper`，排查问题会很痛苦。

---

### 装饰器必须返回原函数结果

```python
@log
def add(a, b):
    return a + b


print(add(3, 5))
```

**这行在干嘛？**

`add(3, 5)` 原本应该返回 `8`。装饰器加了日志，但不能把返回值弄丢。

所以 wrapper 里一定要写：

```python
return func(*args, **kwargs)
```

**容易踩的坑**

如果你写成：

```python
func(*args, **kwargs)
```

没有 `return`，那被装饰函数的返回值就会变成 `None`。

---

### 带参数的装饰器 —— 三层函数

```python
def log_with_prefix(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] 调用 {func.__name__}()")
            return func(*args, **kwargs)

        return wrapper

    return decorator
```

**这行在干嘛？**

`@log_with_prefix("DEBUG")` 看起来像给装饰器传了参数。它的执行过程是：

1. 先调用 `log_with_prefix("DEBUG")`，得到真正的装饰器 `decorator`；
2. 再执行 `fetch_data = decorator(fetch_data)`；
3. 调用 `fetch_data()` 时，实际执行 `wrapper()`。

**为什么要三层？**

因为外层要接收装饰器参数 `prefix`，中层接收原函数 `func`，内层接收原函数调用时的参数 `*args, **kwargs`。

---

### 统计调用次数 —— 装饰器也能带状态

```python
def count_calls(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} 第 {count} 次调用")
        return func(*args, **kwargs)

    return wrapper
```

**这行在干嘛？**

`count` 是外层变量，`wrapper()` 每次执行都会修改它。这里用到了上一关闭包里的 `nonlocal`。

被装饰的 `double()` 每调用一次，计数器就加一：

```python
double 第 1 次调用
double 第 2 次调用
```

**为什么这个例子实用？**

很多真实装饰器都需要保存一点状态，比如调用次数、缓存结果、失败重试次数、权限上下文等。

## 🏃 跑一下试试

```bash
$ python decorators.py
=== 最基本的装饰器 ===
调用 say_hello()
Hello!
say_hello

=== @ 语法糖的本质 ===
调用 greet()
Hello, Alice!

=== 装饰器必须返回原函数结果 ===
调用 add()
8

=== 带参数的装饰器 ===
[DEBUG] 调用 fetch_data()
数据来自 https://example.com

=== 统计调用次数的装饰器 ===
double 第 1 次调用
20
double 第 2 次调用
40
```

## 💡 师兄的碎碎念

- 装饰器本质是高阶函数：接收函数，返回新函数。
- `@decorator` 等价于 `func = decorator(func)`。
- wrapper 通常写 `*args, **kwargs`，这样能装饰各种参数形态的函数。
- 写装饰器时几乎总该加 `@functools.wraps(func)`。
- 带参数装饰器是三层：装饰器参数层、原函数层、wrapper 调用层。

## 🎓 这一关的知识点清单

- **Decorator**：在不修改原函数代码的前提下，为函数增加额外行为。
- **@ 语法糖**：`@log` 等价于 `func = log(func)`。
- **wrapper**：包住原函数的新函数，负责前后增强并调用原函数。
- **functools.wraps**：保留原函数的 `__name__`、文档等元信息。
- **带参数装饰器**：外层接收装饰器参数，中层接收原函数，内层处理调用。
- **闭包状态**：装饰器可以通过闭包保存计数、缓存等状态。

## ➡️ 下一关

装饰器之后，我们看函数式编程这一段的最后一个小工具：偏函数。它能帮你提前固定一部分参数，做出更专用的新函数 👉 [下一关：偏函数 →](../26-partial-functions/)


