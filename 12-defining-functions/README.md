# 第 12 关：定义函数

## 🎯 这一关你会学到

- 用 `def` 关键字定义函数
- 函数的参数和返回值
- `return` 语句，没有 return 时返回 `None`
- `pass` 占位符
- 返回多个值（其实是返回 tuple）

## 🤔 先想一个问题

上一关我们学了怎么用别人写好的函数。但总有一天，你需要**自己造工具**。就像奶茶店标配的封杯机你能直接用，但如果你想发明一种「自动加珍珠机」，得自己设计。`def` 就是 Python 的「工具设计台」——给你的逻辑起个名字，以后随时调用。

## 📖 看代码

```python
# 用 def 定义函数
def greet(name):
    print(f"Hello, {name}!")

greet("World")  # Hello, World!

# 带返回值
def add(a, b):
    return a + b

print(f"1 + 2 = {add(1, 2)}")  # 1 + 2 = 3

# 空函数：pass 占位
def do_nothing():
    pass

print(do_nothing())   # None

# 返回多个值（返回的是 tuple）
def move(x, y, step):
    return x + step, y + step

x, y = move(100, 200, 50)
print(f"新坐标: ({x}, {y})")  # 新坐标: (150, 250)

# 参数类型检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误')
    return x if x >= 0 else -x

print(my_abs(-9))  # 9
```

## 🔍 师兄给你逐行拆

### `def` —— 定义函数的关键字

```python
def greet(name):
    print(f"Hello, {name}!")
```

**和 Go 的对比**

Go 用 `func`，Python 用 `def`（define 的缩写）。Go 要写参数类型和返回值类型，Python 都不需要——动态类型语言的自由。但代价是你没法在编译期发现类型错误。

---

### 返回多个值 —— 其实是 tuple

```python
def move(x, y, step):
    return x + step, y + step

x, y = move(100, 200, 50)
```

Python 函数可以 `return a, b, c`，看起来返回了多个值，其实返回的是一个 **tuple** `(a, b, c)`。接收端用解包赋值就能拆开。Go 也支持多返回值（`func f() (int, error)`），但 Go 是语法层面的真正多返回值，Python 是 tuple 的语法糖。

---

### `pass` —— 什么都不做的占位符

```python
def do_nothing():
    pass
```

Python 的函数体不能为空（不像 Go 可以 `func f() {}`），所以需要 `pass` 当占位符。先把函数骨架写好，后续再填充逻辑。`if`、`for`、`class` 里也能用 `pass`。

## 🏃 跑一下试试

```bash
$ python defining-functions.py
Hello, World!
1 + 2 = 3
None
新坐标: (150, 250)
9
3.14
1024
计算 x 的 n 次方
```

## 💡 师兄的碎碎念

- 函数没有 `return` 或 `return` 后面不跟值时，返回 `None`。
- Python 函数是**一等公民**：可以赋值给变量、传给其他函数、从函数返回。这和 Go 一样。
- 函数定义的**位置不重要**（只要在调用之前已经被 Python 解释器执行过就行），但按惯例把函数定义写在文件上面，调用写在下面。
- 可以用 `"""..."""` 在函数体第一行写文档字符串（docstring），用 `help(func)` 或 `func.__doc__` 查看。

## 🎓 这一关的知识点清单

- **def**：定义函数的关键字，语法 `def name(params): body`。
- **return**：返回值。没写 return 返回 `None`。
- **pass**：空操作占位符，函数/类/条件体为空时必须用。
- **多返回值**：`return a, b` 实际返回 tuple，接收端用解包赋值。
- **isinstance()**：在函数内做参数类型检查的推荐方式。

## ➡️ 下一关

函数定义搞定了！但 Python 的函数参数系统超级灵活——默认参数、可变参数、关键字参数，玩法多到让你眼花缭乱 👉 [下一关：函数的参数 →](../13-function-parameters/)
