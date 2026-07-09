# 第 38 关：枚举类

## 🎯 这一关你会学到

- 为什么要用枚举替代魔法数字和魔法字符串
- `Enum("Name", names)` 快捷创建枚举
- 继承 `Enum` 定义更清晰的枚举类
- `.name`、`.value`、按名字/值查找枚举成员
- `@unique` 如何检查重复值
- `IntEnum` 和普通 `Enum` 的区别

## 🤔 先想一个问题

你用数字表示订单状态：

```python
status = 1
if status == 1:
    print("已支付")
```

问题来了：过两个月同事看到 `status == 1`，还能一眼知道它是“已支付”吗？如果另一个系统也用 `1` 表示“失败”，会不会混？

枚举就是给固定值起清楚名字：`OrderStatus.PAID` 比 `1` 更不容易误会。

## 📖 看代码

```python
# 枚举类

from enum import Enum, IntEnum, unique


print("=== 快捷创建枚举 ===")

# Enum() 可以快速创建枚举类，第二个参数是成员名列表。
Month = Enum(
    "Month",
    ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
)

print(Month.Jan)  # Month.Jan
print(Month.Jan.name)  # Jan
# 默认 value 从 1 开始递增。
print(Month.Jan.value)  # 1
print(Month["Jan"])  # Month.Jan
print(Month(1))  # Month.Jan


print("\n=== 继承 Enum 定义枚举 ===")


@unique
class Weekday(Enum):
    # 继承 Enum 的写法更适合业务代码，成员名和值一眼可见。
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7


day = Weekday.Sat
print(day)  # Weekday.Sat
print(day.name)  # Sat
print(day.value)  # 6
# 可以按名字或按值反向获取枚举成员。
print(Weekday["Sat"])  # Weekday.Sat
print(Weekday(6))  # Weekday.Sat


print("\n=== 遍历枚举 ===")

for member in Weekday:
    # 遍历枚举时拿到的是枚举成员，不是普通字符串或整数。
    print(f"{member.name} => {member.value}")


print("\n=== 枚举比较 ===")

print(Weekday.Mon == Weekday.Mon)  # True
print(Weekday.Mon == Weekday.Tue)  # False
print(Weekday.Mon is Weekday.Mon)  # True
# 普通 Enum 不会直接等于它的 value。
print(Weekday.Mon == 1)  # False


print("\n=== IntEnum 可以和整数比较 ===")


class HttpStatus(IntEnum):
    # IntEnum 适合需要和整数兼容的场景，例如 HTTP 状态码。
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


print(HttpStatus.OK == 200)  # True
print(HttpStatus.NOT_FOUND > HttpStatus.OK)  # True


print("\n=== @unique 检查重复值 ===")

try:
    # @unique 会在类创建时检查重复 value。
    @unique
    class BadStatus(Enum):
        SUCCESS = 1
        OK = 1
except ValueError as error:
    print(type(error).__name__)  # ValueError


print("\n=== match 中使用枚举 ===")

status = Weekday.Sat

match status:
    # match/case 可以直接匹配枚举成员。
    case Weekday.Sat | Weekday.Sun:
        print("周末")
    case _:
        print("工作日")
```

## 🔍 师兄给你逐行拆

### 快捷创建枚举

```python
Month = Enum(
    "Month",
    ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
)
```

**这行在干嘛？**

这是函数式 API，快速创建一个名为 `Month` 的枚举类，成员有 `Jan` 到 `Dec`。

如果不手动指定值，`Enum()` 会从 `1` 开始自动编号。

**怎么访问？**

```python
Month.Jan      # 通过属性访问
Month["Jan"]   # 通过名字访问
Month(1)       # 通过值访问
```

---

### `.name` 和 `.value`

```python
print(Month.Jan)
print(Month.Jan.name)
print(Month.Jan.value)
```

**这行在干嘛？**

一个枚举成员有两个常用信息：

- `.name`：成员名字，比如 `"Jan"`；
- `.value`：成员值，比如 `1`。

`print(Month.Jan)` 输出 `Month.Jan`，它不是普通字符串，也不是普通整数，而是枚举成员。

---

### 继承 `Enum` 定义枚举

```python
@unique
class Weekday(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7
```

**这行在干嘛？**

这是更推荐的写法：定义一个 `Weekday` 枚举类，每个成员都有明确值。

`@unique` 会检查枚举值不能重复。如果两个成员值一样，会直接报错。

**为什么推荐这种写法？**

因为它更适合写业务代码：清晰、可扩展、能加方法和注释。

---

### 遍历枚举

```python
for member in Weekday:
    print(f"{member.name} => {member.value}")
```

**这行在干嘛？**

枚举类可以直接遍历，依次拿到每个枚举成员。

如果你需要名字和值，就用 `member.name` 和 `member.value`。

---

### 普通 `Enum` 不等于整数

```python
print(Weekday.Mon == Weekday.Mon)
print(Weekday.Mon == Weekday.Tue)
print(Weekday.Mon is Weekday.Mon)
print(Weekday.Mon == 1)
```

**这行在干嘛？**

枚举成员是单例，所以：

```python
Weekday.Mon is Weekday.Mon
```

是 `True`。

但普通 `Enum` 不会和整数直接相等：

```python
Weekday.Mon == 1
```

是 `False`。

**为什么这样设计？**

枚举的意义就是避免把状态值和普通数字混在一起。`Weekday.Mon` 比 `1` 更有语义，也更安全。

---

### `IntEnum`：需要和整数兼容时使用

```python
class HttpStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500
```

**这行在干嘛？**

`IntEnum` 是整数枚举。它的成员可以和整数比较：

```python
HttpStatus.OK == 200
```

也支持大小比较：

```python
HttpStatus.NOT_FOUND > HttpStatus.OK
```

**什么时候用？**

当你必须和外部系统的整数协议兼容，比如 HTTP 状态码、数据库里的数字状态，可以考虑 `IntEnum`。

如果没有这个需求，优先用普通 `Enum`，类型边界更清楚。

---

### `@unique` 检查重复值

```python
try:
    @unique
    class BadStatus(Enum):
        SUCCESS = 1
        OK = 1
except ValueError as error:
    print(type(error).__name__)
```

**这行在干嘛？**

`SUCCESS` 和 `OK` 的值都等于 `1`。加了 `@unique` 后，Python 会发现重复值并抛出 `ValueError`。

**为什么有用？**

有些业务状态不能有别名。重复值会让状态判断变模糊，`@unique` 可以提前发现问题。

---

### `match` 中使用枚举

```python
match status:
    case Weekday.Sat | Weekday.Sun:
        print("周末")
    case _:
        print("工作日")
```

**这行在干嘛？**

枚举很适合和 `match` 搭配。这里判断 `status` 是周六或周日，就输出“周末”，否则输出“工作日”。

比起写 `status in (6, 7)`，枚举版本更清楚。

## 🏃 跑一下试试

```bash
$ python enum-demo.py
=== 快捷创建枚举 ===
Month.Jan
Jan
1
Month.Jan
Month.Jan

=== 继承 Enum 定义枚举 ===
Weekday.Sat
Sat
6
Weekday.Sat
Weekday.Sat

=== 遍历枚举 ===
Mon => 1
Tue => 2
Wed => 3
Thu => 4
Fri => 5
Sat => 6
Sun => 7

=== 枚举比较 ===
True
False
True
False

=== IntEnum 可以和整数比较 ===
True
True

=== @unique 检查重复值 ===
ValueError

=== match 中使用枚举 ===
周末
```

## 💡 师兄的碎碎念

- 枚举适合表示固定集合：星期、月份、订单状态、用户角色、错误码。
- 普通 `Enum` 和整数/字符串保持边界，不会随便相等。
- 需要兼容整数协议时，用 `IntEnum`。
- `@unique` 能提前发现重复值，推荐在业务枚举上使用。
- 不要到处散落魔法数字和魔法字符串；把它们收拢成枚举更好维护。

## 🎓 这一关的知识点清单

- **Enum**：定义枚举类型，成员是固定的一组命名值。
- **函数式创建**：`Enum("Month", ("Jan", "Feb"))` 快速创建枚举。
- **继承式创建**：`class Weekday(Enum): ...` 更适合业务代码。
- **name/value**：`.name` 是成员名，`.value` 是成员值。
- **按名查找**：`Weekday["Sat"]`。
- **按值查找**：`Weekday(6)`。
- **@unique**：检查枚举值是否重复。
- **IntEnum**：能和整数兼容的枚举。

## ➡️ 下一关

枚举类讲完，面向对象进阶最后一关是元类。它比较抽象，我们会用“类也是对象”这条线慢慢拆 👉 [下一关：元类 →](../39-metaclass/)




