# 第 13 关：函数的参数

## 🎯 这一关你会学到

- 五种参数类型：位置参数、默认参数、可变参数 `*args`、关键字参数 `**kwargs`、命名关键字参数
- 默认参数的**可变对象陷阱**（面试高频题！）
- `*` 和 `**` 解包语法
- 参数组合的正确顺序

## 🤔 先想一个问题

你去奶茶店点单：「一杯珍珠奶茶」——这是最简单的「位置参数」。「一杯珍珠奶茶，不要糖」——「不要糖」是「默认参数的修改」（默认全糖）。「一杯珍珠奶茶，加椰果加布丁加仙草」——加料数量不定，这就是「可变参数」。Python 的参数系统就像奶茶店的点单系统，灵活到你想怎么点就怎么点。

## 📖 看代码

```python
# 1. 默认参数
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")            # Hello, Alice!
greet("Bob", "Hi")       # Hi, Bob!

# ⚠️ 默认参数陷阱：别用可变对象！
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print(bad_append(1))   # [1]
print(bad_append(2))   # [1, 2] ← 不是 [2]！

def good_append(item, lst=None):  # ✅ 正确写法
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# 2. 可变参数 *args
def calc_sum(*numbers):
    return sum(numbers)

print(calc_sum(1, 2, 3))       # 6
print(calc_sum(*[1, 2, 3, 4])) # 10（解包列表）

# 3. 关键字参数 **kwargs
def person(name, age, **kwargs):
    print(f"{name}, {age}, {kwargs}")

person("Alice", 25, city="Beijing", job="Engineer")  # Alice, 25, {'city': 'Beijing', 'job': 'Engineer'}

# 4. 命名关键字参数
def person2(name, age, *, city, job):
    print(f"{name}, {age}, {city}, {job}")

person2("Charlie", 35, city="Shanghai", job="Teacher")  # Charlie, 35, Shanghai, Teacher
```

## 🔍 师兄给你逐行拆

### 默认参数的可变对象陷阱 —— 必考题！

```python
def bad_append(item, lst=[]):
    lst.append(item)
    return lst
```

**为什么第二次调用结果不对？**

Python 的默认参数值在函数**定义时**就创建了，后续每次调用共享同一个对象。如果默认值是可变对象（list、dict），每次调用都在修改同一个对象！

**正确写法**：默认值用 `None`，函数体内判断后再创建新对象。这是 Python 面试的**超高频考点**。

---

### `*args` —— 接收任意数量的位置参数

```python
def calc_sum(*numbers):
    return sum(numbers)
```

`*numbers` 把所有传入的参数打包成一个 **tuple**。调用时用 `*list` 可以把列表解包成多个参数传入。

---

### `**kwargs` —— 接收任意数量的关键字参数

```python
def person(name, age, **kwargs):
    print(kwargs)   # {'city': 'Beijing', 'job': 'Engineer'}
```

`**kwargs` 把所有未匹配的关键字参数打包成一个 **dict**。这在写装饰器、封装 API 调用时特别有用。

---

### 参数组合顺序

五种参数在函数定义中的顺序必须是：

```
位置参数 → 默认参数 → *args → 命名关键字参数 → **kwargs
```

顺序错了会报 `SyntaxError`。

## 🏃 跑一下试试

```bash
$ python function-parameters.py
1024
Hello, Alice!
Hi, Bob!
[1]
[1, 2]
[1]
[2]
6
15
10
name: Alice, age: 25, other: {'city': 'Beijing', 'job': 'Engineer'}
Charlie, 35, Shanghai, Teacher
a=1, b=2, args=(3, 4), keyword_only=yes, kwargs={'extra': 'data'}
```

## 💡 师兄的碎碎念

- **永远不要用可变对象作为默认参数值**。用 `None` 代替，这是 Python 最重要的编码规范之一。
- `*args` 和 `**kwargs` 这两个名字是约定俗成的，你改成 `*params` 和 `**options` 也能用，但别人会不习惯。
- Go 的可变参数 `func f(args ...int)` 只支持同类型，Python 的 `*args` 可以混合任意类型。
- `*` 和 `**` 不仅在函数定义时有用，在函数调用时也能用来**解包**：`f(*[1,2,3])` 等价于 `f(1,2,3)`。

## 🎓 这一关的知识点清单

| 参数类型 | 语法 | 说明 |
|---------|------|------|
| 位置参数 | `def f(a, b)` | 最普通的参数，按位置传 |
| 默认参数 | `def f(a, b=0)` | 有默认值，可省略。**别用可变对象！** |
| 可变参数 | `def f(*args)` | 接收任意个位置参数，打包成 tuple |
| 关键字参数 | `def f(**kwargs)` | 接收任意个关键字参数，打包成 dict |
| 命名关键字 | `def f(*, city)` | `*` 后面的参数必须用名字传 |

## ➡️ 下一关

函数参数搞定了！接下来学一个特殊的函数——调用自己的函数，也就是递归 👉 [下一关：递归函数 →](../14-recursion/)
