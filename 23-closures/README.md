# 第 23 关：返回函数（闭包）（师兄带你学 Python）

## 🎯 这一关你会学到

- 函数可以作为返回值
- 什么是闭包：内层函数记住外层变量
- 闭包捕获的是变量引用，不是“当时的值”
- 循环变量陷阱，以及用默认参数绑定当前值
- `nonlocal` 如何修改外层函数变量

## 🤔 先想一个问题

你搬出宿舍了，但你还带着宿舍钥匙。人已经离开，钥匙还在，你仍然能回去打开那扇门。

闭包也是类似的感觉：外层函数已经执行结束了，但内层函数还带着外层变量的“钥匙”，之后调用它时，依然能访问那些变量。

## 📖 看代码

```python
# 返回函数（闭包）


print("=== 函数可以作为返回值 ===")


def lazy_sum(*args):
    # calc 引用了外层函数的 args，这就形成了闭包。
    def calc():
        total = 0
        for n in args:
            total += n
        return total

    return calc


f = lazy_sum(1, 3, 5, 7, 9)
# 此时还没有真正求和，f 是一个等待调用的函数。
print(type(f).__name__)
print(f.__name__)
print(f())
# __closure__ 可以看到函数是否捕获了外层变量。
print(f.__closure__ is not None)
print(len(f.__closure__))


print("\n=== 每次调用都会返回新函数 ===")

f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
# 参数一样，也会生成两个不同的函数对象。
print(f1 == f2)
print(f1())
print(f2())


print("\n=== 循环变量陷阱 ===")


def count_bad():
    funcs = []
    for i in range(1, 4):
        def square():
            # 这里的 i 是外层变量，调用时已经变成循环结束后的 3。
            return i * i

        funcs.append(square)
    return funcs


print([func() for func in count_bad()])


print("\n=== 修复循环变量陷阱 ===")


def count_fixed():
    funcs = []
    for i in range(1, 4):
        def square(i=i):
            # 用默认参数把当前 i 的值固定下来。
            return i * i

        funcs.append(square)
    return funcs


print([func() for func in count_fixed()])


print("\n=== nonlocal 修改外层变量 ===")


def counter(start=0):
    n = start

    def inc(step=1):
        # nonlocal 表示修改外层函数里的 n，而不是新建局部变量。
        nonlocal n
        n += step
        return n

    return inc


c = counter()
print(c())
print(c())
print(c(10))

c2 = counter(100)
print(c2())
```

## 🔍 师兄给你逐行拆

### `return calc` —— 返回函数本身，不是返回结果

```python
def lazy_sum(*args):
    def calc():
        total = 0
        for n in args:
            total += n
        return total

    return calc
```

**这行在干嘛？**

`lazy_sum()` 内部定义了一个函数 `calc()`，但最后返回的是 `calc` 本身，而不是 `calc()` 的执行结果。

所以：

```python
f = lazy_sum(1, 3, 5, 7, 9)
```

此时还没有真正求和，只是拿到了一个函数。等你调用：

```python
f()
```

才会得到 `25`。

**为什么叫 lazy？**

因为它是“懒”的：先把计算规则打包起来，等真正调用时才计算。

---

### 闭包：函数带着外层变量一起走

```python
f = lazy_sum(1, 3, 5, 7, 9)
print(type(f).__name__)
print(f.__name__)
print(f())
print(f.__closure__ is not None)
print(len(f.__closure__))
```

**这行在干嘛？**

`f` 是一个函数，名字叫 `calc`。调用 `f()` 时，它还能访问 `lazy_sum()` 里的 `args`，所以能算出 `25`。

但 `lazy_sum()` 明明已经执行结束了，为什么 `args` 还在？

因为 `calc()` 引用了外层变量 `args`，Python 会把这个引用保存起来。这就是闭包。

**容易踩的坑**

闭包不是把外层变量“复制一份快照”塞进函数，而是保留对变量的引用。这个区别会直接导致下面的循环变量陷阱。

---

### 每次调用都会创建新函数

```python
f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
print(f1 == f2)
print(f1())
print(f2())
```

**这行在干嘛？**

即使参数一样，`lazy_sum()` 每调用一次，都会创建一个新的 `calc` 函数对象。

所以 `f1 == f2` 是 `False`。但它们各自保存的参数都是 `(1, 2, 3)`，所以调用结果都是 `6`。

---

### 循环变量陷阱：三个函数都记住同一个 `i`

```python
def count_bad():
    funcs = []
    for i in range(1, 4):
        def square():
            return i * i

        funcs.append(square)
    return funcs


print([func() for func in count_bad()])
```

**这行在干嘛？**

你可能以为三个函数分别记住 `1`、`2`、`3`，结果会是：

```python
[1, 4, 9]
```

实际输出却是：

```python
[9, 9, 9]
```

**为什么？**

闭包捕获的是变量 `i` 本身，不是每一轮循环时 `i` 的值。循环结束后，`i` 最终变成 `3`。三个函数调用时都去看同一个 `i`，于是全是 `3 * 3`。

---

### 用默认参数绑定当前值

```python
def count_fixed():
    funcs = []
    for i in range(1, 4):
        def square(i=i):
            return i * i

        funcs.append(square)
    return funcs
```

**这行在干嘛？**

`i=i` 这个写法看起来有点怪，但它的意思是：把当前这一轮的 `i` 作为默认参数保存下来。

默认参数是在函数定义时计算的，所以每个 `square()` 都拥有自己的默认参数：

- 第一个函数保存 `i=1`
- 第二个函数保存 `i=2`
- 第三个函数保存 `i=3`

于是结果变成正确的：

```python
[1, 4, 9]
```

**容易踩的坑**

这不是闭包专属技巧。你在第 13 关学过默认参数要小心可变对象，这里用的是不可变整数，所以是安全的。

---

### `nonlocal` —— 修改外层函数变量

```python
def counter(start=0):
    n = start

    def inc(step=1):
        nonlocal n
        n += step
        return n

    return inc
```

**这行在干嘛？**

`counter()` 返回一个计数函数 `inc()`。每调用一次 `inc()`，外层变量 `n` 就增加一次。

`nonlocal n` 的意思是：这里的 `n` 不是 `inc()` 里的局部变量，而是外层 `counter()` 里的那个 `n`。

**如果不写 `nonlocal` 会怎样？**

下面这种写法会报错：

```python
def inc():
    n += 1
    return n
```

因为只要你在函数里给变量赋值，Python 默认就把它当作当前函数的局部变量。`n += 1` 又要先读取 `n`，又要给 `n` 赋值，结果 Python 发现局部变量还没定义。

**什么时候用 `nonlocal`？**

当你在内层函数里需要修改外层函数的变量时，用 `nonlocal`。如果只是读取外层变量，不需要写。

## 🏃 跑一下试试

```bash
$ python closures.py
=== 函数可以作为返回值 ===
function
calc
25
True
1

=== 每次调用都会返回新函数 ===
False
6
6

=== 循环变量陷阱 ===
[9, 9, 9]

=== 修复循环变量陷阱 ===
[1, 4, 9]

=== nonlocal 修改外层变量 ===
1
2
12
101
```

## 💡 师兄的碎碎念

- 函数名后面不加括号，表示函数对象本身；加括号才是调用函数。
- 闭包会让内层函数记住外层变量，即使外层函数已经返回。
- 闭包捕获的是变量引用，不是定义时的值快照。
- 循环里返回函数时，特别小心循环变量陷阱；常见修复方式是默认参数 `i=i`。
- `nonlocal` 只能用于外层函数作用域的变量，不能用于全局变量；全局变量要用 `global`，但新手尽量少用。

## 🎓 这一关的知识点清单

- **函数作为返回值**：函数可以像普通对象一样被返回、赋值、传递。
- **闭包**：内层函数引用外层函数变量，并在外层函数结束后继续保留这些引用。
- **延迟计算**：返回函数本身，让调用者决定什么时候真正执行。
- **循环变量陷阱**：闭包捕获变量引用，循环结束后多个函数可能看到同一个最终值。
- **默认参数绑定**：用 `i=i` 把当前循环值固定下来。
- **nonlocal**：在内层函数中声明要修改外层函数变量。

## ➡️ 下一关

闭包搞定后，匿名函数就容易多了。下一关看 `lambda`：适合写短小的一次性函数，但不能滥用 👉 [下一关：匿名函数 →](../24-lambda/)


