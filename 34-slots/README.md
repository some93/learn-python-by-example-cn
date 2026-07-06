# 第 34 关：__slots__（师兄带你学 Python）

## 🎯 这一关你会学到

- Python 默认为什么可以动态绑定属性
- `__slots__` 如何限制实例能绑定哪些属性
- `__dict__` 和实例属性存储的关系
- `__slots__` 对子类为什么默认不起作用
- `__slots__` 的主要价值：约束属性和节省大量实例的内存

## 🤔 先想一个问题

你开了个快递柜，本来每个格子都能乱塞东西。有人放快递，有人放自行车，还有人塞了一把椅子。

你决定给柜子加规则：这个格子只能放“姓名”和“年龄”，别的都不许塞。

Python 的 `__slots__` 就像这个格子限制：**提前声明实例允许有哪些属性**。

## 📖 看代码

```python
# __slots__

from types import MethodType


print("=== 普通类可以动态绑定属性 ===")


class Student:
    # 不定义 __slots__ 的普通类，实例会有 __dict__ 保存动态属性。
    pass


student = Student()
# 普通实例可以在运行时新增任意属性。
student.name = "Alice"
student.age = 18
print(student.name, student.age)
print(hasattr(student, "__dict__"))


print("\n=== 普通实例还能动态绑定方法 ===")


def set_score(self, score):
    self.score = score


# MethodType 可以把函数绑定成某个实例的方法。
student.set_score = MethodType(set_score, student)
student.set_score(99)
print(student.score)


print("\n=== __slots__ 限制实例属性 ===")


class Person:
    # __slots__ 限制实例只能拥有这些属性，并且通常不再生成 __dict__。
    __slots__ = ("name", "age")


person = Person()
person.name = "Bob"
person.age = 25
print(person.name, person.age)
print(hasattr(person, "__dict__"))

try:
    # score 不在 __slots__ 里，所以不能动态新增。
    person.score = 99
except AttributeError as error:
    print(type(error).__name__)


print("\n=== __slots__ 默认不限制子类 ===")


class GraduateStudent(Person):
    # 子类没有定义 __slots__ 时，会重新拥有 __dict__。
    pass


graduate = GraduateStudent()
graduate.name = "Charlie"
graduate.score = 100
print(graduate.name, graduate.score)
print(hasattr(graduate, "__dict__"))


print("\n=== 子类也定义 __slots__ ===")


class UnderGrad(Person):
    # 子类也定义 __slots__，才能继续限制新增属性。
    __slots__ = ("score",)


under_grad = UnderGrad()
under_grad.name = "Dave"
under_grad.age = 20
under_grad.score = 88
print(under_grad.name, under_grad.age, under_grad.score)
print(hasattr(under_grad, "__dict__"))

try:
    under_grad.gpa = 3.8
except AttributeError as error:
    print(type(error).__name__)
```

## 🔍 师兄给你逐行拆

### 普通类为什么能随便加属性？

```python
class Student:
    pass


student = Student()
student.name = "Alice"
student.age = 18
print(hasattr(student, "__dict__"))
```

**这行在干嘛？**

普通 Python 实例通常有一个 `__dict__`，用字典保存实例属性。

你写：

```python
student.name = "Alice"
```

本质上就是往这个实例的属性字典里塞一个键值对。

**为什么灵活也危险？**

灵活意味着你可以随手加属性；危险也在这里：写错属性名时，Python 可能不会报错，而是悄悄创建了一个新属性。

---

### 动态绑定方法

```python
def set_score(self, score):
    self.score = score


student.set_score = MethodType(set_score, student)
student.set_score(99)
```

**这行在干嘛？**

`MethodType` 可以把一个函数绑定到某个实例上，让它变成这个实例的方法。

这里只给 `student` 这个实例绑定了 `set_score()`，不是给所有 `Student` 实例绑定。

**现实提醒**

这展示了 Python 的动态能力，但真实业务里不建议频繁这么干。对象结构太动态，代码会变难维护。

---

### `__slots__` 限制属性

```python
class Person:
    __slots__ = ("name", "age")
```

**这行在干嘛？**

`__slots__` 声明 `Person` 实例只允许绑定 `name` 和 `age`。

所以这些可以：

```python
person.name = "Bob"
person.age = 25
```

但这个不行：

```python
person.score = 99
```

会抛出 `AttributeError`。

**为什么 `hasattr(person, "__dict__")` 是 False？**

定义 `__slots__` 后，实例默认不再用普通 `__dict__` 存属性，而是用固定槽位保存。这样能节省内存，尤其是创建几十万、几百万个对象时。

---

### `__slots__` 默认不限制子类

```python
class GraduateStudent(Person):
    pass


graduate = GraduateStudent()
graduate.score = 100
print(hasattr(graduate, "__dict__"))
```

**这行在干嘛？**

虽然 `Person` 定义了 `__slots__`，但子类 `GraduateStudent` 没有定义 `__slots__`，所以子类实例又会拥有自己的 `__dict__`。

因此 `graduate.score = 100` 可以成功。

**容易踩的坑**

很多人以为父类定义了 `__slots__`，所有子类都会被限制。不是。子类如果也要限制，必须自己也定义 `__slots__`。

---

### 子类也定义 `__slots__`

```python
class UnderGrad(Person):
    __slots__ = ("score",)
```

**这行在干嘛？**

`UnderGrad` 的实例允许使用父类槽位 `name`、`age`，再加上自己的槽位 `score`。

所以：

```python
under_grad.name = "Dave"
under_grad.age = 20
under_grad.score = 88
```

都可以。

但：

```python
under_grad.gpa = 3.8
```

会抛出 `AttributeError`。

**小细节**

`__slots__ = ("score",)` 里的逗号不能漏。单元素元组必须写逗号，否则它只是一个字符串。

## 🏃 跑一下试试

```bash
$ python slots.py
=== 普通类可以动态绑定属性 ===
Alice 18
True

=== 普通实例还能动态绑定方法 ===
99

=== __slots__ 限制实例属性 ===
Bob 25
False
AttributeError

=== __slots__ 默认不限制子类 ===
Charlie 100
True

=== 子类也定义 __slots__ ===
Dave 20 88
False
AttributeError
```

## 💡 师兄的碎碎念

- 普通实例通常有 `__dict__`，所以能动态增加属性。
- `__slots__` 声明允许的属性名，超出范围会 `AttributeError`。
- `__slots__` 主要用于属性约束和内存优化，不是安全机制。
- 父类的 `__slots__` 不会自动限制没有定义 `__slots__` 的子类。
- 只有创建大量小对象时，`__slots__` 的内存优化才特别值得考虑；普通业务类别急着上。

## 🎓 这一关的知识点清单

- **动态绑定属性**：普通对象可以运行时新增属性。
- **__dict__**：普通实例保存属性的字典。
- **__slots__**：声明实例允许绑定的属性名。
- **AttributeError**：给 slots 对象绑定未声明属性时抛出的错误。
- **子类行为**：子类不定义 `__slots__` 时会重新拥有 `__dict__`。
- **内存优化**：`__slots__` 可减少大量实例的属性存储开销。

## ➡️ 下一关

`__slots__` 能限制属性名，但不能优雅地校验属性值。下一关看 `@property`：像访问属性一样调用方法，顺手加上校验逻辑 👉 [下一关：@property →](../35-property/)


