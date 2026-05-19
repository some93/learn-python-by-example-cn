# 第 38 关：枚举类（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解枚举的用途
- 用 `Enum` 和 `@unique` 定义枚举
- 掌握枚举的多种访问方式
- 在 `match` 语句中使用枚举

## 🤔 先想一个问题

你用数字 0-6 表示星期一到星期天，但同事把 0 当成了星期天，系统炸了。如果有一种类型，`Weekday.Mon` 就是星期一，不会搞混。这就是**枚举**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 枚举类

from enum import Enum, unique

# 定义枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 访问枚举成员
print(Month.Jan)          # Month.Jan
print(Month.Jan.value)    # 1（自动从 1 开始赋值）

# 遍历枚举
for name, member in Month.__members__.items():
    print(f"{name} => {member.value}")

# 自定义枚举类（推荐方式）
@unique   # 保证值不重复
class Weekday(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7

# 多种访问方式
day = Weekday.Mon
print(day)              # Weekday.Mon
print(day.name)         # Mon
print(day.value)        # 1
print(Weekday(1))       # Weekday.Mon（通过值获取）
print(Weekday['Mon'])   # Weekday.Mon（通过名字获取）

# 枚举比较
print(Weekday.Mon == Weekday.Mon)    # True
print(Weekday.Mon == Weekday.Tue)    # False
# Weekday.Mon < Weekday.Tue          # TypeError! 枚举不支持大小比较

# 枚举用于 match
status = Weekday.Sat
match status:
    case Weekday.Sat | Weekday.Sun:
        print("周末！")
    case _:
        print("工作日")
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `Enum('Name', ('A', 'B'))` 是快捷方式，`value` 从 1 开始自动编号
- 继承 `Enum` 类是更推荐的定义方式，可以自定义 `value`
- `@unique` 装饰器保证枚举值不重复
- 枚举成员可以通过 `.name`（名字）和 `.value`（值）访问
- 枚举成员是单例，可以用 `==` 比较，但不支持 `<` / `>` 排序

## 🏃 跑一下试试

```bash
cd 38-enum
python enum.py
```

## 💡 师兄的碎碎念

- `Enum('Name', ('A', 'B'))` 是快捷方式，`value` 从 1 开始自动编号
- 继承 `Enum` 类是更推荐的定义方式，可以自定义 `value`
- `@unique` 装饰器保证枚举值不重复
- 枚举成员可以通过 `.name`（名字）和 `.value`（值）访问
- 枚举成员是单例，可以用 `==` 比较，但不支持 `<` / `>` 排序

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `Enum('Name', tuple)` | 快捷创建枚举 |
| `class X(Enum)` | 继承方式定义枚举（推荐） |
| `@unique` | 保证枚举值不重复 |
| `.name / .value` | 获取枚举成员的名字和值 |
| `Weekday(1)` | 通过值获取枚举成员 |
| `Weekday['Mon']` | 通过名字获取枚举成员 |

## ➡️ 下一关

下一关我们学习 [元类](../39-metaclass/README.md)，继续加油！
