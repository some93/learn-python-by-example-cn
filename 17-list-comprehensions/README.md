# 第 17 关：列表生成式（师兄带你学 Python）

## 🎯 这一关你会学到

- List Comprehension 语法
- 一行代码生成列表
- 带条件过滤的列表生成式
- 双层循环和 if...else 的位置

## 🤔 先想一个问题

你去超市买水果，一个一个挑太慢了。列表生成式就像你跟店员说：「所有苹果，每个削皮切块装盒」——一句话描述规则，店员批量操作。

## 📖 看代码

```python
# 列表生成式（List Comprehension）

# 基本用法：生成 1-10 的平方
squares = [x * x for x in range(1, 11)]
print(squares)

# 带条件过滤：只取偶数的平方
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)

# 双层循环
pairs = [m + n for m in 'ABC' for n in 'XYZ']
print(pairs)

# 遍历目录列表
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(f"当前目录文件数: {len(files)}")

# 使用两个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
result = [f"{k}={v}" for k, v in d.items()]
print(result)

# 全部转小写
L = ['Hello', 'World', 'IBM', 'Apple']
lower = [s.lower() for s in L]
print(lower)

# if...else 在列表生成式中的位置
# 前置 if...else（表达式位置）：没有 filter，每个元素都产出
result = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(result)   # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
```

## 🔍 师兄给你逐行拆

列表生成式是 Python 最具特色的语法之一——用一行代码生成列表，替代多行 for 循环。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python list-comprehensions.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **[expr for x in iterable] 基本语法**
- **[expr for x in iterable if cond] 条件过滤**
- **双层循环生成笛卡尔积**
- **if...else 作为表达式 vs 过滤器**

## 🎓 这一关的知识点清单

- **List Comprehension 语法**
- **一行代码生成列表**
- **带条件过滤的列表生成式**
- **双层循环和 if...else 的位置**

## ➡️ 下一关

本关搞定！接下来学 生成器 👉 [下一关：生成器 →](../18-generators/)
