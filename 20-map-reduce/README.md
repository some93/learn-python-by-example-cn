# 第 20 关：map/reduce（师兄带你学 Python）

## 🎯 这一关你会学到

- `map()`：把一个函数作用到可迭代对象的每个元素上
- `map()` 返回惰性迭代器，不是列表
- `reduce()`：把一串值从左到右累积合并成一个值
- `reduce()` 的初始值参数，以及空序列坑
- 什么时候用 `map/reduce`，什么时候列表生成式更清楚

## 🤔 先想一个问题

`map` 像流水线工人：每个包裹经过他手里，都贴同一种标签。

`reduce` 像滚雪球：先拿两个雪球合成一个，再把结果和下一个合成一个，最后滚成一个大雪球。

前者是「逐个加工」，后者是「累积合并」。

## 📖 看代码

```python
# map/reduce 高阶函数

from functools import reduce


print("=== map：逐个加工 ===")


def square(x):
    return x * x


# map 返回的是惰性迭代器，不会立刻生成完整列表。
mapped = map(square, [1, 2, 3, 4, 5])
print(type(mapped).__name__)
print(list(mapped))
# map 结果消费完之后，再转 list 就没有内容了。
print(list(mapped))


print("\n=== map 和列表生成式对比 ===")

numbers = [1, 2, 3, 4, 5]
# 这两种写法结果相同；列表生成式通常更直观。
print(list(map(square, numbers)))
print([square(x) for x in numbers])


print("\n=== map 的常见用法 ===")

# 把一组数字统一转换成字符串。
print(list(map(str, [1, 2, 3, 4, 5])))

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
# map 可以同时遍历多个序列，按位置把参数传给函数。
records = map(lambda name, score: f"{name}: {score}", names, scores)
print(list(records))


print("\n=== reduce：累积合并 ===")

# reduce 会把上一次计算结果继续和下一个元素合并。
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(total)

product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)


print("\n=== reduce 的初始值 ===")

# 空序列必须提供初始值，否则 reduce 不知道从哪里开始。
print(reduce(lambda x, y: x + y, [], 0))
try:
    print(reduce(lambda x, y: x + y, []))
except TypeError as error:
    print(type(error).__name__)


print("\n=== map + reduce 组合 ===")


def char_to_int(ch):
    return ord(ch) - ord("0")


def digits_to_int(text):
    # 先把字符映射成数字，再用 reduce 拼成整数。
    return reduce(lambda x, y: x * 10 + y, map(char_to_int, text))


print(digits_to_int("13579"))
```

## 🔍 师兄给你逐行拆

### `map(square, numbers)` —— 逐个加工

```python
def square(x):
    return x * x


mapped = map(square, [1, 2, 3, 4, 5])
print(type(mapped).__name__)
print(list(mapped))
print(list(mapped))
```

**这行在干嘛？**

`map(square, [1, 2, 3, 4, 5])` 会把 `square()` 作用到每个元素上：

```python
1 -> 1
2 -> 4
3 -> 9
4 -> 16
5 -> 25
```

**为什么要 `list(mapped)`？**

在 Python 3 里，`map()` 返回的是一个惰性迭代器，不是列表。你想一次性看结果，就要用 `list()` 把它取出来。

第一次 `list(mapped)` 得到 `[1, 4, 9, 16, 25]`，第二次再取就是 `[]`，因为这个迭代器已经被消费完了。

---

### `map` 和列表生成式怎么选？

```python
numbers = [1, 2, 3, 4, 5]
print(list(map(square, numbers)))
print([square(x) for x in numbers])
```

**这行在干嘛？**

这两行结果一样，都是把每个数字平方：

```python
[1, 4, 9, 16, 25]
```

**为什么 Python 里很多人更爱列表生成式？**

因为列表生成式直接把“遍历谁、生成什么”写在一处，读起来更自然：

```python
[square(x) for x in numbers]
```

`map()` 在这几类场景更合适：

- 直接套用现成函数：`map(str, numbers)`；
- 多个序列并行处理；
- 和函数式风格的代码搭配；
- 想保留惰性迭代器，不立刻生成列表。

---

### `map()` 可以接多个可迭代对象

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
records = map(lambda name, score: f"{name}: {score}", names, scores)
print(list(records))
```

**这行在干嘛？**

`map()` 不只能处理一个序列，也能同时处理多个序列。这里每次从 `names` 和 `scores` 各取一个元素，传给 `lambda name, score`。

结果是：

```python
['Alice: 85', 'Bob: 92', 'Charlie: 78']
```

**容易踩的坑**

多个可迭代对象长度不一样时，`map()` 和 `zip()` 一样，会在最短的那个用完时停止。

---

### `reduce()` —— 把一串值合成一个值

```python
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(total)

product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)
```

**这行在干嘛？**

`reduce()` 会从左到右累积计算。

求和这行可以理解成：

```python
((((1 + 2) + 3) + 4) + 5)
```

乘积这行可以理解成：

```python
((((1 * 2) * 3) * 4) * 5)
```

**为什么要从 `functools` 导入？**

Python 3 把 `reduce()` 放进了 `functools` 模块，所以要先写：

```python
from functools import reduce
```

---

### 初始值参数 —— 空列表不翻车

```python
print(reduce(lambda x, y: x + y, [], 0))
try:
    print(reduce(lambda x, y: x + y, []))
except TypeError as error:
    print(type(error).__name__)
```

**这行在干嘛？**

第三个参数 `0` 是初始值。空列表没有元素可合并，但有初始值，所以结果是 `0`。

如果没有初始值，又传入空列表，`reduce()` 不知道从哪里开始，就会抛 `TypeError`。

**容易踩的坑**

只要输入可能为空，就认真考虑给 `reduce()` 一个初始值。比如求和用 `0`，求乘积用 `1`。

不过在真实项目里，求和通常直接用内置函数：

```python
sum(numbers)
```

比 `reduce(lambda x, y: x + y, numbers)` 更清楚。

---

### `map + reduce`：把字符串数字转成整数

```python
def char_to_int(ch):
    return ord(ch) - ord("0")


def digits_to_int(text):
    return reduce(lambda x, y: x * 10 + y, map(char_to_int, text))


print(digits_to_int("13579"))
```

**这行在干嘛？**

先用 `map(char_to_int, text)` 把每个字符转成数字：

```python
"1", "3", "5", "7", "9" -> 1, 3, 5, 7, 9
```

再用 `reduce()` 一步步合并：

```python
1
1 * 10 + 3 = 13
13 * 10 + 5 = 135
135 * 10 + 7 = 1357
1357 * 10 + 9 = 13579
```

**现实提醒**

这个例子是为了理解 `map/reduce`。真实写代码时，字符串转整数当然直接用：

```python
int("13579")
```

别为了函数式而函数式。

## 🏃 跑一下试试

```bash
$ python map-reduce.py
=== map：逐个加工 ===
map
[1, 4, 9, 16, 25]
[]

=== map 和列表生成式对比 ===
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25]

=== map 的常见用法 ===
['1', '2', '3', '4', '5']
['Alice: 85', 'Bob: 92', 'Charlie: 78']

=== reduce：累积合并 ===
15
120

=== reduce 的初始值 ===
0
TypeError

=== map + reduce 组合 ===
13579
```

## 💡 师兄的碎碎念

- `map(func, iterable)` 返回迭代器，想看完整结果通常要 `list()`。
- `map()` 适合把现成函数批量作用到数据上，比如 `map(str, nums)`。
- `reduce()` 把多个值合成一个值，常见场景是累积、组合、折叠。
- `reduce()` 处理可能为空的数据时，最好传初始值。
- 能用 `sum()`、`max()`、`min()` 或列表生成式清楚表达时，就别硬上 `reduce()`。

## 🎓 这一关的知识点清单

- **map()**：逐个加工可迭代对象里的元素，返回惰性迭代器。
- **多序列 map**：`map(func, a, b)` 会同时从多个可迭代对象取值传给函数。
- **reduce()**：从左到右把一串值累积合并为一个值。
- **初始值**：`reduce(func, iterable, initial)` 可以指定起点，避免空序列报错。
- **函数式风格取舍**：语法短不等于可读性高，能用更直观写法时优先直观写法。

## ➡️ 下一关

`map()` 负责逐个加工，下一关的 `filter()` 负责按条件筛选。也就是：流水线后面再加一道安检门 👉 [下一关：filter →](../21-filter/)


