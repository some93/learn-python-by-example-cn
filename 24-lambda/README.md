# 第 24 关：匿名函数（师兄带你学 Python）

## 🎯 这一关你会学到

- `lambda 参数: 表达式` 的基本语法
- lambda 和 `def` 定义函数的等价关系
- lambda 在 `sorted()`、`map()`、`filter()` 中的常见用法
- lambda 只能写一个表达式，不能写多条语句
- 什么时候用 lambda，什么时候应该老实写 `def`

## 🤔 先想一个问题

lambda 像便利店的一次性筷子。吃一顿盒饭，用它刚刚好；但你要开饭店，就别拿一次性筷子当长期餐具了。

代码也一样。逻辑很短、只用一次，lambda 很方便；逻辑稍微复杂、需要复用或调试，就应该写 `def`。

## 📖 看代码

```python
# 匿名函数（lambda）


print("=== lambda 基本语法 ===")

# lambda 适合写很短的匿名函数。
square = lambda x: x * x
print(square(5))       # 25
print(square.__name__) # <lambda>


def square_def(x):
    # 逻辑稍微复杂一点时，用 def 更清楚，也更方便调试。
    return x * x


print(square_def(5))       # 25
print(square_def.__name__) # square_def


print("\n=== lambda 用在 sorted 的 key 参数 ===")

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]

# sorted 的 key 参数常见写法：用 lambda 指定排序依据。
by_score = sorted(students, key=lambda student: student["score"], reverse=True)
print([student["name"] for student in by_score])  # ['Bob', 'Alice', 'Charlie']

pairs = [(1, "one"), (3, "three"), (2, "two")]
# 同一组数据可以按不同字段排序。
print(sorted(pairs, key=lambda pair: pair[0]))      # [(1, 'one'), (2, 'two'), (3, 'three')]
print(sorted(pairs, key=lambda pair: len(pair[1]))) # [(1, 'one'), (2, 'two'), (3, 'three')]


print("\n=== lambda 配合 map/filter ===")

# lambda 经常和高阶函数一起出现，但别为了简短牺牲可读性。
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))     # [1, 4, 9, 16, 25]
print(list(filter(lambda x: x % 2 == 1, range(1, 11)))) # [1, 3, 5, 7, 9]


print("\n=== lambda 作为返回值 ===")


def make_adder(n):
    # 返回的 lambda 会记住外层的 n，这也是闭包。
    return lambda x: x + n


add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))   # 8
print(add10(3))  # 13


print("\n=== 复杂逻辑用 def 更清楚 ===")


def classify_score(score):
    # 多分支逻辑不适合写成 lambda。
    if score >= 90:
        return "优秀"
    if score >= 60:
        return "及格"
    return "不及格"


print(classify_score(95)) # 优秀
print(classify_score(72)) # 及格
print(classify_score(50)) # 不及格
```

## 🔍 师兄给你逐行拆

### `lambda x: x * x` —— 一个没有正式名字的小函数

```python
square = lambda x: x * x
print(square(5))
print(square.__name__)
```

**这行在干嘛？**

`lambda x: x * x` 定义了一个函数：接收 `x`，返回 `x * x`。

它和下面这个函数逻辑等价：

```python
def square_def(x):
    return x * x
```

**为什么说 lambda 是匿名函数？**

lambda 创建出来的函数默认名字是 `<lambda>`，不像 `def square_def` 有一个清楚的函数名。

这也是为什么不推荐经常写：

```python
square = lambda x: x * x
```

如果都已经要赋值给变量了，多数时候直接写 `def square(x): ...` 更清楚，调试输出也更友好。

---

### lambda 最适合放在 `key=` 里

```python
by_score = sorted(students, key=lambda student: student["score"], reverse=True)
print([student["name"] for student in by_score])
```

**这行在干嘛？**

`lambda student: student["score"]` 是一个临时排序规则：给一个学生字典，取出它的 `score`。

`sorted()` 用这个分数排序，于是学生按成绩从高到低排列。

**为什么这里适合用 lambda？**

因为这个函数逻辑很短，而且只在这一行使用。专门写一个函数：

```python
def get_score(student):
    return student["score"]
```

也可以，但略显啰嗦。

---

### 对元组排序

```python
pairs = [(1, "one"), (3, "three"), (2, "two")]
print(sorted(pairs, key=lambda pair: pair[0]))
print(sorted(pairs, key=lambda pair: len(pair[1])))
```

**这行在干嘛？**

第一行按元组第一个元素排序，得到：

```python
[(1, 'one'), (2, 'two'), (3, 'three')]
```

第二行按英文单词长度排序，得到：

```python
[(1, 'one'), (2, 'two'), (3, 'three')]
```

这两个结果刚好一样，但排序标准不同。一个看数字，一个看字符串长度。

---

### lambda 配合 `map()` 和 `filter()`

```python
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x % 2 == 1, range(1, 11))))
```

**这行在干嘛？**

第一行把每个数字平方：

```python
[1, 4, 9, 16, 25]
```

第二行保留奇数：

```python
[1, 3, 5, 7, 9]
```

**什么时候不建议这么写？**

如果 lambda 里面逻辑开始变长、嵌套三元表达式、读起来像密码，那就别硬写。函数式写法不是越短越高级，读得懂才重要。

---

### lambda 作为返回值：闭包的简洁写法

```python
def make_adder(n):
    return lambda x: x + n


add5 = make_adder(5)
add10 = make_adder(10)
```

**这行在干嘛？**

`make_adder(5)` 返回一个函数，这个函数会把传入的数字加 5。`make_adder(10)` 返回另一个函数，把传入的数字加 10。

这其实就是上一关闭包的简写：lambda 也能捕获外层变量 `n`。

---

### 复杂逻辑用 `def`

```python
def classify_score(score):
    if score >= 90:
        return "优秀"
    if score >= 60:
        return "及格"
    return "不及格"
```

**这行在干嘛？**

这是一个成绩分类函数。它有多条语句、多个判断分支，所以应该用 `def`。

**为什么 lambda 写不了？**

lambda 只能写一个表达式，不能写多条语句，不能写普通的 `if` 代码块，也不能写 `return`。

你可以把简单条件写成条件表达式：

```python
lambda score: "及格" if score >= 60 else "不及格"
```

但如果逻辑继续变复杂，就别硬塞了。

## 🏃 跑一下试试

```bash
$ python lambda.py
=== lambda 基本语法 ===
25
<lambda>
25
square_def

=== lambda 用在 sorted 的 key 参数 ===
['Bob', 'Alice', 'Charlie']
[(1, 'one'), (2, 'two'), (3, 'three')]
[(1, 'one'), (2, 'two'), (3, 'three')]

=== lambda 配合 map/filter ===
[1, 4, 9, 16, 25]
[1, 3, 5, 7, 9]

=== lambda 作为返回值 ===
8
13

=== 复杂逻辑用 def 更清楚 ===
优秀
及格
不及格
```

## 💡 师兄的碎碎念

- lambda 的格式是 `lambda 参数: 表达式`，冒号右边只能有一个表达式。
- lambda 没有正式函数名，调试时通常显示 `<lambda>`。
- 如果一个 lambda 需要赋值给变量并反复使用，优先考虑改成 `def`。
- `sorted(key=...)` 是 lambda 最常见、最自然的使用场景。
- lambda 也能形成闭包，捕获外层变量。

## 🎓 这一关的知识点清单

- **lambda 表达式**：创建短小的匿名函数。
- **语法**：`lambda 参数1, 参数2: 返回表达式`。
- **匿名函数名**：lambda 默认名字是 `<lambda>`，不像 `def` 有清晰函数名。
- **常见用途**：作为 `sorted()` 的 `key`，或配合 `map()`、`filter()`。
- **表达式限制**：lambda 不能包含多条语句、普通 `if` 代码块或 `return`。
- **选择原则**：短小一次性逻辑用 lambda，复杂或复用逻辑用 `def`。

## ➡️ 下一关

lambda 是小函数，装饰器则是“改造函数的函数”。下一关看 `@decorator` 背后到底发生了什么 👉 [下一关：装饰器 →](../25-decorators/)


