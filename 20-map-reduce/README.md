# 第 20 关：map/reduce（师兄带你学 Python）

## 🎯 这一关你会学到

- 高阶函数 map 和 reduce
- map() 把函数作用到每个元素
- reduce() 把序列累积计算
- map + reduce 组合使用

## 🤔 先想一个问题

map 像流水线工人——每个产品经过他手时做同一个操作。reduce 像滚雪球——从第一个开始，每次把结果和下一个合并，越滚越大。

## 📖 看代码

```python
# map/reduce 高阶函数

# map：把函数作用到每个元素上
def f(x):
    return x * x

result = map(f, [1, 2, 3, 4, 5])
print(list(result))    # [1, 4, 9, 16, 25]

# 用 lambda 更简洁
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# 把整数列表转字符串列表
print(list(map(str, [1, 2, 3, 4, 5])))  # ['1', '2', '3', '4', '5']

# reduce：把序列累积计算
from functools import reduce

# 求和：1 + 2 + 3 + 4 + 5
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(total)   # 15

# 把 [1, 3, 5, 7] 变成 1357
num = reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7])
print(num)     # 1357

# 组合使用 map 和 reduce
# 把字符串 '13579' 变成整数 13579
def char_to_int(c):
    return ord(c) - ord('0')

result = reduce(lambda x, y: x * 10 + y, map(char_to_int, '13579'))
print(result)  # 13579
```

## 🔍 师兄给你逐行拆

map 把一个函数作用于序列的每个元素，reduce 把序列从左到右累积运算。这两个是函数式编程的基础积木。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python map-reduce.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **map(func, iterable) 返回 Iterator**
- **from functools import reduce**
- **reduce(func, iterable) 累积计算**
- **map + reduce 组合实现 str→int**

## 🎓 这一关的知识点清单

- **高阶函数 map 和 reduce**
- **map() 把函数作用到每个元素**
- **reduce() 把序列累积计算**
- **map + reduce 组合使用**

## ➡️ 下一关

本关搞定！接下来学 filter 👉 [下一关：filter →](../21-filter/)
