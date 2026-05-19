# 第 55 关：itertools（师兄带你学 Python）

## 🎯 这一关你会学到

- 使用无限迭代器：`count`、`cycle`、`repeat`
- 使用组合迭代器：`chain`、`groupby`
- 使用排列组合：`product`、`permutations`、`combinations`
- 用 `islice` 切片无限迭代器

## 🤔 先想一个问题

你想生成所有可能的密码组合、把多个列表串起来、或者对数据分组统计。手写循环很麻烦，`itertools` 提供了一堆现成的「迭代器积木」，拼起来就能用。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# itertools

import itertools

# count：无限计数器
for i in itertools.count(1):
    if i > 5:
        break
    print(i, end=' ')    # 1 2 3 4 5
print()

# cycle：无限循环
n = 0
for c in itertools.cycle('ABC'):
    if n >= 6:
        break
    print(c, end=' ')    # A B C A B C
    n += 1
print()

# repeat：重复
for x in itertools.repeat('Hi', 3):
    print(x, end=' ')    # Hi Hi Hi
print()

# chain：串联多个迭代器
for x in itertools.chain('AB', 'CD', 'EF'):
    print(x, end=' ')    # A B C D E F
print()

# groupby：相邻相同元素分组
for key, group in itertools.groupby('AAABBBCCA'):
    print(f"{key}: {list(group)}")
# A: ['A', 'A', 'A']
# B: ['B', 'B', 'B']
# C: ['C', 'C']
# A: ['A']

# 忽略大小写分组
for key, group in itertools.groupby('AaaBBbcCc', lambda c: c.upper()):
    print(f"{key}: {list(group)}")

# product：笛卡尔积
print(list(itertools.product('AB', '12')))
# [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

# permutations：排列
print(list(itertools.permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations：组合
print(list(itertools.combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# islice：切片无限迭代器
print(list(itertools.islice(itertools.count(10), 5)))
# [10, 11, 12, 13, 14]

# accumulate：累积
print(list(itertools.accumulate([1, 2, 3, 4, 5])))
# [1, 3, 6, 10, 15]
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `count/cycle/repeat` 是无限迭代器，记得用 `islice` 或 `break` 截断
- `chain` 把多个迭代器串成一个，比 `list1 + list2` 更省内存
- `groupby` 要求数据先排序！相邻相同的才会分在一组
- `product` 是笛卡尔积，等价于多层 for 循环
- `combinations` 是组合（不考虑顺序），`permutations` 是排列（考虑顺序）

## 🏃 跑一下试试

```bash
cd 55-itertools
python itertools_demo.py
```

## 💡 师兄的碎碎念

- `count/cycle/repeat` 是无限迭代器，记得用 `islice` 或 `break` 截断
- `chain` 把多个迭代器串成一个，比 `list1 + list2` 更省内存
- `groupby` 要求数据先排序！相邻相同的才会分在一组
- `product` 是笛卡尔积，等价于多层 for 循环
- `combinations` 是组合（不考虑顺序），`permutations` 是排列（考虑顺序）

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `count(start)` | 从 start 开始的无限计数 |
| `cycle(iterable)` | 无限循环迭代 |
| `chain(a, b, c)` | 串联多个迭代器 |
| `groupby(iterable, key)` | 相邻元素分组 |
| `product(a, b)` | 笛卡尔积 |
| `combinations/permutations` | 组合/排列 |

## ➡️ 下一关

下一关我们学习 [contextlib](../56-contextlib/README.md)，继续加油！
