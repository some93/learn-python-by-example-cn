# 第 35 关：@property（师兄带你学 Python）

## 🎯 这一关你会学到

- 直接暴露属性为什么容易失控
- `@property` 如何把方法包装成属性读取
- `@xxx.setter` 如何拦截属性赋值并做校验
- 只读属性如何实现
- 计算属性如何像普通属性一样使用

## 🤔 先想一个问题

你在网上买东西，评分只能打 0 到 100 分。但如果系统没做检查，有人直接填了 9999 分怎么办？

你希望代码写起来像普通赋值：

```python
student.score = 90
```

但背后又能自动检查范围。`@property` 就是这个工具：**外表像属性，里面是方法**。

## 📖 看代码

```python
# @property


print("=== 直接暴露属性的问题 ===")


class BadStudent:
    pass


bad = BadStudent()
# 直接暴露属性时，外部可以写入明显不合理的值。
bad.score = 9999
print(bad.score)  # 9999


print("\n=== 老式 getter/setter ===")


class OldStudent:
    def get_score(self):
        return self._score

    def set_score(self, value):
        # getter/setter 可以校验数据，但调用方式比较啰嗦。
        if not isinstance(value, int):
            raise ValueError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在 0-100 之间")
        self._score = value


old = OldStudent()
old.set_score(88)
print(old.get_score())  # 88


print("\n=== @property 读写属性 ===")


class Student:
    @property
    def score(self):
        # @property 让方法像属性一样读取。
        return self._score

    @score.setter
    def score(self, value):
        # setter 保留校验能力，同时调用方式变成 student.score = ...
        if not isinstance(value, int):
            raise ValueError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在 0-100 之间")
        self._score = value


student = Student()
student.score = 90
print(student.score)  # 90

try:
    student.score = 120
except ValueError as error:
    print(error)  # 分数必须在 0-100 之间


print("\n=== 只读属性和计算属性 ===")


class Person:
    def __init__(self, birth_year, current_year):
        self._birth_year = birth_year
        self._current_year = current_year

    @property
    def birth_year(self):
        # 只定义 getter，没有 setter，就是只读属性。
        return self._birth_year

    @property
    def age(self):
        # 计算属性不一定需要真实存储在对象里。
        return self._current_year - self._birth_year


person = Person(2000, 2026)
print(person.birth_year)  # 2000
print(person.age)  # 26

try:
    person.age = 30
except AttributeError as error:
    print(type(error).__name__)  # AttributeError
```

## 🔍 师兄给你逐行拆

### 直接暴露属性的问题

```python
class BadStudent:
    pass


bad = BadStudent()
bad.score = 9999
print(bad.score)
```

**这行在干嘛？**

`BadStudent` 没有任何限制，外部可以随便给它绑定 `score`。分数设成 `9999`，Python 也不会拦你。

**为什么这不行？**

对象的数据如果没有入口校验，很容易进入非法状态。后面的代码再基于这个分数做排名、评级、统计，结果都会错。

---

### 老式 getter/setter 能校验，但不够顺手

```python
class OldStudent:
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在 0-100 之间")
        self._score = value
```

**这行在干嘛？**

`set_score()` 负责写入分数，并检查类型和范围。`get_score()` 负责读取分数。

**有什么问题？**

调用起来不够像 Python：

```python
old.set_score(88)
old.get_score()
```

Python 更希望写成属性访问：

```python
student.score = 88
student.score
```

---

### `@property` —— 把方法变成属性读取

```python
class Student:
    @property
    def score(self):
        return self._score
```

**这行在干嘛？**

`@property` 把 `score()` 方法包装成一个可读属性。外部可以写：

```python
student.score
```

但实际执行的是 `score(self)` 这个方法。

**为什么内部叫 `_score`？**

如果 getter 也叫 `score`，真实存储值就不能再叫 `self.score`，否则会递归调用 property 自己。

所以常见写法是：

```python
self._score
```

单下划线表示内部使用。

---

### `@score.setter` —— 拦截属性赋值

```python
@score.setter
def score(self, value):
    if not isinstance(value, int):
        raise ValueError("分数必须是整数")
    if value < 0 or value > 100:
        raise ValueError("分数必须在 0-100 之间")
    self._score = value
```

**这行在干嘛？**

`@score.setter` 定义写入逻辑。外部执行：

```python
student.score = 90
```

实际会调用这个 setter 方法，并把 `90` 作为 `value` 传进来。

如果值不合法，就抛 `ValueError`。

**生活类比**

你看起来是在往表格里填分数，但系统背后有门禁：不是整数不让进，超过 100 不让进。

---

### 只读属性：不写 setter 就行

```python
class Person:
    @property
    def birth_year(self):
        return self._birth_year
```

**这行在干嘛？**

`birth_year` 只有 getter，没有 setter，所以外部能读：

```python
person.birth_year
```

但不能写：

```python
person.birth_year = 1999
```

否则会抛 `AttributeError`。

---

### 计算属性：每次读取时动态计算

```python
@property
def age(self):
    return self._current_year - self._birth_year
```

**这行在干嘛？**

`age` 没有单独存储，而是根据 `birth_year` 和 `current_year` 计算出来。

外部使用时像普通属性：

```python
person.age
```

但背后每次都会执行计算逻辑。

**为什么示例传 `current_year=2026`？**

为了让教程输出稳定。如果直接取系统当前年份，明年运行结果就变了。

## 🏃 跑一下试试

```bash
$ python property.py
=== 直接暴露属性的问题 ===
9999

=== 老式 getter/setter ===
88

=== @property 读写属性 ===
90
分数必须在 0-100 之间

=== 只读属性和计算属性 ===
2000
26
AttributeError
```

## 💡 师兄的碎碎念

- `@property` 定义 getter，让方法像属性一样读取。
- `@xxx.setter` 定义 setter，让属性赋值时自动执行校验逻辑。
- 只定义 getter、不定义 setter，就是只读属性。
- 内部真实数据通常用 `_xxx` 保存，避免和 property 名字冲突。
- `@property` 适合“看起来是属性，但读取或写入时需要逻辑”的场景。

## 🎓 这一关的知识点清单

- **@property**：把方法变成属性读取入口。
- **@xxx.setter**：定义属性写入入口。
- **只读属性**：只有 getter，没有 setter。
- **计算属性**：不直接存值，而是读取时动态计算。
- **内部属性**：常用 `_xxx` 保存真实值，表示内部使用。
- **属性校验**：在 setter 里检查类型、范围和业务规则。

## ➡️ 下一关

`@property` 解决属性读写控制。下一关看多重继承：一个类同时继承多个父类时，Python 怎么决定先用谁的方法 👉 [下一关：多重继承 →](../36-multiple-inheritance/)




