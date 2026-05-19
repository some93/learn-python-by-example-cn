# 第 6 关：条件判断（师兄带你学 Python）

## 🎯 这一关你会学到

- `if`/`elif`/`else` 的语法结构
- Python 用**缩进**标记代码块（不像 Go 用大括号）
- 哪些值会被当成 True，哪些是 False
- 逻辑运算符 `and`/`or`/`not`
- `input()` 获取用户输入

## 🤔 先想一个问题

你去奶茶店点单，收银员看了你一眼：「同学，你满 18 了吗？」——满 18 可以加酒精基底，没满只能喝普通款。这就是最简单的条件判断：**根据某个条件，走不同的分支**。

如果条件更复杂呢？18 以上可以加酒精，12-17 岁可以加咖啡因，12 以下只能喝果汁——这就是多条件分支。Python 的 `if/elif/else` 就是干这个的。

## 📖 看代码

```python
# Python 中条件判断使用 if/elif/else 语句

age = 20

# 单个 if 判断
if age >= 18:
    print("你已经成年了")
    print("可以去网吧了")

# if-else 判断
if age >= 18:
    print("adult")
else:
    print("teenager")

# if-elif-else 多条件判断
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

# 条件表达式中的真假值
# 非零数值、非空字符串、非空列表都被视为 True
# 0、空字符串 ''、空列表 []、None 都被视为 False
if "hello":
    print("非空字符串是 True")

if 0:
    print("这行不会执行")
else:
    print("0 是 False")

# 逻辑运算符 and / or / not
x = 15
if x > 10 and x < 20:
    print(f"{x} 在 10 到 20 之间")

if not x > 100:
    print(f"{x} 不大于 100")

# 简化写法：链式比较
if 10 < x < 20:
    print("Python 支持链式比较，这是语法糖")
```

## 🔍 师兄给你逐行拆

### `if age >= 18:` —— 最基础的条件判断

```python
if age >= 18:
    print("你已经成年了")
    print("可以去网吧了")
```

**这行在干嘛？**

`if` 后面跟一个**条件表达式**，冒号 `:` 结尾，下一行缩进 4 个空格的代码就是「条件为真时执行的代码块」。`age >= 18` 返回 `True` 或 `False`。

**为什么这么写？**

Python 用**缩进**来标记代码块，不像 Go/Java/C 用大括号 `{}`。这意味着缩进不是「好看」，而是**语法要求**——缩进错了，程序直接报错或逻辑出错。

**容易踩的坑**

1. **忘记冒号**：`if age >= 18` 后面必须有冒号 `:`，少写必报 `SyntaxError`
2. **缩进不一致**：同一个代码块里，有的行用 4 个空格，有的行用 Tab，Python 会报 `IndentationError`。建议统一用 **4 个空格**
3. **缩进层级错误**：两行 `print` 必须对齐在同一个缩进级别，否则第二行不属于 `if` 代码块

---

### `if/elif/else` —— 多条件分支

```python
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
```

**这行在干嘛？**

从上往下依次检查条件：先看 `age >= 18`，不满足就看 `age >= 6`，都不满足就走 `else`。**只会执行第一个满足条件的分支**，后面的不看了。

**为什么这么写？**

`elif` 是 `else if` 的缩写，Python 不像 Go 那样用 `else if`（两个单词），而是合成一个关键字 `elif`，更简洁。你可以有任意多个 `elif`，但 `else` 最多只能有一个，且必须放在最后。

**生活类比**

就像奶茶店的分级优惠券：先看你是不是 VIP，是就打 8 折；不是的话看你是不是会员，是就打 9 折；都不是就原价。**从上往下匹配，命中就停**。

**容易踩的坑**

条件的顺序很重要！如果你把 `age >= 6` 放在 `age >= 18` 前面，那 20 岁的人也会匹配到 `age >= 6` 就停了，永远走不到 `age >= 18` 的分支。

---

### 真假值判定 —— Python 的「宽容」

```python
if "hello":
    print("非空字符串是 True")

if 0:
    print("这行不会执行")
```

**这行在干嘛？**

Python 的 `if` 不要求条件必须是布尔值。任何对象都可以放在 `if` 后面，Python 会自动判断它的「真假性」。

**规则很简单**：

| 假值（False） | 真值（True） |
|--------------|-------------|
| `False` | `True` |
| `0`, `0.0` | 任何非零数字 |
| `""` 空字符串 | 任何非空字符串 |
| `[]` 空列表 | 任何非空列表 |
| `{}` 空字典 | 任何非空字典 |
| `None` | 其他一切对象 |

**一句话总结**：空的、零的、None 的都是 False，其他都是 True。

这个特性让代码更简洁，比如判断列表是否为空：`if my_list:` 比 `if len(my_list) > 0:` 简洁得多。

---

### `and`/`or`/`not` —— 逻辑运算符

```python
x = 15
if x > 10 and x < 20:
    print(f"{x} 在 10 到 20 之间")

# Python 独有的链式比较
if 10 < x < 20:
    print("Python 支持链式比较，这是语法糖")
```

**这行在干嘛？**

`and` 表示「且」，两边都为 True 才是 True。`or` 表示「或」，有一边为 True 就是 True。`not` 表示「非」，取反。

**和 Go 的对比**

Go 用的是 `&&`、`||`、`!`，Python 用的是英文单词 `and`、`or`、`not`，更易读。

**Python 独有彩蛋**：`10 < x < 20` 这种链式比较在大多数语言里不支持，但 Python 可以！它等价于 `x > 10 and x < 20`，但写起来更像数学公式。

## 🏃 跑一下试试

```bash
$ python if-else.py
你已经成年了
可以去网吧了
adult
adult
非空字符串是 True
0 是 False
15 在 10 到 20 之间
15 不大于 100
Python 支持链式比较，这是语法糖
```

## 💡 师兄的碎碎念

- Python 没有 `switch` 语句（Python 3.10+ 加了 `match/case`，下一关讲）。3.10 之前只能用 `if/elif/else` 链来替代。
- **三元表达式**：`result = "adult" if age >= 18 else "kid"`，一行搞定简单条件赋值，等价于 Go 里没有的三元运算符（Go 也没有三元运算符，大家半斤八两）。
- `input()` 返回的永远是**字符串**，如果你要拿来做数字比较，必须先 `int()` 转换，否则 `"20" >= 18` 会报 `TypeError`。
- 缩进用 **4 个空格**是 PEP 8 官方推荐。Tab 也能用，但不要混用，否则 `TabError` 等着你。

## 🎓 这一关的知识点清单

- **if/elif/else**：条件分支语句，`elif` 可以有多个，`else` 最多一个。
- **缩进即代码块**：Python 用缩进代替大括号，缩进错误会导致语法错误或逻辑错误。
- **真假值规则**：空值/零值/None 为 False，其他为 True。
- **逻辑运算符**：`and`（且）、`or`（或）、`not`（非），用英文单词而不是符号。
- **链式比较**：`10 < x < 20` 是 Python 独有语法糖，等价于 `x > 10 and x < 20`。
- **三元表达式**：`value_if_true if condition else value_if_false`。

## ➡️ 下一关

条件判断搞定了！Python 3.10 还引入了更强大的模式匹配 `match/case`——比 Go 的 `switch` 还灵活 👉 [下一关：模式匹配 →](../07-pattern-matching/)
