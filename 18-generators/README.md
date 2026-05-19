# 第 18 关：生成器（师兄带你学 Python）

## 🎯 这一关你会学到

- Generator 惰性求值
- 生成器表达式 (x for x in ...)
- yield 关键字定义生成器函数
- 惰性求值节省内存

## 🤔 先想一个问题

列表生成式像一次性把所有奶茶都做好摆桌上——100 万杯桌子放不下。生成器像现做现卖——来一个做一个，永远只占一杯的空间。这就是惰性求值的魔力。

## 📖 看代码

```python
# 生成器（Generator）

# 把列表生成式的 [] 换成 () 就是生成器
g = (x * x for x in range(5))
print(g)           # <generator object ...>
print(next(g))     # 0
print(next(g))     # 1

# 用 for 遍历生成器（推荐方式）
g2 = (x * x for x in range(5))
for val in g2:
    print(val, end=" ")
print()

# 用 yield 关键字定义生成器函数
def fib(max_count):
    n, a, b = 0, 0, 1
    while n < max_count:
        yield b          # yield 暂停并返回值
        a, b = b, a + b
        n += 1

# 调用生成器函数得到生成器对象
for num in fib(10):
    print(num, end=" ")
print()

# 生成器可以节省内存
# list(range(1000000)) 会立刻占用大量内存
# range(1000000) 是惰性的，几乎不占内存

# yield 的执行流程演示
def count_up_to(n):
    print("开始生成")
    i = 1
    while i <= n:
        print(f"  即将 yield {i}")
        yield i
        print(f"  yield {i} 之后继续")
        i += 1
    print("生成结束")

for val in count_up_to(3):
    print(f"收到: {val}")
```

## 🔍 师兄给你逐行拆

生成器是一种特殊的迭代器——它不一次性生成所有元素，而是按需产生，用到一个才算一个。把列表生成式的 [] 换成 () 就变成了生成器。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python generators.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **(expr for x in iterable) 生成器表达式**
- **yield 暂停并返回值**
- **next() 手动取下一个值**
- **for 循环自动遍历生成器**

## 🎓 这一关的知识点清单

- **Generator 惰性求值**
- **生成器表达式 (x for x in ...)**
- **yield 关键字定义生成器函数**
- **惰性求值节省内存**

## ➡️ 下一关

本关搞定！接下来学 迭代器 👉 [下一关：迭代器 →](../19-iterators/)
