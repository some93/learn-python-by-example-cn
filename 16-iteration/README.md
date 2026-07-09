# 第 16 关：迭代

## 🎯 这一关你会学到

- `for...in` 的核心思想：直接从可迭代对象里逐个取值
- 如何遍历 `list`、`dict`、字符串等常见对象
- `enumerate()` 同时拿下标和值
- `zip()` 并行遍历多个序列，以及它的截断规则
- 用 `collections.abc.Iterable` 判断对象是否可迭代

## 🤔 先想一个问题

你搬进新宿舍，要逐个认识室友。名单上有三个人，你不会先问「名单长度是多少、下标 0 是谁、下标 1 是谁」；你会直接按名单一个个念名字。

Python 的 `for...in` 就是这个思路：**别老惦记下标，直接关心每次拿到的元素**。

这也是 Python 和很多 C/Java 初学写法不一样的地方。Python 当然能写 `for i in range(len(L))`，但大多数时候，更自然的写法是：

```python
for item in L:
    ...
```

## 📖 看代码

```python
# 迭代

from collections.abc import Iterable


print("=== 遍历列表 ===")

students = ["小王", "小李", "小张"]

for student in students:               # 依次输出：小王 / 小李 / 小张
    print(student)


print("\n=== 遍历字典 ===")

scores = {"小王": 85, "小李": 92, "小张": 78}

# 直接遍历 dict，拿到的是 key
for name in scores:                    # 小王: 85 / 小李: 92 / 小张: 78
    print(f"{name}: {scores[name]}")

# 只遍历 value
for score in scores.values():          # 85 / 92 / 78
    print(score)

# 同时遍历 key 和 value
for name, score in scores.items():     # 小王 => 85 / 小李 => 92 / 小张 => 78
    print(f"{name} => {score}")


print("\n=== 遍历字符串 ===")

for ch in "Python":                    # P y t h o n
    print(ch, end=" ")
print()


print("\n=== enumerate：同时拿下标和值 ===")

tasks = ["打开电脑", "写代码", "提交作业"]

for index, task in enumerate(tasks):   # 0: 打开电脑 / 1: 写代码 / 2: 提交作业
    print(f"{index}: {task}")

for step, task in enumerate(tasks, start=1):  # 第 1 步：打开电脑 / 第 2 步：写代码 / 第 3 步：提交作业
    print(f"第 {step} 步：{task}")


print("\n=== zip：并行遍历 ===")

names = ["Alice", "Bob", "Charlie"]
math_scores = [85, 92, 78]
english_scores = [88, 90]

for name, score in zip(names, math_scores):   # Alice: 85 / Bob: 92 / Charlie: 78
    print(f"{name}: {score}")

# zip 遇到最短的序列就停止，Charlie 没有英语成绩，所以不会输出
for name, score in zip(names, english_scores):  # Alice English: 88 / Bob English: 90
    print(f"{name} English: {score}")


print("\n=== 判断是否可迭代 ===")

print(isinstance("hello", Iterable))  # True
print(isinstance(123, Iterable))      # False
print(isinstance([1, 2], Iterable))   # True
print(isinstance({"a": 1}, Iterable)) # True
```

## 🔍 师兄给你逐行拆

### `for item in students` —— 直接拿元素

```python
students = ["小王", "小李", "小张"]

for student in students:
    print(student)
```

**这行在干嘛？**

`for...in` 会从 `students` 里一个一个取元素。第一次取到 `"小王"`，第二次取到 `"小李"`，第三次取到 `"小张"`。

**为什么这么写？**

Python 的循环更强调「遍历对象本身」，不是「操作下标」。如果你不需要下标，就别写：

```python
for i in range(len(students)):
    print(students[i])
```

这个写法不是错，但更啰嗦，也更容易写出越界问题。

**生活类比**

点名时你会直接念人名，不会说「第 0 个同学请回答、第 1 个同学请回答」。Python 的 `for student in students` 就是在点名。

---

### 遍历 `dict` —— 默认拿 key

```python
scores = {"小王": 85, "小李": 92, "小张": 78}

for name in scores:
    print(f"{name}: {scores[name]}")
```

**这行在干嘛？**

直接遍历字典时，拿到的是 **key**，也就是这里的学生名字。再用 `scores[name]` 根据 key 取 value，也就是分数。

**为什么这么写？**

字典本质是 key 到 value 的映射。默认遍历 key，是因为 key 才是字典查找的入口。

如果你只关心分数，用 `.values()`：

```python
for score in scores.values():
    print(score)
```

如果你同时关心名字和分数，用 `.items()`：

```python
for name, score in scores.items():
    print(f"{name} => {score}")
```

**容易踩的坑**

很多新手以为 `for x in dict` 会拿到 value，结果拿到的是 key。记住三件套：

- `for key in d`：遍历 key
- `for value in d.values()`：遍历 value
- `for key, value in d.items()`：同时遍历 key 和 value

---

### 遍历字符串 —— 字符串也是可迭代对象

```python
for ch in "Python":
    print(ch, end=" ")
print()
```

**这行在干嘛？**

字符串可以被逐字符遍历。这里依次拿到 `P`、`y`、`t`、`h`、`o`、`n`。

`print(ch, end=" ")` 表示打印后不要换行，而是在后面接一个空格。最后单独 `print()` 一次，用来补一个换行。

**为什么这么写？**

Python 里很多对象都支持迭代：列表、元组、字符串、字典、集合、文件对象、生成器。只要对象能「一次吐一个元素」，就可以被 `for...in` 遍历。

---

### `enumerate()` —— 同时拿下标和值

```python
tasks = ["打开电脑", "写代码", "提交作业"]

for index, task in enumerate(tasks):
    print(f"{index}: {task}")

for step, task in enumerate(tasks, start=1):
    print(f"第 {step} 步：{task}")
```

**这行在干嘛？**

`enumerate(tasks)` 会把每个元素变成一对数据：`(下标, 元素)`。

默认下标从 `0` 开始。如果你想让编号从 `1` 开始，传 `start=1`。

**为什么这么写？**

当你既需要元素，又需要下标时，用 `enumerate()` 比 `range(len(...))` 更清楚。

```python
# 不推荐：绕了一圈
for i in range(len(tasks)):
    print(i, tasks[i])

# 推荐：直接拿到 i 和 task
for i, task in enumerate(tasks):
    print(i, task)
```

---

### `zip()` —— 两张表并排拉拉链

```python
names = ["Alice", "Bob", "Charlie"]
math_scores = [85, 92, 78]

for name, score in zip(names, math_scores):
    print(f"{name}: {score}")
```

**这行在干嘛？**

`zip(names, math_scores)` 会把多个序列按位置配对：

```python
("Alice", 85)
("Bob", 92)
("Charlie", 78)
```

所以循环里可以直接写：

```python
for name, score in zip(names, math_scores):
```

**容易踩的坑**

`zip()` 会在最短的序列用完时停止：

```python
english_scores = [88, 90]

for name, score in zip(names, english_scores):
    print(name, score)
```

这里只会输出 Alice 和 Bob，Charlie 没有英语成绩，所以不会报错，也不会补 `None`，而是直接停。

如果你希望长度不一致时报错或补默认值，后面可以学 `itertools.zip_longest()`。

---

### `Iterable` —— 判断一个对象能不能被遍历

```python
from collections.abc import Iterable

print(isinstance("hello", Iterable))
print(isinstance(123, Iterable))
print(isinstance([1, 2], Iterable))
print(isinstance({"a": 1}, Iterable))
```

**这行在干嘛？**

`Iterable` 表示「可迭代对象」。用 `isinstance(obj, Iterable)` 可以判断一个对象能不能被 `for...in` 遍历。

字符串、列表、字典都能遍历，所以是 `True`；整数 `123` 只是一个数字，不能逐个取元素，所以是 `False`。

**容易踩的坑**

可迭代对象不一定有下标。比如字典、集合、生成器都能遍历，但不能都用 `obj[0]`。所以「能 `for...in`」和「能按下标取」不是一回事。

## 🏃 跑一下试试

```bash
$ python iteration.py
=== 遍历列表 ===
小王
小李
小张

=== 遍历字典 ===
小王: 85
小李: 92
小张: 78
85
92
78
小王 => 85
小李 => 92
小张 => 78

=== 遍历字符串 ===
P y t h o n 

=== enumerate：同时拿下标和值 ===
0: 打开电脑
1: 写代码
2: 提交作业
第 1 步：打开电脑
第 2 步：写代码
第 3 步：提交作业

=== zip：并行遍历 ===
Alice: 85
Bob: 92
Charlie: 78
Alice English: 88
Bob English: 90

=== 判断是否可迭代 ===
True
False
True
True
```

## 💡 师兄的碎碎念

- Python 的 `for...in` 遍历的是**可迭代对象**，不只限于列表。
- 直接遍历字典拿到的是 key；想拿 value 用 `.values()`，想 key/value 一起拿用 `.items()`。
- 需要下标时优先用 `enumerate()`，不要上来就写 `range(len(...))`。
- `zip()` 很适合把两列数据配对，但它会按最短序列截断。
- Python 3.7 起，普通 `dict` 保持插入顺序；但写代码时最好别把「字典是排序结构」当成默认假设。

## 🎓 这一关的知识点清单

- **迭代**：从一个对象里逐个取元素，常见写法是 `for item in iterable`。
- **可迭代对象**：能被 `for...in` 遍历的对象，比如 list、tuple、str、dict、set、文件、生成器。
- **字典遍历**：`for key in d` 遍历 key，`d.values()` 遍历 value，`d.items()` 同时遍历 key/value。
- **enumerate()**：把可迭代对象变成 `(index, value)`，适合同时需要下标和值的场景。
- **zip()**：把多个可迭代对象按位置配对，遇到最短序列结束就停止。
- **Iterable 判断**：`isinstance(obj, Iterable)` 可以判断对象是否可迭代。

## ➡️ 下一关

迭代搞定！接下来学 Python 很有代表性的语法：列表生成式。它能把常见的「遍历 + 处理 + 收集结果」压成一行清爽代码 👉 [下一关：列表生成式 →](../17-list-comprehensions/)
