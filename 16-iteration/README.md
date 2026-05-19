# 第 16 关：迭代（师兄带你学 Python）

## 🎯 这一关你会学到

- for...in 遍历一切
- 遍历 dict、字符串等各种对象
- enumerate() 和 zip() 的用法
- 判断可迭代对象

## 🤔 先想一个问题

你搬进新宿舍，要逐个认识室友。list 像名单——按顺序念名字。dict 像通讯录——翻的是人名（key），看到的是号码（value）。字符串像一串糖葫芦——一个字符一个字符地吃。Python 的 for...in 就是这个「逐个过」的动作。

## 📖 看代码

```python
# 迭代

# 遍历 list
for item in [1, 2, 3]:
    print(item)

# 遍历 dict（默认遍历 key）
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(f"{key}: {d[key]}")

# 遍历 value
for value in d.values():
    print(value)

# 同时遍历 key 和 value
for k, v in d.items():
    print(f"{k} => {v}")

# 遍历字符串
for ch in 'Python':
    print(ch, end=" ")
print()

# enumerate：同时获取索引和值
for i, value in enumerate(['A', 'B', 'C']):
    print(f"{i}: {value}")

# 同时遍历多个序列：zip
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 判断对象是否可迭代
from collections.abc import Iterable
print(isinstance('hello', Iterable))   # True
print(isinstance(123, Iterable))       # False
print(isinstance([1, 2], Iterable))    # True
```

## 🔍 师兄给你逐行拆

Python 的 for...in 能遍历一切可迭代对象——列表、字典、字符串、文件——只要对象实现了迭代协议。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python iteration.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **for...in 遍历列表/字典/字符串**
- **enumerate() 获取索引+值**
- **zip() 并行遍历多个序列**
- **Iterable 判断: isinstance(obj, Iterable)**

## 🎓 这一关的知识点清单

- **for...in 遍历一切**
- **遍历 dict、字符串等各种对象**
- **enumerate() 和 zip() 的用法**
- **判断可迭代对象**

## ➡️ 下一关

本关搞定！接下来学 列表生成式 👉 [下一关：列表生成式 →](../17-list-comprehensions/)
