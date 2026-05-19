# 第 19 关：迭代器（师兄带你学 Python）

## 🎯 这一关你会学到

- Iterator 协议
- Iterable vs Iterator 的区别
- iter() 和 next() 函数
- for 循环的本质是 Iterator

## 🤔 先想一个问题

Iterable 像一本书，Iterator 像书签。iter() 给书夹上书签，next() 翻到下一页。StopIteration 就是翻到了最后一页。

## 📖 看代码

```python
# 迭代器（Iterator）

from collections.abc import Iterable, Iterator

# 可迭代对象 vs 迭代器
# 可迭代对象（Iterable）：能用 for 遍历的对象
# 迭代器（Iterator）：能用 next() 逐个取值的对象

# list、dict、str 是 Iterable，但不是 Iterator
print(isinstance([], Iterable))      # True
print(isinstance([], Iterator))      # False

# iter() 把 Iterable 转成 Iterator
it = iter([1, 2, 3])
print(isinstance(it, Iterator))     # True
print(next(it))    # 1
print(next(it))    # 2
print(next(it))    # 3
# print(next(it))  # StopIteration!

# for 循环的本质
# for x in [1, 2, 3]:  等价于：
it = iter([1, 2, 3])
while True:
    try:
        x = next(it)
        print(x, end=" ")
    except StopIteration:
        break
print()

# 生成器天生就是 Iterator
g = (x for x in range(3))
print(isinstance(g, Iterator))      # True

# 自定义迭代器类
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num, end=" ")
print()
```

## 🔍 师兄给你逐行拆

可迭代对象（Iterable）是能 for 遍历的，迭代器（Iterator）是能 next() 取值的。for 循环本质上就是先 iter() 拿到迭代器，然后不断 next() 直到 StopIteration。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python iterators.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **Iterable: 实现 __iter__()**
- **Iterator: 实现 __iter__() + __next__()**
- **iter() 把 Iterable 变成 Iterator**
- **for 循环 = iter() + next() + StopIteration**

## 🎓 这一关的知识点清单

- **Iterator 协议**
- **Iterable vs Iterator 的区别**
- **iter() 和 next() 函数**
- **for 循环的本质是 Iterator**

## ➡️ 下一关

本关搞定！接下来学 map/reduce 👉 [下一关：map/reduce →](../20-map-reduce/)
