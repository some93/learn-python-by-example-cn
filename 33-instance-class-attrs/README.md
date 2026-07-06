# 第 33 关：实例属性和类属性（师兄带你学 Python）

## 🎯 这一关你会学到

- 实例属性和类属性的定义位置
- 属性查找顺序：先实例，再类
- 实例属性如何遮蔽同名类属性
- 如何用类属性做共享计数器
- 可变类属性为什么容易造成共享数据坑

## 🤔 先想一个问题

班级里每个同学有自己的名字，这应该是个人信息。

但大家共享同一个学校名称，这更像班级统一信息。

如果某个同学转学了，是只改他一个人的学校，还是全班都换学校？这个问题对应到 Python，就是实例属性和类属性的区别。

## 📖 看代码

```python
# 实例属性和类属性


print("=== 类属性和实例属性 ===")


class Student:
    # 类属性属于类对象，实例没有同名属性时会读到它。
    school = "清华大学"

    def __init__(self, name):
        # 实例属性属于某个具体对象。
        self.name = name


s1 = Student("Alice")
s2 = Student("Bob")

print(Student.school)
print(s1.school)
print(s2.school)
print(s1.name)
print(s2.name)


print("\n=== 实例属性遮蔽类属性 ===")

# 给 s1 绑定同名实例属性后，s1.school 会优先读实例自己的值。
s1.school = "北京大学"
print(s1.school)
print(s2.school)
print(Student.school)
print("school" in s1.__dict__)
print("school" in s2.__dict__)

# 删除实例属性后，再次读取会回到类属性。
del s1.school
print(s1.school)


print("\n=== 修改类属性 ===")

# 修改类属性会影响所有没有同名实例属性的对象。
Student.school = "Python 大学"
print(s1.school)
print(s2.school)
print(Student.school)


print("\n=== 类属性计数器 ===")


class Counter:
    count = 0

    def __init__(self):
        # 用类名访问类属性，表达“所有实例共享一个计数器”。
        Counter.count += 1


Counter()
Counter()
Counter()
print(Counter.count)


print("\n=== 可变类属性的坑 ===")


class BadBag:
    # 可变类属性会被所有实例共享，容易造成数据串在一起。
    items = []

    def add(self, item):
        self.items.append(item)


bag1 = BadBag()
bag2 = BadBag()
bag1.add("苹果")
bag2.add("香蕉")
print(bag1.items)
print(bag2.items)
print(bag1.items is bag2.items)


print("\n=== 正确做法：可变数据放实例属性 ===")


class GoodBag:
    def __init__(self):
        # 每个实例都创建自己的列表，互不影响。
        self.items = []

    def add(self, item):
        self.items.append(item)


good1 = GoodBag()
good2 = GoodBag()
good1.add("苹果")
good2.add("香蕉")
print(good1.items)
print(good2.items)
print(good1.items is good2.items)
```

## 🔍 师兄给你逐行拆

### 类属性：写在类里，方法外

```python
class Student:
    school = "清华大学"

    def __init__(self, name):
        self.name = name
```

**这行在干嘛？**

`school` 写在类里、方法外，是类属性。它属于 `Student` 类。

`self.name` 写在 `__init__()` 里，是实例属性。每个学生实例都有自己的 `name`。

**怎么访问？**

类属性可以通过类访问：

```python
Student.school
```

也可以通过实例访问：

```python
s1.school
```

如果实例自己没有 `school`，Python 会去类上找。

---

### 属性查找顺序：实例优先

```python
s1.school = "北京大学"
print(s1.school)
print(s2.school)
print(Student.school)
```

**这行在干嘛？**

`s1.school = "北京大学"` 不是修改类属性，而是给 `s1` 新增了一个实例属性 `school`。

所以：

- `s1.school` 先找到实例自己的 `school`，输出 `北京大学`；
- `s2.school` 自己没有 `school`，去类上找，输出 `清华大学`；
- `Student.school` 还是 `清华大学`。

**为什么叫遮蔽？**

因为 `s1` 自己的 `school` 把类上的 `school` 挡住了。类属性还在，只是对 `s1.school` 这个访问路径不可见了。

---

### `__dict__` 看实例自己的属性

```python
print("school" in s1.__dict__)
print("school" in s2.__dict__)
```

**这行在干嘛？**

`__dict__` 可以看到实例自己身上的属性。

给 `s1.school` 赋值后，`s1.__dict__` 里有 `school`；`s2` 没有。

删除它：

```python
del s1.school
```

再访问 `s1.school`，Python 又会回到类上找 `Student.school`。

---

### 修改类属性要通过类名

```python
Student.school = "Python 大学"
print(s1.school)
print(s2.school)
print(Student.school)
```

**这行在干嘛？**

这次是直接修改类属性。所有没有自己 `school` 实例属性的学生，都会看到新的学校名。

**容易踩的坑**

如果你在实例方法里想修改共享类属性，优先写：

```python
Student.school = "Python 大学"
```

而不是：

```python
self.school = "Python 大学"
```

后者很可能只是给当前实例新增同名属性。

---

### 类属性做计数器

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
```

**这行在干嘛？**

`count` 是类属性，所有实例共享。每创建一个 `Counter()`，`Counter.count` 就加一。

创建三次后：

```python
Counter.count == 3
```

**为什么用 `Counter.count`，不用 `self.count`？**

因为我们要修改的是类属性，不是某个实例自己的属性。

---

### 可变类属性的坑

```python
class BadBag:
    items = []

    def add(self, item):
        self.items.append(item)
```

**这行在干嘛？**

`items` 是类属性，而且是一个列表。`bag1` 和 `bag2` 访问到的是同一个列表。

所以：

```python
bag1.add("苹果")
bag2.add("香蕉")
```

最后两个包里都会看到：

```python
['苹果', '香蕉']
```

**为什么？**

`self.items.append(...)` 没有给实例创建新属性，而是在修改类属性指向的同一个列表。

**正确做法**

每个实例都应该有自己的列表：

```python
class GoodBag:
    def __init__(self):
        self.items = []
```

这样 `good1.items` 和 `good2.items` 才是两个不同列表。

## 🏃 跑一下试试

```bash
$ python instance-class-attrs.py
=== 类属性和实例属性 ===
清华大学
清华大学
清华大学
Alice
Bob

=== 实例属性遮蔽类属性 ===
北京大学
清华大学
清华大学
True
False
清华大学

=== 修改类属性 ===
Python 大学
Python 大学
Python 大学

=== 类属性计数器 ===
3

=== 可变类属性的坑 ===
['苹果', '香蕉']
['苹果', '香蕉']
True

=== 正确做法：可变数据放实例属性 ===
['苹果']
['香蕉']
False
```

## 💡 师兄的碎碎念

- 类属性适合放所有实例共享的数据，比如配置、计数器、常量。
- 实例属性适合放每个对象独有的数据，比如姓名、分数、购物车列表。
- 属性查找顺序是：实例自身 -> 类 -> 父类。
- 给实例赋值同名属性会遮蔽类属性，不会修改类属性。
- 可变数据通常不要做类属性，除非你明确就是想让所有实例共享它。

## 🎓 这一关的知识点清单

- **类属性**：定义在类中、方法外，默认被所有实例共享。
- **实例属性**：绑定在具体实例上，每个实例独立。
- **属性查找顺序**：访问 `obj.attr` 时，先找实例，再找类。
- **遮蔽效果**：实例属性和类属性同名时，实例属性优先。
- **类属性计数器**：用 `ClassName.attr` 修改共享状态。
- **可变类属性坑**：列表、字典作为类属性时会被实例共享。

## ➡️ 下一关

属性能随便加虽然灵活，但有时也会失控。下一关看 `__slots__`：如何限制实例能绑定哪些属性 👉 [下一关：__slots__ →](../34-slots/)


