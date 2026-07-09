# 第 55 关：itertools（师兄带你学 Python）

## 🎯 这一关你会学到

- `count`、`cycle`、`repeat` 这类无限迭代器如何安全使用
- `islice` 如何截断惰性迭代器
- `chain` / `chain.from_iterable` 如何串联数据
- `groupby` 为什么要先排序
- `product`、`permutations`、`combinations` 的区别
- `accumulate`、`takewhile`、`dropwhile`、`compress`、`zip_longest`、`pairwise` 的常用场景

## 🤔 先想一个问题

你要处理一批数据：多个列表要串起来、学生要按班级分组、温度要计算相邻差值、两个序列长度不同还要配对。

这些都能手写循环，但 `itertools` 提供了很多“迭代器积木”。它们的共同特点是：**惰性计算，按需产出，不急着创建完整列表**。

## 📖 看代码

```python
# itertools 迭代器工具

import itertools
import operator


print("=== 无限迭代器要截断 ===")

# count 会无限计数，必须配合 islice 或 break 使用。
print(list(itertools.islice(itertools.count(10, 2), 5)))  # [10, 12, 14, 16, 18]

# cycle 会无限循环一个序列。
print(list(itertools.islice(itertools.cycle("ABC"), 8)))  # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']

# repeat 可以重复同一个值；第二个参数限制次数。
print(list(itertools.repeat("Hi", 3)))  # ['Hi', 'Hi', 'Hi']


print("\n=== chain 串联多个可迭代对象 ===")

print(list(itertools.chain("AB", "CD", "EF")))  # ['A', 'B', 'C', 'D', 'E', 'F']

groups = [["Alice", "Bob"], ["Charlie"], ["Diana", "Eric"]]

# chain.from_iterable 适合把“列表的列表”压平成一层。
print(list(itertools.chain.from_iterable(groups)))  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Eric']


print("\n=== groupby 相邻分组 ===")

records = [
    {"class": "二班", "name": "Bob"},
    {"class": "一班", "name": "Alice"},
    {"class": "一班", "name": "Charlie"},
    {"class": "二班", "name": "Diana"},
]

# groupby 只合并相邻元素，所以通常要先按同一个 key 排序。
records.sort(key=lambda item: item["class"])
for class_name, group in itertools.groupby(records, key=lambda item: item["class"]):  # 一班 ['Alice', 'Charlie'] / 二班 ['Bob', 'Diana']
    print(class_name, [item["name"] for item in group])


print("\n=== 排列组合 ===")

# product 是笛卡尔积，等价于多层 for 循环。
print(list(itertools.product("AB", "12")))  # [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

# permutations 是排列，顺序不同算不同结果。
print(list(itertools.permutations("ABC", 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations 是组合，顺序不同不重复计算。
print(list(itertools.combinations("ABC", 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]


print("\n=== accumulate 累积计算 ===")

sales = [100, -20, 50, -10]

# 默认做累加，也可以传入 operator.mul、max 等函数。
print(list(itertools.accumulate(sales)))  # [100, 80, 130, 120]
print(list(itertools.accumulate([3, 1, 4, 2], max)))  # [3, 3, 4, 4]
print(list(itertools.accumulate([1, 2, 3, 4], operator.mul)))  # [1, 2, 6, 24]


print("\n=== takewhile / dropwhile ===")

numbers = [1, 3, 5, 8, 9, 2]

# takewhile 遇到第一个不满足条件的元素就停止。
print(list(itertools.takewhile(lambda n: n < 8, numbers)))  # [1, 3, 5]

# dropwhile 跳过开头满足条件的元素，之后全部保留。
print(list(itertools.dropwhile(lambda n: n < 8, numbers)))  # [8, 9, 2]


print("\n=== compress / zip_longest / pairwise ===")

names = ["Alice", "Bob", "Charlie", "Diana"]
selected = [True, False, True, False]

# compress 用布尔选择器过滤数据。
print(list(itertools.compress(names, selected)))  # ['Alice', 'Charlie']

# zip_longest 会按最长序列对齐，缺失位置用 fillvalue 补。
print(list(itertools.zip_longest("ABC", [1, 2], fillvalue="-")))  # [('A', 1), ('B', 2), ('C', '-')]

# pairwise 适合计算相邻元素关系。
temperatures = [21, 23, 22, 25]
print(list(itertools.pairwise(temperatures)))  # [(21, 23), (23, 22), (22, 25)]
print([b - a for a, b in itertools.pairwise(temperatures)])  # [2, -1, 3]
```

## 🔍 师兄给你拆开讲

`count()`、`cycle()` 是无限迭代器，直接 `list(itertools.count())` 会一直跑下去。使用时要配合 `islice()`、`break` 或其他终止条件。

`chain()` 把多个可迭代对象接成一个迭代器，不需要先创建大列表。`chain.from_iterable()` 常用于把二维列表压平成一层。

`groupby()` 只把“相邻且 key 相同”的元素放在一组。它不是 SQL 的 `GROUP BY`，不会自动把分散在各处的相同 key 聚到一起，所以通常要先排序。

`product()` 是笛卡尔积，适合生成所有参数组合；`permutations()` 是排列，顺序不同算不同；`combinations()` 是组合，顺序不同不重复。

`takewhile()` 和 `dropwhile()` 都只关注开头连续满足条件的部分。一旦 `takewhile()` 遇到第一个不满足条件的元素就停止，不会继续往后找。

## 🏃 跑一下试试

```bash
cd 55-itertools
python itertools_demo.py
```

输出：

```text
=== 无限迭代器要截断 ===
[10, 12, 14, 16, 18]
['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
['Hi', 'Hi', 'Hi']

=== chain 串联多个可迭代对象 ===
['A', 'B', 'C', 'D', 'E', 'F']
['Alice', 'Bob', 'Charlie', 'Diana', 'Eric']

=== groupby 相邻分组 ===
一班 ['Alice', 'Charlie']
二班 ['Bob', 'Diana']

=== 排列组合 ===
[('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
[('A', 'B'), ('A', 'C'), ('B', 'C')]

=== accumulate 累积计算 ===
[100, 80, 130, 120]
[3, 3, 4, 4]
[1, 2, 6, 24]

=== takewhile / dropwhile ===
[1, 3, 5]
[8, 9, 2]

=== compress / zip_longest / pairwise ===
['Alice', 'Charlie']
[('A', 1), ('B', 2), ('C', '-')]
[(21, 23), (23, 22), (22, 25)]
[2, -1, 3]
```

## 💡 师兄的提醒

`itertools` 的优势是省内存、可组合，但可读性也要控制。三四个迭代器函数嵌在一起时，可能不如一个清楚的 `for` 循环。

看到无限迭代器先问自己：它在哪里停？看到 `groupby` 先问自己：数据是否已经按同一个 key 排好序？

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `count(start, step)` | 无限计数器 |
| `cycle(iterable)` | 无限循环迭代 |
| `repeat(value, n)` | 重复指定值 |
| `islice(iterable, n)` | 截断或切片迭代器 |
| `chain()` | 串联多个可迭代对象 |
| `chain.from_iterable()` | 展平一层嵌套 |
| `groupby()` | 按相邻 key 分组 |
| `product()` | 笛卡尔积 |
| `permutations()` | 排列 |
| `combinations()` | 组合 |
| `accumulate()` | 累积计算 |
| `takewhile()` / `dropwhile()` | 按开头连续条件截取或丢弃 |
| `compress()` | 用布尔选择器过滤 |
| `zip_longest()` | 按最长序列配对 |
| `pairwise()` | 生成相邻元素对 |

## ➡️ 下一关

下一关：[contextlib](../56-contextlib/README.md)。
