# 第 24 关：匿名函数（师兄带你学 Python）

## 🎯 这一关你会学到

- lambda 表达式
- lambda 参数: 表达式 语法
- lambda 在 map/filter/sorted 中的应用
- lambda 只能写一个表达式

## 🤔 先想一个问题

lambda 像便利店的一次性餐具——用完就扔，不值得买一套正式餐具（def 定义函数）。但如果逻辑复杂，还是用 def 正经定义比较好。

## 📖 看代码

```python
# 匿名函数（lambda）

# lambda 语法：lambda 参数: 表达式
f = lambda x: x * x
print(f(5))    # 25

# 等价于
def f2(x):
    return x * x

# lambda 常用于排序的 key 参数
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)

# 配合 map 使用
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# 配合 filter 使用
print(list(filter(lambda x: x % 2 == 1, range(1, 11))))

# lambda 也可以赋值给变量（但不推荐，直接用 def 更清晰）
add = lambda x, y: x + y
print(add(3, 5))   # 8

# lambda 作为返回值
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
print(add5(10))    # 15

# lambda 只能写一个表达式，不能写多条语句
# lambda x: print(x); return x  # SyntaxError!
```

## 🔍 师兄给你逐行拆

lambda 是不需要名字的一次性小函数——适合逻辑简单、只用一次的场合。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python lambda.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **lambda x: x*x 等价于 def f(x): return x*x**
- **常用于 sorted(key=lambda ...)**
- **可以赋值给变量但不推荐**
- **不能包含多条语句**

## 🎓 这一关的知识点清单

- **lambda 表达式**
- **lambda 参数: 表达式 语法**
- **lambda 在 map/filter/sorted 中的应用**
- **lambda 只能写一个表达式**

## ➡️ 下一关

本关搞定！接下来学 装饰器 👉 [下一关：装饰器 →](../25-decorators/)
