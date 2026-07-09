# 第 8 关：循环

## 🎯 这一关你会学到

- `for...in` 循环遍历列表和序列
- `range()` 函数生成整数序列
- `while` 循环
- `break` 和 `continue` 控制循环流程
- Python 独有的 `for...else` 语法

## 🤔 先想一个问题

奶茶店每天早上要给所有员工点名。如果只有 3 个人，你可以喊三遍。但如果有 100 个人呢？你需要一个「循环」——拿着花名册，从第一个名字念到最后一个。Go 只有一种循环关键字 `for`，Python 有两种：`for...in` 和 `while`。但 Python 的 `for` 不是 Go 那种 `for i := 0; i < n; i++` 的计数器模式——它是**直接遍历集合中的每个元素**。

## 📖 看代码

```python
# for...in 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:                 # 依次输出：Hello, Michael! / Hello, Bob! / Hello, Tracy!
    print(f"Hello, {name}!")

# range() 生成整数序列
for i in range(5):       # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

# 计算 1+2+...+100
total = 0
for i in range(1, 101):
    total += i
print(f"1+2+...+100 = {total}")  # 1+2+...+100 = 5050

# while 循环
n = 10
while n > 0:                      # 10 9 8 7 6 5 4 3 2 1
    print(n, end=" ")
    n -= 1
print()

# break 和 continue
for i in range(10):               # 0 1 2 3 4
    if i == 5:
        break           # 到 5 就停
    print(i, end=" ")
print()

for i in range(10):               # 1 3 5 7 9
    if i % 2 == 0:
        continue        # 跳过偶数
    print(i, end=" ")
print()

# for...else（Python 独有！）
for i in range(5):
    if i == 99:
        break
else:
    print("循环正常结束，没有被 break")  # 循环正常结束，没有被 break
```

## 🔍 师兄给你逐行拆

### `for...in` —— 直接遍历，不要下标

```python
for name in names:
    print(f"Hello, {name}!")
```

**和 Go 的区别**

Go 的 `for i, v := range slice` 同时给你下标和值。Python 的 `for x in list` 默认只给你值。如果你也想要下标，用 `enumerate()`：

```python
for i, name in enumerate(names):
    print(f"{i}: {name}")
```

---

### `range()` —— 数字序列生成器

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

三种用法：`range(stop)`、`range(start, stop)`、`range(start, stop, step)`。**左闭右开**——包含 start，不包含 stop。

---

### `for...else` —— Python 独有的奇招

```python
for i in range(5):
    if i == 99:
        break
else:
    print("循环正常结束")
```

如果循环**正常结束**（没有被 `break` 中断），就执行 `else` 块。如果中途 `break` 了，`else` 不执行。这个语法在「搜索某个元素，没找到时执行默认操作」的场景很好用，但因为太反直觉，很多人不推荐使用。

## 🏃 跑一下试试

```bash
$ python loops.py
Hello, Michael!
Hello, Bob!
Hello, Tracy!
0 1 2 3 4
1+2+...+100 = 5050
10 9 8 7 6 5 4 3 2 1
0 1 2 3 4
1 3 5 7 9
循环正常结束，没有被 break
```

## 💡 师兄的碎碎念

- Python **没有** `do...while` 循环。如果需要「至少执行一次」，用 `while True:` + `break` 模拟。
- Python **没有** `i++` 和 `i--` 语法，用 `i += 1` 和 `i -= 1`。
- `range()` 返回的不是列表，是一个惰性迭代器，不会一次性占满内存。`range(10**9)` 不会炸掉你的内存。
- 嵌套循环可以用 `break` 跳出内层循环，但没法直接跳出外层。需要跳出多层时，可以用标志变量或封装成函数用 `return`。

## 🎓 这一关的知识点清单

- **for...in**：遍历可迭代对象（列表、字符串、range 等），每次取一个元素。
- **range()**：生成整数序列，`range(start, stop, step)`，左闭右开。
- **while**：条件循环，条件为 True 就一直执行。
- **break**：立即退出当前循环。
- **continue**：跳过本次循环，进入下一次。
- **for...else**：循环正常结束时执行 else，被 break 则不执行。

## ➡️ 下一关

循环搞定了！接下来学字典（Dict）——Python 中查找速度最快的数据结构 👉 [下一关：字典 Dict →](../09-dicts/)
