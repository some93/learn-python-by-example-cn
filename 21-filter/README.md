# 第 21 关：filter

## 🎯 这一关你会学到

- `filter(func, iterable)` 的基本用法
- `filter()` 返回惰性迭代器，不是列表
- 判断函数返回真值就保留，返回假值就丢弃
- `filter(None, iterable)` 的特殊用法
- 用 `filter()` 实现一个简单的素数筛

## 🤔 先想一个问题

`filter` 像安检门。每个人都过一遍，符合条件的放行，不符合条件的拦下。

你的任务不是亲手把每个人挑出来，而是先写清楚「放行标准」。Python 会把这个标准逐个套到数据上。

## 📖 看代码

```python
# filter：过滤序列


print("=== filter 基本用法 ===")


def is_odd(n):
    return n % 2 == 1


# filter 返回惰性迭代器，只保留函数返回真值的元素。
result = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(type(result).__name__)  # filter
print(list(result))           # [1, 3, 5]
# filter 结果消费完之后不能重复使用。
print(list(result))           # []


print("\n=== filter 和列表生成式对比 ===")

numbers = range(1, 11)
# 简单过滤时，列表生成式通常更容易读。
print(list(filter(is_odd, numbers)))       # [1, 3, 5, 7, 9]
print([n for n in range(1, 11) if is_odd(n)])  # [1, 3, 5, 7, 9]


print("\n=== filter(None, iterable) ===")

mixed = [0, 1, "", "Python", [], [1], None, True, False]
# 函数传 None 时，会自动过滤掉所有假值。
print(list(filter(None, mixed)))  # [1, 'Python', [1], True]


print("\n=== 删除空字符串 ===")


def not_empty(text):
    # text and ... 可以避免 None 调用 strip() 报错。
    return text and text.strip()


items = ["A", "", "B", None, "C", "  "]
print(list(filter(not_empty, items)))  # ['A', 'B', 'C']


print("\n=== 用 filter 求素数 ===")


def odd_numbers():
    n = 1
    while True:
        n += 2
        # 素数里除了 2 都是奇数，所以只生成奇数候选。
        yield n


def not_divisible(n):
    # 返回一个过滤函数：剔除能被 n 整除的数。
    return lambda x: x % n != 0


def primes():
    yield 2
    it = odd_numbers()
    while True:
        n = next(it)
        yield n
        # 每发现一个素数，就用它过滤后面的候选数。
        it = filter(not_divisible(n), it)


p = primes()
first_primes = [next(p) for _ in range(20)]
print(first_primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
```

## 🔍 师兄给你逐行拆

### `filter(is_odd, data)` —— 满足条件才留下

```python
def is_odd(n):
    return n % 2 == 1


result = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(type(result).__name__)
print(list(result))
print(list(result))
```

**这行在干嘛？**

`filter()` 会把列表里的每个数字传给 `is_odd()`。返回真值的元素保留，返回假值的元素丢掉。

所以 `[1, 2, 3, 4, 5, 6]` 过滤后得到：

```python
[1, 3, 5]
```

**为什么第二次 `list(result)` 是空列表？**

Python 3 里的 `filter()` 返回的是惰性迭代器。第一次 `list(result)` 已经把它消费完了，第二次自然是 `[]`。

---

### `filter` 和列表生成式怎么选？

```python
numbers = range(1, 11)
print(list(filter(is_odd, numbers)))
print([n for n in range(1, 11) if is_odd(n)])
```

**这行在干嘛？**

这两行效果一样，都是保留奇数：

```python
[1, 3, 5, 7, 9]
```

**为什么要对比？**

列表生成式把过滤条件直接写在一行里，通常更适合新手阅读：

```python
[n for n in numbers if is_odd(n)]
```

`filter()` 在这些场景更顺手：

- 已经有一个现成判断函数；
- 想保留惰性迭代器，不立刻生成列表；
- 和 `map()`、生成器、函数式代码一起使用。

---

### `filter(None, iterable)` —— 自动丢掉假值

```python
mixed = [0, 1, "", "Python", [], [1], None, True, False]
print(list(filter(None, mixed)))
```

**这行在干嘛？**

如果 `filter()` 的第一个参数传 `None`，Python 会直接用每个元素自己的真假值来判断。

这里会丢掉这些假值：

```python
0, "", [], None, False
```

保留下来的是：

```python
[1, 'Python', [1], True]
```

**容易踩的坑**

`filter(None, data)` 不是只删 `None`，它会删除所有假值。比如 `0` 和空字符串也会被删掉。如果你只想删除 `None`，应该写：

```python
[x for x in data if x is not None]
```

---

### 删除空字符串 —— 判断函数不一定非得返回 `True/False`

```python
def not_empty(text):
    return text and text.strip()


items = ["A", "", "B", None, "C", "  "]
print(list(filter(not_empty, items)))
```

**这行在干嘛？**

`not_empty()` 会过滤掉空字符串、`None` 和只包含空格的字符串。

注意它返回的不一定是布尔值：

- `"A"` 返回 `"A"`，是真值，所以保留；
- `""` 返回 `""`，是假值，所以丢弃；
- `None` 返回 `None`，是假值，所以丢弃；
- `"  "` 调用 `.strip()` 后是 `""`，是假值，所以丢弃。

**为什么可以这样？**

Python 判断条件时看的是**真值/假值**，不是必须严格等于 `True` 或 `False`。

---

### 用 `filter()` 求素数

```python
def odd_numbers():
    n = 1
    while True:
        n += 2
        yield n
```

**这行在干嘛？**

`odd_numbers()` 是一个无限生成奇数的生成器：`3, 5, 7, 9, 11...`

因为除了 `2` 以外，偶数都不是素数，所以我们只需要检查奇数。

```python
def not_divisible(n):
    return lambda x: x % n != 0
```

这个函数会生成一个过滤函数：给定一个素数 `n`，返回「不能被 `n` 整除」的判断函数。

```python
def primes():
    yield 2
    it = odd_numbers()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)
```

**这行在干嘛？**

每找到一个新素数 `n`，就把后面的数再过滤一遍：凡是能被 `n` 整除的，都不可能是素数，丢掉。

这就是埃拉托斯特尼筛法的函数式版本。

**容易踩的坑**

这里用 `not_divisible(n)` 固定当前的 `n`，避免在循环里直接写复杂的闭包逻辑。闭包的细节后面第 23 关会讲。

## 🏃 跑一下试试

```bash
$ python filter.py
=== filter 基本用法 ===
filter
[1, 3, 5]
[]

=== filter 和列表生成式对比 ===
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9]

=== filter(None, iterable) ===
[1, 'Python', [1], True]

=== 删除空字符串 ===
['A', 'B', 'C']

=== 用 filter 求素数 ===
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
```

## 💡 师兄的碎碎念

- `filter(func, iterable)` 返回迭代器，不会立刻生成列表。
- 判断函数返回真值就保留，返回假值就丢弃，不要求必须返回 `True`/`False`。
- `filter(None, iterable)` 会删除所有假值，不只是删除 `None`。
- 简单过滤用列表生成式通常更直观；已有判断函数或需要惰性处理时，`filter()` 很合适。
- 素数筛这个例子偏进阶，重点是看懂「一层层过滤」的思想，不必一开始就背下来。

## 🎓 这一关的知识点清单

- **filter()**：按判断函数过滤可迭代对象，保留返回真值的元素。
- **惰性迭代器**：`filter()` 返回迭代器，消费一次就没了。
- **真值/假值**：条件判断看 truthiness，空字符串、空列表、`0`、`None` 都是假值。
- **filter(None, data)**：自动过滤掉所有假值。
- **素数筛**：可以用生成器和 `filter()` 逐层筛掉合数。

## ➡️ 下一关

筛选完数据，下一步常常是排序。下一关看 `sorted()`：默认排序、自定义 key、倒序、以及它和 `list.sort()` 的区别 👉 [下一关：sorted →](../22-sorted/)


