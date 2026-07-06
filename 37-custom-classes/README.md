# 第 37 关：定制类（师兄带你学 Python）

## 🎯 这一关你会学到

- `__str__` / `__repr__` 如何自定义对象显示
- `__iter__` / `__next__` 如何让对象可迭代
- `__getitem__` 如何支持下标和切片
- `__getattr__` 如何处理不存在的属性
- `__call__` 如何让实例像函数一样调用

## 🤔 先想一个问题

你打印一个自己写的对象，屏幕上显示：

```text
<__main__.Student object at 0x...>
```

这玩意对人类很不友好。你更希望它显示：

```python
Student(Alice)
```

Python 提供了一批特殊方法，也叫魔法方法。它们不是给你直接调用的，而是让 Python 的内置语法自动调用，比如 `print(obj)`、`len(obj)`、`obj[0]`、`for x in obj`。

## 📖 看代码

```python
# 定制类


print("=== __str__ 和 __repr__ ===")


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # print(obj) 会优先使用 __str__ 的返回值。
        return f"Student({self.name})"

    # 交互环境、列表展示等场景会使用 __repr__。
    __repr__ = __str__


student = Student("Alice")
print(student)
print([student])


print("\n=== __iter__ 和 __next__ ===")


class Fib:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        # 返回 self 表示这个对象自己就是迭代器。
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.max_value:
            raise StopIteration
        return self.a


print(list(Fib(100)))


print("\n=== __getitem__ 支持下标和切片 ===")


class FibList:
    def __getitem__(self, item):
        # 为了演示下标和切片，先准备一段斐波那契数列。
        values = [1, 1]
        while len(values) <= 20:
            values.append(values[-1] + values[-2])

        if isinstance(item, int):
            # fib[5] 会走这里。
            return values[item]
        if isinstance(item, slice):
            # fib[:6] 会把 slice 对象传进来。
            return values[item]
        raise TypeError("下标必须是整数或切片")


fib = FibList()
print(fib[0])
print(fib[5])
print(fib[:6])
print(fib[2:8:2])


print("\n=== __getattr__ 动态属性 ===")


class Chain:
    def __init__(self, path=""):
        self._path = path

    def __getattr__(self, name):
        # 只有正常属性找不到时，才会调用 __getattr__。
        return Chain(f"{self._path}/{name}")

    def __str__(self):
        return self._path or "/"

    __repr__ = __str__


chain = Chain()
print(chain.api.users.list)
print(chain._path == "")


print("\n=== __call__ 让实例像函数一样调用 ===")


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, step=1):
        # 定义 __call__ 后，实例就能像函数一样被调用。
        self.count += step
        return self.count


counter = Counter()
print(counter())
print(counter())
print(counter(10))
print(callable(counter))
print(callable(Student))
print(callable(student))
```

## 🔍 师兄给你逐行拆

### `__str__` 和 `__repr__` —— 让对象显示成人话

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student({self.name})"

    __repr__ = __str__
```

**这行在干嘛？**

`print(student)` 会调用 `student.__str__()`。所以我们返回 `Student(Alice)`，打印出来就更友好。

`__repr__` 更偏开发者调试场景，比如对象出现在列表里：

```python
print([student])
```

列表内部会用元素的 `repr()`，所以这里把 `__repr__` 也指向 `__str__`。

**区别怎么记？**

- `__str__`：给用户看的；
- `__repr__`：给开发者看的，最好能明确表达对象状态。

---

### `__iter__` 和 `__next__` —— 让对象可以被遍历

```python
class Fib:
    def __iter__(self):
        return self

    def __next__(self):
        ...
```

**这行在干嘛？**

实现 `__iter__()` 和 `__next__()` 后，`Fib` 实例就是迭代器，可以用于：

```python
for n in Fib(100):
    ...
```

或者：

```python
list(Fib(100))
```

当没有下一个值时，`__next__()` 抛出 `StopIteration`，循环结束。

**和前面迭代器章节的关系**

这就是第 19 关讲的迭代器协议：`for` 循环背后会调用 `iter()` 和 `next()`，对应到类里就是 `__iter__()` 和 `__next__()`。

---

### `__getitem__` —— 让对象支持 `obj[index]`

```python
class FibList:
    def __getitem__(self, item):
        ...
```

**这行在干嘛？**

实现 `__getitem__()` 后，对象可以用方括号访问：

```python
fib[0]
fib[5]
```

Python 会把下标传给 `__getitem__()` 的 `item` 参数。

---

### 支持切片

```python
if isinstance(item, slice):
    return values[item]
```

**这行在干嘛？**

当你写：

```python
fib[:6]
fib[2:8:2]
```

传进 `__getitem__()` 的不是整数，而是一个 `slice` 对象。我们判断它是切片后，直接用列表的切片能力返回结果。

**容易踩的坑**

很多教程只写整数下标，不写切片。结果你以为 `__getitem__` 自动支持切片，其实不是。你要自己处理 `slice` 类型。

---

### `__getattr__` —— 属性不存在时才触发

```python
class Chain:
    def __getattr__(self, name):
        return Chain(f"{self._path}/{name}")
```

**这行在干嘛？**

当你访问一个不存在的属性，比如：

```python
chain.api
```

Python 找不到 `api`，才会调用 `__getattr__("api")`。这里返回一个新的 `Chain("/api")`。

继续访问：

```python
chain.api.users.list
```

就会一步步拼成 `/api/users/list`。

**已有属性不会触发**

`chain._path` 是真实存在的属性，所以访问它不会调用 `__getattr__()`。示例里用 `chain._path == ""` 输出 `True`，说明根路径对象自己的 `_path` 仍然是空字符串。

---

### `__call__` —— 实例也能像函数一样

```python
class Counter:
    def __call__(self, step=1):
        self.count += step
        return self.count
```

**这行在干嘛？**

实现 `__call__()` 后，实例可以像函数一样调用：

```python
counter()
counter(10)
```

Python 会把这类调用转给 `counter.__call__()`。

**`callable()` 判断什么？**

`callable(obj)` 判断对象能不能被调用。

- 类 `Student` 可以调用，因为 `Student("Alice")` 会创建实例；
- `counter` 可以调用，因为实现了 `__call__`；
- 普通 `student` 实例不能调用，因为没实现 `__call__`。

## 🏃 跑一下试试

```bash
$ python custom-classes.py
=== __str__ 和 __repr__ ===
Student(Alice)
[Student(Alice)]

=== __iter__ 和 __next__ ===
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

=== __getitem__ 支持下标和切片 ===
1
8
[1, 1, 2, 3, 5, 8]
[2, 5, 13]

=== __getattr__ 动态属性 ===
/api/users/list
True

=== __call__ 让实例像函数一样调用 ===
1
2
12
True
True
False
```

## 💡 师兄的碎碎念

- 特殊方法通常不是手动调用，而是被 Python 语法触发。
- `print(obj)` 触发 `__str__`，列表调试输出更偏向 `__repr__`。
- `for x in obj` 依赖 `__iter__` / `__next__`。
- `obj[index]` 和 `obj[start:stop]` 都会走 `__getitem__`，但参数类型不同。
- `__getattr__` 只在属性不存在时触发，不会拦截已有属性。
- 实现 `__call__` 后，实例就可以像函数一样调用。

## 🎓 这一关的知识点清单

- **__str__**：自定义面向用户的字符串表示。
- **__repr__**：自定义面向开发者的调试表示。
- **__iter__ / __next__**：实现迭代器协议。
- **__getitem__**：支持下标访问和切片访问。
- **__getattr__**：属性不存在时动态处理。
- **__call__**：让实例可调用。
- **callable()**：判断对象是否可以像函数一样调用。

## ➡️ 下一关

定制类讲完，下一关看枚举类：用一组有名字的固定值替代散落的魔法数字和字符串 👉 [下一关：枚举类 →](../38-enum/)




