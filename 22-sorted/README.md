# 第 22 关：sorted（师兄带你学 Python）

## 🎯 这一关你会学到

- `sorted()` 的基本用法
- `key` 参数如何自定义排序规则
- `reverse=True` 如何反向排序
- 排序稳定性：相同 key 的元素保持原相对顺序
- `sorted()` 和 `list.sort()` 的区别

## 🤔 先想一个问题

快递站要整理包裹。默认可以按编号排，但站长也可以说：「今天按重量排」「今天按目的地排」「今天从大到小排」。

Python 的 `sorted()` 也是这样：默认按元素本身排序；如果你给它一个 `key`，它就按你指定的规则排序。

## 📖 看代码

```python
# sorted：排序函数


print("=== 基本排序 ===")

numbers = [36, 5, -12, 9, -21]
# sorted() 返回新列表，不会修改原列表。
print(sorted(numbers))
print(numbers)


print("\n=== key：自定义排序规则 ===")

# key 指定“按什么值排序”，这里按绝对值排序。
print(sorted(numbers, key=abs))

words = ["bob", "about", "Zoo", "Credit"]
print(sorted(words))
# 忽略大小写排序时，可以把每个单词先转成小写再比较。
print(sorted(words, key=str.lower))


print("\n=== reverse：反向排序 ===")

print(sorted(numbers, reverse=True))
# key 和 reverse 可以一起使用：先按绝对值排序，再反向。
print(sorted(numbers, key=abs, reverse=True))


print("\n=== 对字典列表排序 ===")

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 85},
    {"name": "Diana", "score": 92},
]

# 按分数从高到低排序。
by_score = sorted(students, key=lambda student: student["score"], reverse=True)
for student in by_score:
    print(f"{student['name']}: {student['score']}")

# 元组 key 可以实现多条件排序：先按分数降序，再按姓名升序。
by_score_name = sorted(students, key=lambda student: (-student["score"], student["name"]))
print([student["name"] for student in by_score_name])


print("\n=== key 函数只调用一次 ===")

calls = []


def by_length(word):
    # 记录 key 函数被调用的顺序。
    calls.append(word)
    return len(word)


print(sorted(["pear", "fig", "apple"], key=by_length))
print(calls)


print("\n=== sorted() vs list.sort() ===")

data = [3, 1, 2]
new_data = sorted(data)
print(data)
print(new_data)

# list.sort() 会原地修改列表，并返回 None。
result = data.sort()
print(data)
print(result)
```

## 🔍 师兄给你逐行拆

### `sorted(numbers)` —— 返回一个新列表

```python
numbers = [36, 5, -12, 9, -21]
print(sorted(numbers))
print(numbers)
```

**这行在干嘛？**

`sorted(numbers)` 会把数字从小到大排序，得到：

```python
[-21, -12, 5, 9, 36]
```

但原列表 `numbers` 不会被修改，还是：

```python
[36, 5, -12, 9, -21]
```

**为什么这么写？**

`sorted()` 是一个通用函数，接收任何可迭代对象，返回一个新的列表。它不会原地修改输入数据。

---

### `key=abs` —— 按“处理后的值”排序

```python
print(sorted(numbers, key=abs))
```

**这行在干嘛？**

`key=abs` 表示排序时先对每个数字取绝对值，再按绝对值大小排序。

原始数字：

```python
[36, 5, -12, 9, -21]
```

排序用的 key：

```python
[36, 5, 12, 9, 21]
```

所以结果是：

```python
[5, 9, -12, -21, 36]
```

**生活类比**

快递包裹本身不能变，但你可以拿“重量”当排序依据。`key` 就是告诉 Python：别直接看包裹，看这个包裹算出来的排序指标。

---

### 字符串排序和忽略大小写

```python
words = ["bob", "about", "Zoo", "Credit"]
print(sorted(words))
print(sorted(words, key=str.lower))
```

**这行在干嘛？**

默认字符串排序按 Unicode 码位排序。大写字母通常排在小写字母前面，所以结果是：

```python
['Credit', 'Zoo', 'about', 'bob']
```

如果传 `key=str.lower`，排序前先把每个单词临时转成小写比较，于是得到：

```python
['about', 'bob', 'Credit', 'Zoo']
```

**容易踩的坑**

`key=str.lower` 不会真的修改原字符串。它只是在排序时拿小写结果做比较，最终列表里还是原来的字符串。

---

### `reverse=True` —— 反向排序

```python
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=abs, reverse=True))
```

**这行在干嘛？**

`reverse=True` 表示倒序。

第一行按数字本身从大到小排：

```python
[36, 9, 5, -12, -21]
```

第二行按绝对值从大到小排：

```python
[36, -21, -12, 9, 5]
```

---

### 对字典列表排序

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 85},
    {"name": "Diana", "score": 92},
]

by_score = sorted(students, key=lambda student: student["score"], reverse=True)
```

**这行在干嘛？**

`students` 是一组字典。字典之间不能直接比较大小，所以要用 `key` 指定排序依据：按 `score` 排。

`reverse=True` 表示高分在前。

**排序稳定性是什么？**

Bob 和 Diana 都是 92 分。因为 Bob 在原列表里排在 Diana 前面，所以排序后 Bob 仍然在 Diana 前面。

这叫**稳定排序**：如果两个元素的 key 相等，它们原本的相对顺序会保留。

**多条件排序**

```python
by_score_name = sorted(students, key=lambda student: (-student["score"], student["name"]))
```

这里的 key 是一个元组：

1. 先按 `-score` 排，相当于分数从高到低；
2. 分数相同，再按 `name` 字母顺序排。

---

### key 函数只调用一次

```python
calls = []


def by_length(word):
    calls.append(word)
    return len(word)


print(sorted(["pear", "fig", "apple"], key=by_length))
print(calls)
```

**这行在干嘛？**

这个例子故意记录 `key` 函数被调用过哪些单词。输出会看到：

```python
['pear', 'fig', 'apple']
```

每个元素只调用一次 `key` 函数，而不是比较时反复调用。这意味着你可以放心在 `key` 里做一些简单计算。

**但也别太重**

如果 `key` 函数里做网络请求、数据库查询，那还是很危险。排序前先把需要的数据准备好，更稳。

---

### `sorted()` vs `list.sort()`

```python
data = [3, 1, 2]
new_data = sorted(data)
print(data)
print(new_data)

result = data.sort()
print(data)
print(result)
```

**这行在干嘛？**

`sorted(data)` 返回一个新列表，不改原列表：

```python
data      -> [3, 1, 2]
new_data  -> [1, 2, 3]
```

`data.sort()` 会原地修改 `data`，并且返回 `None`：

```python
data   -> [1, 2, 3]
result -> None
```

**容易踩的坑**

新手常写：

```python
data = data.sort()
```

然后发现 `data` 变成了 `None`。记住：`sort()` 是原地排序，不要接返回值。

## 🏃 跑一下试试

```bash
$ python sorted.py
=== 基本排序 ===
[-21, -12, 5, 9, 36]
[36, 5, -12, 9, -21]

=== key：自定义排序规则 ===
[5, 9, -12, -21, 36]
['Credit', 'Zoo', 'about', 'bob']
['about', 'bob', 'Credit', 'Zoo']

=== reverse：反向排序 ===
[36, 9, 5, -12, -21]
[36, -21, -12, 9, 5]

=== 对字典列表排序 ===
Bob: 92
Diana: 92
Alice: 85
Charlie: 85
['Bob', 'Diana', 'Alice', 'Charlie']

=== key 函数只调用一次 ===
['fig', 'pear', 'apple']
['pear', 'fig', 'apple']

=== sorted() vs list.sort() ===
[3, 1, 2]
[1, 2, 3]
[1, 2, 3]
None
```

## 💡 师兄的碎碎念

- `sorted(iterable)` 返回新列表，不修改原数据。
- `list.sort()` 原地修改列表，返回 `None`。
- `key` 是排序规则，常见写法有 `key=abs`、`key=str.lower`、`key=lambda x: x["score"]`。
- Python 的排序是稳定排序，相同 key 的元素会保留原来的相对顺序。
- 多条件排序可以让 `key` 返回元组，比如 `key=lambda s: (-s["score"], s["name"])`。

## 🎓 这一关的知识点清单

- **sorted()**：接收可迭代对象，返回排序后的新列表。
- **key 参数**：为每个元素计算排序依据。
- **reverse=True**：倒序排列。
- **稳定排序**：key 相等时保持原相对顺序。
- **多条件排序**：让 key 返回元组，按元组顺序逐项比较。
- **list.sort()**：列表原地排序，返回 `None`。

## ➡️ 下一关

排序搞定。下一关开始进入闭包：函数不但能被调用，还能被返回，并且带着外层变量一起“打包带走” 👉 [下一关：返回函数（闭包） →](../23-closures/)


