# 第 34 关：__slots__（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解 Python 实例可以动态绑定属性
- 用 `__slots__` 限制实例属性
- 了解 `__slots__` 对子类的影响
- 了解 `__slots__` 的内存优化原理

## 🤔 先想一个问题

你开了个快递柜，本来每个格子可以放任何东西。但你发现有人往格子里塞沙发、自行车……你想限制只能放快递和包裹。Python 的 `__slots__` 就是给类加「格子限制」。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# __slots__

# 正常情况下，可以给实例绑定任意属性
class Student:
    pass

s = Student()
s.name = 'Alice'      # 动态绑定属性
s.age = 18
print(s.name, s.age)

# 甚至可以绑定方法
from types import MethodType

def set_score(self, score):
    self.score = score

s.set_score = MethodType(set_score, s)
s.set_score(99)
print(s.score)    # 99

# 用 __slots__ 限制实例属性
class Person:
    __slots__ = ('name', 'age')   # 只允许绑定 name 和 age

p = Person()
p.name = 'Bob'
p.age = 25
# p.score = 99   # AttributeError! 不允许绑定 score

# __slots__ 对子类不起作用（除非子类也定义 __slots__）
class GraduateStudent(Person):
    pass

g = GraduateStudent()
g.name = 'Charlie'
g.score = 100     # 可以！子类没有 __slots__ 限制
print(g.score)

# 子类也定义 __slots__ 时，子类允许的属性是两者的并集
class UnderGrad(Person):
    __slots__ = ('score',)   # 加上父类的 name、age，共三个

u = UnderGrad()
u.name = 'Dave'
u.age = 20
u.score = 88
# u.gpa = 3.8   # AttributeError!

# __slots__ 的好处：节省内存（不用 __dict__）
print(hasattr(p, '__dict__'))    # False（有 __slots__ 就没有 __dict__）
print(hasattr(s, '__dict__'))    # True（普通类有 __dict__）
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- 没有 `__slots__` 时，Python 用 `__dict__` 存实例属性，可以随便加
- `__slots__` 是个元组，列出允许绑定的属性名
- `__slots__` 只对当前类有效，子类不受限（除非子类也定义）
- 子类和父类都有 `__slots__` 时，允许的属性是两者的并集
- `__slots__` 的真正好处是节省内存：不用 `__dict__`，适合创建大量实例

## 🏃 跑一下试试

```bash
cd 34-slots
python slots.py
```

## 💡 师兄的碎碎念

- 没有 `__slots__` 时，Python 用 `__dict__` 存实例属性，可以随便加
- `__slots__` 是个元组，列出允许绑定的属性名
- `__slots__` 只对当前类有效，子类不受限（除非子类也定义）
- 子类和父类都有 `__slots__` 时，允许的属性是两者的并集
- `__slots__` 的真正好处是节省内存：不用 `__dict__`，适合创建大量实例

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `__slots__ = ('name', 'age')` | 限制实例只能绑定指定属性 |
| `动态绑定` | Python 默认允许给实例绑定任意属性 |
| `MethodType` | 给单个实例绑定方法 |
| `__dict__` | 存储实例属性的字典，有 __slots__ 时不存在 |
| `子类继承` | __slots__ 不会被子类继承 |

## ➡️ 下一关

下一关我们学习 [@property](../35-property/README.md)，继续加油！
