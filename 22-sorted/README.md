# 第 22 关：sorted（师兄带你学 Python）

## 🎯 这一关你会学到

- sorted 排序函数
- key 参数自定义排序规则
- reverse=True 反向排序
- sorted vs list.sort

## 🤔 先想一个问题

sorted 像给快递排序——默认按编号排，但你也可以告诉快递员「按重量排」或「按目的地排」——key 就是排序标准。

## 📖 看代码

```python
# sorted：排序函数

# 基本排序
print(sorted([36, 5, -12, 9, -21]))       # [-21, -12, 5, 9, 36]

# 按绝对值排序：key 参数
print(sorted([36, 5, -12, 9, -21], key=abs))  # [5, 9, -12, -21, 36]

# 字符串排序（默认按 ASCII）
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# ['Credit', 'Zoo', 'about', 'bob']（大写在前）

# 忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# ['about', 'bob', 'Credit', 'Zoo']

# 反向排序
print(sorted([36, 5, -12, 9, -21], reverse=True))

# 对字典列表排序
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
]
result = sorted(students, key=lambda s: s['score'], reverse=True)
for s in result:
    print(f"{s['name']}: {s['score']}")

# sorted vs sort
# sorted() 返回新列表，原列表不变
# list.sort() 原地排序，返回 None
```

## 🔍 师兄给你逐行拆

sorted() 是通用排序函数，可以对任何可迭代对象排序。通过 key 参数你可以自定义排序规则——按绝对值排、忽略大小写排、按字典某个字段排。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python sorted.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **sorted(iterable, key=func, reverse=bool)**
- **key=abs 按绝对值**
- **key=str.lower 忽略大小写**
- **sorted 返回新列表，sort 原地排序**

## 🎓 这一关的知识点清单

- **sorted 排序函数**
- **key 参数自定义排序规则**
- **reverse=True 反向排序**
- **sorted vs list.sort**

## ➡️ 下一关

本关搞定！接下来学 返回函数(闭包) 👉 [下一关：返回函数(闭包) →](../23-closures/)
