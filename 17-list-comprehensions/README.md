# 第 17 关：列表生成式（师兄带你学 Python）

## 🎯 这一关你会学到

- 列表生成式的基本语法 `[expr for item in iterable]`
- 如何把「遍历 + 处理 + append」压缩成清晰的一行
- 带 `if` 的过滤写法
- `if...else` 表达式和过滤 `if` 的位置区别
- 双层循环、字典遍历、类型过滤等常见用法

## 🤔 先想一个问题

你去食堂打包 5 份套餐。普通写法像你每打一份就喊一句：「把第 1 份装进袋子，把第 2 份装进袋子……」

列表生成式像你直接对阿姨说：「把 1 到 5 号套餐都装进袋子。」规则说清楚，动作一口气完成。

在 Python 里，列表生成式就是专门解决这类问题的：**从一批数据里，按规则生成一个新列表**。

## 📖 看代码

```python
# 列表生成式（List Comprehension）


print("=== 普通 for 循环生成列表 ===")

# 先用普通循环写一遍，方便和列表生成式对比。
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)  # [1, 4, 9, 16, 25]


print("\n=== 列表生成式生成列表 ===")

# 列表生成式把“创建空列表、循环、append”压缩成一行。
squares = [x * x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


print("\n=== 带条件过滤 ===")

# if 放在 for 后面时，表示只保留满足条件的元素。
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]


print("\n=== if...else 表达式 ===")

# if...else 放在 for 前面时，表示对每个元素做二选一转换。
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']

# 也可以在保留元素数量不变的情况下改造每个值。
signed_numbers = [x if x % 2 == 0 else -x for x in range(1, 6)]
print(signed_numbers)  # [-1, 2, -3, 4, -5]


print("\n=== 双层循环 ===")

# 双层 for 的执行顺序和普通嵌套循环一致：左边的 for 是外层。
pairs = [letter + number for letter in "AB" for number in "12"]
print(pairs)  # ['A1', 'A2', 'B1', 'B2']

matrix = [[1, 2, 3], [4, 5, 6]]
# 常见用途：把二维列表压平成一维列表。
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]


print("\n=== 遍历字典和处理字符串 ===")

scores = {"小王": 85, "小李": 92, "小张": 78}
# 遍历字典时通常用 items() 同时拿到 key 和 value。
score_items = [f"{name}={score}" for name, score in scores.items()]
print(score_items)  # ['小王=85', '小李=92', '小张=78']

words = ["Hello", "World", 18, "Python", None]
# 先用 isinstance 过滤出字符串，再调用字符串方法，避免类型错误。
lower_words = [word.lower() for word in words if isinstance(word, str)]
print(lower_words)  # ['hello', 'world', 'python']
```

## 🔍 师兄给你逐行拆

### 从普通 `for` 循环开始看

```python
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)
```

**这行在干嘛？**

先准备一个空列表 `squares`，再遍历 `1` 到 `5`，每次把 `x * x` 追加进去。最后得到：

```python
[1, 4, 9, 16, 25]
```

**为什么先看这个？**

因为列表生成式不是魔法，它本质上就是把这种固定套路压短：

1. 准备一个空列表；
2. 遍历一批数据；
3. 对每个元素做处理；
4. 把处理结果放进新列表。

---

### `[x * x for x in range(1, 6)]` —— 列表生成式基本款

```python
squares = [x * x for x in range(1, 6)]
print(squares)
```

**这行在干嘛？**

这行和上面的普通 `for` 循环等价：对 `range(1, 6)` 里的每个 `x`，计算 `x * x`，收集成新列表。

可以按这个模板读：

```python
[要放进列表的结果 for 临时变量 in 可迭代对象]
```

**生活类比**

普通循环像你自己一个个装袋；列表生成式像你写一张加工单：「每个数字都平方后装袋」。结果一样，只是表达方式更直接。

**容易踩的坑**

列表生成式适合「生成新列表」。如果你只是想打印、写文件、发请求这种副作用操作，别为了炫技写：

```python
[print(x) for x in range(3)]
```

这会生成一个没用的列表 `[None, None, None]`。这种场景老老实实写 `for` 循环更清楚。

---

### 末尾 `if` —— 过滤元素

```python
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)
```

**这行在干嘛？**

只保留偶数，再对偶数求平方。`if x % 2 == 0` 放在最后，表示过滤条件：

```python
[4, 16, 36, 64, 100]
```

**为什么这么写？**

末尾的 `if` 只决定「这个元素要不要进列表」，不会给不满足条件的元素生成替代值。

等价普通写法是：

```python
result = []
for x in range(1, 11):
    if x % 2 == 0:
        result.append(x * x)
```

---

### 前置 `if...else` —— 每个元素都产出一个结果

```python
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(labels)
```

**这行在干嘛？**

这里不是过滤，而是给每个数字打标签。`1` 变成 `"奇数"`，`2` 变成 `"偶数"`，每个输入都会产出一个结果。

**重点区别**

这两个 `if` 位置不同，含义完全不同：

```python
# 过滤：只要偶数
[x for x in range(1, 6) if x % 2 == 0]

# 条件表达式：每个数都保留，只是结果不同
[x if x % 2 == 0 else -x for x in range(1, 6)]
```

前者结果是 `[2, 4]`，后者结果是 `[-1, 2, -3, 4, -5]`。

**容易踩的坑**

很多人会写出这种错误语法：

```python
# 错误：if...else 不能放在末尾过滤位置
[x for x in range(1, 6) if x % 2 == 0 else -x]
```

记住：**过滤 if 在后面，条件表达式 if...else 在前面**。

---

### 双层循环 —— 顺序和普通 `for` 一样

```python
pairs = [letter + number for letter in "AB" for number in "12"]
print(pairs)
```

**这行在干嘛？**

生成所有字母和数字的组合：

```python
['A1', 'A2', 'B1', 'B2']
```

它等价于：

```python
result = []
for letter in "AB":
    for number in "12":
        result.append(letter + number)
```

**为什么要讲顺序？**

列表生成式里的多个 `for`，顺序和普通嵌套循环从左到右一致。别倒着读。

**容易踩的坑**

双层还能接受，三层以上就很难读了。列表生成式不是越短越好，读起来费劲时就拆回普通循环。

---

### 拉平二维列表

```python
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)
```

**这行在干嘛？**

把二维列表拉平成一维列表：

```python
[1, 2, 3, 4, 5, 6]
```

读法还是按普通循环：

```python
for row in matrix:
    for num in row:
        ...
```

---

### 字典和混合列表也能处理

```python
scores = {"小王": 85, "小李": 92, "小张": 78}
score_items = [f"{name}={score}" for name, score in scores.items()]
print(score_items)

words = ["Hello", "World", 18, "Python", None]
lower_words = [word.lower() for word in words if isinstance(word, str)]
print(lower_words)
```

**这行在干嘛？**

第一段遍历字典的 `.items()`，把每个键值对格式化成字符串。

第二段先用 `isinstance(word, str)` 过滤掉不是字符串的元素，再调用 `.lower()` 转小写。

**为什么这么写？**

如果直接写：

```python
[word.lower() for word in words]
```

程序跑到 `18` 时会报错，因为整数没有 `.lower()` 方法。过滤条件可以让数据更干净。

## 🏃 跑一下试试

```bash
$ python list-comprehensions.py
=== 普通 for 循环生成列表 ===
[1, 4, 9, 16, 25]

=== 列表生成式生成列表 ===
[1, 4, 9, 16, 25]

=== 带条件过滤 ===
[4, 16, 36, 64, 100]

=== if...else 表达式 ===
['奇数', '偶数', '奇数', '偶数', '奇数']
[-1, 2, -3, 4, -5]

=== 双层循环 ===
['A1', 'A2', 'B1', 'B2']
[1, 2, 3, 4, 5, 6]

=== 遍历字典和处理字符串 ===
['小王=85', '小李=92', '小张=78']
['hello', 'world', 'python']
```

## 💡 师兄的碎碎念

- 列表生成式会**立刻生成完整列表**。如果数据量特别大，下一关的生成器更合适。
- 末尾 `if` 是过滤，前置 `if...else` 是条件表达式，二者位置不同、含义不同。
- 列表生成式适合简单转换；如果逻辑很复杂，普通 `for` 循环更可读。
- 不要用列表生成式做纯副作用操作，比如 `[print(x) for x in L]`。
- 字典、字符串、集合、生成器都能放进列表生成式里，只要它们是可迭代对象。

## 🎓 这一关的知识点清单

- **基本语法**：`[expr for item in iterable]`，对每个元素计算表达式并收集成列表。
- **条件过滤**：`[expr for item in iterable if condition]`，只保留满足条件的元素。
- **条件表达式**：`[a if condition else b for item in iterable]`，每个元素都会产生一个结果。
- **双层循环**：`[expr for a in A for b in B]`，顺序和普通嵌套 `for` 一样。
- **字典遍历**：可以结合 `.items()` 处理 key/value。
- **可读性原则**：简单转换用列表生成式，复杂逻辑用普通循环。

## ➡️ 下一关

列表生成式很爽，但它会一次性把结果全部生成出来。下一关我们学生成器：需要一个算一个，不把内存撑爆 👉 [下一关：生成器 →](../18-generators/)


