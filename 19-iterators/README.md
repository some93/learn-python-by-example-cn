# 第 19 关：迭代器（师兄带你学 Python）

## 🎯 这一关你会学到

- `Iterable` 和 `Iterator` 的区别
- `iter()` 和 `next()` 的作用
- `for` 循环背后的真实执行过程
- 生成器为什么天然就是迭代器
- 如何实现自定义迭代器，以及一次性迭代器和可重复遍历对象的差别

## 🤔 先想一个问题

一本书可以反复读，这叫**可迭代对象**：你每次翻开它，都能从第一页重新开始。

书签就不一样。书签记录你当前读到哪里，每翻一次就往后挪一页，这叫**迭代器**。书签走到最后，再往后翻就没了。

Python 里的 `Iterable` 像书，`Iterator` 像书签。`iter()` 是拿书签，`next()` 是翻下一页。

## 📖 看代码

```python
# 迭代器（Iterator）

from collections.abc import Iterable, Iterator


print("=== Iterable vs Iterator ===")

numbers = [1, 2, 3]

# 列表可以被 for 遍历，所以它是 Iterable。
print(isinstance(numbers, Iterable))  # True
# 但列表本身不是 Iterator，因为它没有记录“当前走到哪里”。
print(isinstance(numbers, Iterator))  # False

# iter() 会把可迭代对象转换成迭代器。
it = iter(numbers)
print(isinstance(it, Iterable))  # True
print(isinstance(it, Iterator))  # True


print("\n=== iter() 和 next() ===")

# next() 每调用一次，就从迭代器里取出下一个元素。
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
try:
    # 迭代器耗尽后，再取会抛出 StopIteration。
    print(next(it))
except StopIteration:
    print("没有更多元素了")


print("\n=== for 循环的本质 ===")

it = iter([1, 2, 3])
while True:
    try:
        # for 循环内部本质上就是反复调用 next()。
        value = next(it)
        print(value, end=" ")
    except StopIteration:
        break
print()


print("\n=== 生成器天生就是 Iterator ===")

g = (x * x for x in range(3))
print(isinstance(g, Iterator))  # True
print(list(g))                  # [0, 1, 4]
# 生成器也是一次性的，消费完之后再次遍历为空。
print(list(g))                  # []


print("\n=== 自定义一次性迭代器 ===")


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # 一次性迭代器通常返回 self。
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


countdown = Countdown(3)
print(list(countdown))  # [3, 2, 1]
print(list(countdown))  # []


print("\n=== 自定义可重复遍历的对象 ===")


class Team:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        # 每次返回一个新的列表迭代器，所以 Team 可以重复遍历。
        return iter(self.members)


team = Team(["小王", "小李", "小张"])
print(list(team))  # ['小王', '小李', '小张']
print(list(team))  # ['小王', '小李', '小张']
```

## 🔍 师兄给你逐行拆

### `Iterable` 和 `Iterator` 不是一回事

```python
numbers = [1, 2, 3]

print(isinstance(numbers, Iterable))
print(isinstance(numbers, Iterator))

it = iter(numbers)
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))
```

**这行在干嘛？**

列表 `numbers` 是 `Iterable`，因为它可以被 `for...in` 遍历。但它不是 `Iterator`，因为不能直接对列表不断 `next(numbers)`。

`iter(numbers)` 会返回一个迭代器 `it`。这个 `it` 既是 `Iterable`，也是 `Iterator`。

**为什么要分这么细？**

因为「能遍历」和「正在遍历到某个位置」不是同一件事。

- `Iterable`：我可以开始遍历你。
- `Iterator`：我已经在遍历路上，并且知道下一个元素是谁。

---

### `next()` 会推进迭代器

```python
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("没有更多元素了")
```

**这行在干嘛？**

前三次 `next(it)` 依次拿到 `1`、`2`、`3`。第四次已经没有元素了，于是抛出 `StopIteration`。

**生活类比**

`next()` 就像翻页。你翻过的页不会自动回去，再翻就是下一页。翻到最后再翻，书签告诉你：没了。

**容易踩的坑**

迭代器通常是一次性的。你把它传给某段代码消费掉之后，后面再用可能就是空的。

---

### `for` 循环本质上就是 `iter()` + `next()`

```python
it = iter([1, 2, 3])
while True:
    try:
        value = next(it)
        print(value, end=" ")
    except StopIteration:
        break
print()
```

**这行在干嘛？**

这段 `while True` 手动模拟了 `for` 循环：

```python
for value in [1, 2, 3]:
    print(value, end=" ")
```

Python 的 `for` 循环会先调用 `iter()` 拿到迭代器，再不断调用 `next()`。遇到 `StopIteration`，循环结束。

**为什么你平时没看到 `StopIteration`？**

因为 `for` 循环帮你吞掉了这个异常，把它当成「循环正常结束」的信号。

---

### 生成器天然就是迭代器

```python
g = (x * x for x in range(3))
print(isinstance(g, Iterator))
print(list(g))
print(list(g))
```

**这行在干嘛？**

生成器 `g` 本身就是 `Iterator`。第一次 `list(g)` 会消费出 `[0, 1, 4]`，第二次再消费就只剩空列表 `[]`。

这和上一关讲的「生成器只能消费一次」是同一个原因：它内部保存了当前进度。

---

### 自定义一次性迭代器

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
```

**这行在干嘛？**

`Countdown(3)` 会依次产出 `3`、`2`、`1`。它实现了两个特殊方法：

- `__iter__()`：返回迭代器对象本身；
- `__next__()`：返回下一个值，没有值时抛出 `StopIteration`。

**为什么第二次 `list(countdown)` 是空的？**

因为 `Countdown` 把进度存在 `self.current` 里。第一次遍历结束后，`self.current` 已经变成 `0`，第二次自然没东西可取。

---

### 自定义可重复遍历的对象

```python
class Team:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)
```

**这行在干嘛？**

`Team` 不是自己保存遍历进度，而是每次调用 `__iter__()` 时，都基于内部列表 `self.members` 创建一个新的迭代器。

所以：

```python
print(list(team))
print(list(team))
```

两次都能输出完整成员列表。

**什么时候用哪种？**

- 如果对象表示一条数据流、一个文件读取过程、一个倒计时过程，通常做成一次性迭代器。
- 如果对象表示一个容器，比如班级、队伍、购物车，通常应该支持重复遍历。

## 🏃 跑一下试试

```bash
$ python iterators.py
=== Iterable vs Iterator ===
True
False
True
True

=== iter() 和 next() ===
1
2
3
没有更多元素了

=== for 循环的本质 ===
1 2 3 

=== 生成器天生就是 Iterator ===
True
[0, 1, 4]
[]

=== 自定义一次性迭代器 ===
[3, 2, 1]
[]

=== 自定义可重复遍历的对象 ===
['小王', '小李', '小张']
['小王', '小李', '小张']
```

## 💡 师兄的碎碎念

- `Iterable` 只要求对象能返回一个迭代器；`Iterator` 还要能通过 `next()` 产出下一个值。
- 列表、字符串、字典是 `Iterable`，但不是 `Iterator`；生成器是 `Iterator`。
- `for` 循环的核心流程是：`iter(obj)`，不断 `next()`，遇到 `StopIteration` 停止。
- `__iter__()` 返回 `self` 的对象通常是一次性迭代器。
- 容器类对象一般应该在 `__iter__()` 里返回一个新的迭代器，这样才能重复遍历。

## 🎓 这一关的知识点清单

- **Iterable**：可迭代对象，能被 `for...in` 遍历，核心是能提供 `__iter__()`。
- **Iterator**：迭代器，能被 `next()` 推进，核心是实现 `__next__()`。
- **iter()**：从可迭代对象获取迭代器。
- **next()**：从迭代器获取下一个值。
- **StopIteration**：迭代结束的信号，`for` 循环会自动处理。
- **自定义迭代器**：实现 `__iter__()` 和 `__next__()`。

## ➡️ 下一关

迭代器打通后，函数式编程就更好理解了。下一关看 `map()` 和 `reduce()`：一个负责逐个加工，一个负责累积合并 👉 [下一关：map/reduce →](../20-map-reduce/)


