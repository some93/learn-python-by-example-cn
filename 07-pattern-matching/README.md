# 第 7 关：模式匹配（师兄带你学 Python）

## 🎯 这一关你会学到

- Python 3.10+ 引入的 `match/case` 语法
- 匹配常量、多个值、序列（解构）
- 通配符 `case _` 和带条件守卫的匹配
- 与 `if/elif` 和 Go `switch` 的对比

## 🤔 先想一个问题

上一关我们学了 `if/elif/else`，但如果条件分支特别多——比如根据 HTTP 状态码做 10 种不同处理——写一长串 `elif` 又丑又难维护。Go 有 `switch`，Python 3.10 之前只能硬写 `elif` 链。好消息是 Python 3.10 终于加了 `match/case`，而且比 Go 的 `switch` 还强大——它能**解构数据结构**。

## 📖 看代码

```python
# Python 3.10+ 的 match/case 模式匹配

# 基本用法：匹配常量
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Unknown status: {status}")

# 匹配多个值
command = "quit"

match command:
    case "quit" | "exit" | "q":
        print("退出程序")
    case "help" | "h":
        print("显示帮助")
    case _:
        print(f"未知命令: {command}")

# 匹配序列（解构赋值）
point = (0, 5)

match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"在 x 轴上, x={x}")
    case (0, y):
        print(f"在 y 轴上, y={y}")
    case (x, y):
        print(f"任意点: ({x}, {y})")

# 带条件守卫
age = 15

match age:
    case n if n < 0:
        print("年龄不能为负")
    case n if n < 18:
        print(f"{n} 岁，未成年")
    case n if n < 60:
        print(f"{n} 岁，成年人")
    case _:
        print("老年人")
```

## 🔍 师兄给你逐行拆

### 基本常量匹配 —— 替代 `elif` 链

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print(f"Unknown: {status}")
```

**这行在干嘛？**

`match` 后面跟要匹配的值，`case` 后面是匹配模式。从上到下依次尝试，命中就执行对应代码块，`case _` 是通配符（类似 Go `switch` 的 `default`）。

**和 Go switch 的区别**

Go 的 `switch` 每个 `case` 默认自动 break，不需要写 `break`。Python 的 `match/case` 也是——**命中一个就停，不会 fallthrough**。

---

### 匹配多个值 —— 用 `|` 分隔

```python
case "quit" | "exit" | "q":
    print("退出程序")
```

用 `|` 可以在一个 `case` 里匹配多个值，等价于 Go 里 `case "quit", "exit", "q":`。

---

### 序列解构 —— match 最强大的特性

```python
match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"在 x 轴上, x={x}")
    case (0, y):
        print(f"在 y 轴上, y={y}")
```

**这行在干嘛？**

不仅匹配值，还能**解构数据**并把内容绑定到变量。`(x, 0)` 意思是「这是一个两元素元组，第二个元素是 0，第一个元素绑定到变量 x」。这是 Go 的 switch 做不到的！

**生活类比**

普通的 switch 像安检——检查你的证件号是否匹配。match/case 的解构像**拆快递**——不仅看快递单号，还直接把包裹打开，把里面的东西分别拿出来。

---

### 条件守卫（Guard）

```python
case n if n < 18:
    print(f"{n} 岁，未成年")
```

`case n` 匹配任意值并绑定到 `n`，`if n < 18` 是额外条件。只有两者都满足才命中。

## 🏃 跑一下试试

```bash
$ python pattern-matching.py
Not Found
退出程序
在 y 轴上, y=5
15 岁，未成年
```

## 💡 师兄的碎碎念

- `match/case` 需要 **Python 3.10+**，低版本会报 `SyntaxError`。在公司项目里用之前先确认 Python 版本。
- `case _` 的 `_` 是特殊的通配符，不能当变量用。如果你在 case 里写 `case x`，`x` 会被当作捕获变量（匹配一切并赋值）。
- match/case 还能匹配类实例（`case Point(x=0, y=y)`），在面向对象编程里非常好用，后面会讲到。
- 如果你的 Python 版本低于 3.10，就老老实实用 `if/elif/else`，或者用 dict 映射替代：`actions = {200: "OK", 404: "Not Found"}`。

## 🎓 这一关的知识点清单

- **match/case**：Python 3.10+ 的模式匹配语法，从上到下匹配，命中即停。
- **常量匹配**：`case 200:` 匹配具体值。
- **多值匹配**：`case "a" | "b":` 用 `|` 匹配多个候选值。
- **通配符**：`case _:` 匹配一切，类似 `default`。
- **序列解构**：`case (x, 0):` 匹配并绑定变量，是 match 最强大的特性。
- **条件守卫**：`case n if n > 0:` 在匹配的基础上加额外条件。

## ➡️ 下一关

分支判断搞定了！接下来学循环——让程序重复执行某段逻辑 👉 [下一关：循环 →](../08-loops/)
