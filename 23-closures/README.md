# 第 23 关：返回函数（闭包）（师兄带你学 Python）

## 🎯 这一关你会学到

- 闭包 Closure
- 函数作为返回值
- 闭包的循环变量陷阱（面试必考！）
- nonlocal 关键字修改外层变量

## 🤔 先想一个问题

闭包就像搬出父母家后你带走了家里的钥匙。你已经不住那里了（外层函数执行完了），但你随时可以回去开门（访问外层变量）。

## 📖 看代码

```python
# 返回函数（闭包）

# 函数作为返回值
def lazy_sum(*args):
    def calc():
        total = 0
        for n in args:
            total += n
        return total
    return calc       # 返回的是函数，不是结果

f = lazy_sum(1, 3, 5, 7, 9)
print(f)              # <function lazy_sum.<locals>.calc at 0x...>
print(f())            # 25（调用时才真正计算）

# 每次调用返回一个新的函数
f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
print(f1 == f2)       # False（不同的函数对象）

# 闭包陷阱：循环变量被捕获
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())   # 9 9 9（全是9！不是1 4 9）

# 修复：用参数绑定当前值
def count_fixed():
    fs = []
    for i in range(1, 4):
        def f(i=i):       # 用默认参数绑定
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count_fixed()
print(f1(), f2(), f3())   # 1 4 9（正确！）

# nonlocal：在闭包中修改外层变量
def counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c = counter()
print(c())   # 1
print(c())   # 2
print(c())   # 3
```

## 🔍 师兄给你逐行拆

闭包是指内层函数「记住」了外层函数的变量——即使外层函数已经执行完毕，内层函数仍然可以访问那些变量。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python closures.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **函数可以作为返回值**
- **闭包捕获外层变量（引用而非值！）**
- **循环变量陷阱：用默认参数 i=i 修复**
- **nonlocal 声明修改外层非全局变量**

## 🎓 这一关的知识点清单

- **闭包 Closure**
- **函数作为返回值**
- **闭包的循环变量陷阱（面试必考！）**
- **nonlocal 关键字修改外层变量**

## ➡️ 下一关

本关搞定！接下来学 匿名函数 👉 [下一关：匿名函数 →](../24-lambda/)
