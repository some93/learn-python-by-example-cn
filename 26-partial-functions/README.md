# 第 26 关：偏函数

## 🎯 这一关你会学到

- `functools.partial()` 的基本用法
- 如何提前固定函数的一部分参数
- 位置参数和关键字参数在 partial 里的行为差异
- partial 和手写包装函数的区别
- 在真实业务里用 partial 减少重复配置

## 🤔 先想一个问题

你每天去同一家奶茶店，点单永远是「中杯、少糖、去冰、加珍珠」。如果每次都完整说一遍，当然可以，但很烦。

更聪明的做法是让店员给你记一个「老样子」按钮：以后你只说「小王一杯」，系统自动补上中杯、少糖、去冰、珍珠。偶尔想改成正常冰，也只需要临时覆盖一下。

`functools.partial()` 干的就是这件事：**把一个函数的一部分参数提前填好，生成一个更专用、更好用的新函数**。

## 📖 看代码

```python
# 偏函数（Partial Function）

from functools import partial


print("=== 进制转换 ===")

# int() 默认按十进制转换字符串
print(int("12345"))  # 12345

# int() 可以通过 base 参数指定进制
print(int("12345", base=8))   # 5349
print(int("12345", base=16))  # 74565

# 经常转二进制时，把 base=2 预先固定住
int2 = partial(int, base=2)

print(int2("1000000"))  # 64
print(int2("1010101"))  # 85

# 关键字参数不是锁死的，调用时传同名参数会覆盖预设值
print(int2("10", base=10))  # 10

# partial 对象会记住原函数、预设的位置参数和关键字参数
print(int2.func)
print(int2.args)
print(int2.keywords)


print("\n=== 固定位置参数 ===")

# 固定位置参数时，新参数会追加到后面
max10 = partial(max, 10)

print(max10(5, 6, 7))     # 等价于 max(10, 5, 6, 7)
print(max10(-1, -2, -3))  # 10 仍然参与比较


print("\n=== 奶茶店常用订单 ===")


def make_milk_tea(customer, size, sugar, ice, topping):
    return f"{customer}: {size}, {sugar}, {ice}, 加{topping}"


# 把常用配置固定下来，只留下顾客名和少量临时修改项
office_order = partial(
    make_milk_tea,
    size="中杯",
    sugar="少糖",
    ice="去冰",
    topping="珍珠",
)

print(office_order("小王"))
print(office_order("小李", ice="正常冰"))
print(office_order("小张", topping="椰果"))


print("\n=== 价格格式化 ===")


def format_price(price, currency="CNY", precision=2):
    return f"{currency} {price:.{precision}f}"


# 为不同业务场景准备专用格式化函数
cny_price = partial(format_price, currency="CNY", precision=2)
jpy_price = partial(format_price, currency="JPY", precision=0)

print(cny_price(19.9))
print(jpy_price(1999.6))

prices = [12, 3.5, 99.99]
formatted_prices = [cny_price(price) for price in prices]
print(formatted_prices)


print("\n=== 手写包装函数 ===")


def int16(s):
    return int(s, base=16)


def strict_int2(s):
    return int(s, base=2)


print(int16("ff"))
print(strict_int2("10"))
```

## 🔍 师兄给你逐行拆

### `partial(int, base=2)` —— 给 `int()` 做一个二进制专用版

```python
from functools import partial

int2 = partial(int, base=2)

print(int2("1000000"))  # 64
print(int2("1010101"))  # 85
```

**这行在干嘛？**

`int()` 原本可以把字符串转成整数，默认按十进制理解。比如 `int("123")` 得到 `123`。

但 `int()` 还有一个 `base` 参数，可以指定字符串是什么进制：

```python
int("1000000", base=2)   # 二进制，结果是 64
int("12345", base=8)     # 八进制，结果是 5349
int("12345", base=16)    # 十六进制，结果是 74565
```

如果你的程序里经常要解析二进制字符串，每次都写 `int(x, base=2)` 就有点啰嗦。于是我们用：

```python
int2 = partial(int, base=2)
```

生成一个新函数 `int2`，它等价于「默认 `base=2` 的 `int()`」。

**为什么这么写？**

因为 `partial()` 适合处理这种场景：**原函数很好用，但某些参数总是重复出现**。与其在代码里到处复制同样的参数，不如把这些参数封装成一个更明确的新函数名。

`int2("1010101")` 看起来就比 `int("1010101", base=2)` 更像一句人话：把这个字符串当二进制整数解析。

**生活类比**

`int()` 像一个万能翻译员：你告诉它「这是二进制」「这是八进制」「这是十六进制」，它都能翻译。

`int2` 像专门负责二进制的窗口：你不用每次解释「这是二进制」，窗口默认就按二进制处理。

---

### 关键字参数可以被覆盖 —— partial 不是焊死参数

```python
print(int2("10", base=10))  # 10

print(int2.func)
print(int2.args)
print(int2.keywords)
```

**这行在干嘛？**

`int2` 预设了 `base=2`，所以 `int2("10")` 会把 `"10"` 当二进制，结果是 `2`。

但这里调用时又传了 `base=10`：

```python
int2("10", base=10)
```

同名关键字参数会覆盖 partial 里预设的关键字参数，所以结果变成十进制的 `10`。

**为什么这么设计？**

`partial()` 不是「锁死参数」，而是「提前填默认参数」。后面调用时如果传入新的位置参数，会追加到已有位置参数后面；如果传入同名关键字参数，会覆盖旧的关键字参数。

这也是官方文档强调的核心语义：partial 返回的新对象被调用时，会把预设参数和新传入的参数合并后再调用原函数。

**容易踩的坑**

如果你希望 `int2` 永远只能按二进制解析，不允许别人覆盖 `base`，那就别用 partial 暴露这个可覆盖入口，手写一个包装函数更稳：

```python
def strict_int2(s):
    return int(s, base=2)
```

这时调用方只能传 `s`，没地方传 `base=10`。

---

### `partial(max, 10)` —— 固定位置参数

```python
max10 = partial(max, 10)

print(max10(5, 6, 7))     # 等价于 max(10, 5, 6, 7)
print(max10(-1, -2, -3))  # 10 仍然参与比较
```

**这行在干嘛？**

`partial(max, 10)` 创建了一个新函数 `max10`，它每次调用 `max()` 时都会先塞进去一个 `10`。

所以：

```python
max10(5, 6, 7)
```

等价于：

```python
max(10, 5, 6, 7)
```

结果当然是 `10`。

**为什么这个例子重要？**

它说明 partial 固定位置参数时，参数是**从左往右提前填进去的**。后续调用传入的位置参数，会追加到这些预设位置参数后面。

**容易踩的坑**

按本教程推荐的 Python 3.10/3.12 口径，普通 `partial()` 不能随便固定「中间某个位置参数」。比如一个函数长这样：

```python
def send_message(sender, receiver, content):
    ...
```

你想只固定 `receiver`，但不固定 `sender`，用普通 `partial()` 就不顺手。解决办法通常是：

- 把容易被固定的参数设计成关键字参数；
- 或者手写一个小包装函数；
- 或者调整函数参数顺序。

补充一句：Python 3.14 给 `functools.partial()` 新增了 `Placeholder`，可以预留位置参数的空位。不过这是新版特性，入门阶段先掌握最常见的关键字参数预设就够了。

---

### 奶茶店常用订单 —— partial 的真实用途

```python
def make_milk_tea(customer, size, sugar, ice, topping):
    return f"{customer}: {size}, {sugar}, {ice}, 加{topping}"


office_order = partial(
    make_milk_tea,
    size="中杯",
    sugar="少糖",
    ice="去冰",
    topping="珍珠",
)

print(office_order("小王"))
print(office_order("小李", ice="正常冰"))
print(office_order("小张", topping="椰果"))
```

**这行在干嘛？**

`make_milk_tea()` 原本需要 5 个参数：顾客、杯型、甜度、冰量、加料。

但办公室团购时，大多数人都点「中杯、少糖、去冰、珍珠」。所以我们用 partial 创建一个 `office_order`，把这些高频配置先固定住：

```python
office_order("小王")
```

只传顾客名，就能生成完整订单。

如果某个人要正常冰，也可以临时覆盖：

```python
office_order("小李", ice="正常冰")
```

**为什么这个例子比 `int2` 更贴近实际？**

因为真实项目里 partial 最常见的用途不是为了炫技，而是为了消除重复配置。比如：

- 给日志函数预设 `level="INFO"`；
- 给请求函数预设 `timeout=5`；
- 给格式化函数预设 `currency="CNY"`；
- 给回调函数提前绑定上下文参数。

这些场景里，partial 都是在帮你创建「更专用的小函数」。

---

### 价格格式化 —— 给业务场景起一个清楚的名字

```python
def format_price(price, currency="CNY", precision=2):
    return f"{currency} {price:.{precision}f}"


cny_price = partial(format_price, currency="CNY", precision=2)
jpy_price = partial(format_price, currency="JPY", precision=0)

print(cny_price(19.9))
print(jpy_price(1999.6))
```

**这行在干嘛？**

`format_price()` 是一个通用函数：传价格、货币、保留小数位，就能格式化金额。

但人民币价格通常保留两位小数，日元价格通常不保留小数。于是我们用 partial 生成两个专用函数：

```python
cny_price(19.9)    # CNY 19.90
jpy_price(1999.6)  # JPY 2000
```

**为什么这么写？**

因为 `cny_price` 和 `jpy_price` 的名字本身就是文档。读代码的人一眼就知道这里是在格式化人民币价格还是日元价格。

**生活类比**

你可以每次都对收银员说「人民币，保留两位小数」。但如果柜台上有两个按钮：`人民币价格`、`日元价格`，你直接按按钮就行。partial 就是在代码里造这种按钮。

---

### partial 和手写包装函数怎么选？

```python
def int16(s):
    return int(s, base=16)


def strict_int2(s):
    return int(s, base=2)
```

**这行在干嘛？**

这两个函数是手写包装函数，效果和 partial 很像：

```python
int16("ff")       # 255
strict_int2("10") # 2
```

**什么时候用 partial？**

当你只是想固定几个参数，没有额外逻辑时，用 partial 很干净：

```python
cny_price = partial(format_price, currency="CNY", precision=2)
```

**什么时候手写函数？**

如果你需要：

- 做参数校验；
- 写更多业务逻辑；
- 禁止调用方覆盖某些参数；
- 给新函数写清楚的文档字符串；

那手写函数更直观。

一句话：**partial 适合简单预设，def 适合认真封装**。

## 🏃 跑一下试试

```bash
$ python partial-functions.py
=== 进制转换 ===
12345
5349
74565
64
85
10
<class 'int'>
()
{'base': 2}

=== 固定位置参数 ===
10
10

=== 奶茶店常用订单 ===
小王: 中杯, 少糖, 去冰, 加珍珠
小李: 中杯, 少糖, 正常冰, 加珍珠
小张: 中杯, 少糖, 去冰, 加椰果

=== 价格格式化 ===
CNY 19.90
JPY 2000
['CNY 12.00', 'CNY 3.50', 'CNY 99.99']

=== 手写包装函数 ===
255
2
```

## 💡 师兄的碎碎念

- `partial(func, *args, **kwargs)` 会返回一个新的可调用对象，不会立刻执行 `func`。
- partial 固定的位置参数会排在后续位置参数前面，`partial(max, 10)(1, 2)` 等价于 `max(10, 1, 2)`。
- partial 固定的关键字参数可以被调用时的同名关键字参数覆盖，所以它更像「默认配置」，不是「强制配置」。
- partial 对象有 `func`、`args`、`keywords` 三个常用属性，调试时可以看看它到底包了谁、预设了什么。
- 不要为了少写一行代码强行用 partial。新手读不懂时，清清楚楚写一个 `def` 往往更好。

## 🎓 这一关的知识点清单

- **偏函数**：把原函数的一部分参数提前固定，生成一个新的可调用对象。
- **functools.partial()**：标准库 `functools` 提供的偏函数工具，用法是 `partial(func, *args, **kwargs)`。
- **固定关键字参数**：例如 `partial(int, base=2)`，让新函数默认按二进制解析字符串。
- **固定位置参数**：例如 `partial(max, 10)`，后续参数会追加到 `10` 后面。
- **参数覆盖**：调用 partial 对象时，同名关键字参数会覆盖预设关键字参数。
- **partial vs def**：只固定参数用 partial；需要校验、文档、不可覆盖规则或复杂逻辑时用 `def`。

## ➡️ 下一关

偏函数搞定！函数式编程这一小段也收尾了。接下来我们进入 Python 的代码组织方式：模块、导入、`__name__ == "__main__"` 👉 [下一关：模块 →](../27-modules/)


