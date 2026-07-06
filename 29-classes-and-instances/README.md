# 第 29 关：类和实例（师兄带你学 Python）

## 🎯 这一关你会学到

- `class` 如何定义类
- `__init__()` 如何初始化实例属性
- `self` 到底代表谁
- 实例属性、类属性和方法的关系
- Python 可以动态给实例绑定属性，但不建议滥用

## 🤔 先想一个问题

类像奶茶店的配方单：一杯奶茶需要茶底、奶、糖、配料。

实例就是按这张配方单做出来的一杯具体奶茶。Bart 这杯可能 59 分，Lisa 这杯可能 87 分。它们都是 `Student`，但各自有不同的数据。

面向对象的核心就是：**把数据和操作数据的方法放在一起**。

## 📖 看代码

```python
# 类和实例


print("=== 定义类和创建实例 ===")


class Student:
    # class 内、方法外定义的是类属性，所有实例默认共享。
    school = "Springfield School"

    def __init__(self, name, score):
        # self 指向当前实例，这里给每个学生保存自己的数据。
        self.name = name
        self.score = score

    def print_score(self):
        print(f"{self.name}: {self.score}")

    def get_grade(self):
        # 方法可以直接读取实例属性，封装和学生相关的业务逻辑。
        if self.score >= 90:
            return "A"
        if self.score >= 60:
            return "B"
        return "C"

    def update_score(self, score):
        self.score = score


bart = Student("Bart Simpson", 59)
lisa = Student("Lisa Simpson", 87)

# 调用实例方法时，Python 会自动把实例作为 self 传进去。
bart.print_score()
lisa.print_score()
print(f"{bart.name} 的等级: {bart.get_grade()}")
print(f"{lisa.name} 的等级: {lisa.get_grade()}")


print("\n=== self 是实例自身 ===")

# 下面这行等价于 bart.print_score()，只是手动把 bart 传给 self。
Student.print_score(bart)
bart.update_score(75)
bart.print_score()
print(bart.get_grade())


print("\n=== 实例属性和类属性 ===")

print(bart.name)
# 实例找不到 school 时，会继续去类上找。
print(bart.school)
print(lisa.school)

# 修改类属性会影响还没有被实例属性遮蔽的所有实例。
Student.school = "Python School"
print(bart.school)
print(lisa.school)


print("\n=== 动态绑定实例属性 ===")

# Python 普通类的实例默认可以随时新增属性。
bart.age = 10
print(bart.age)
print(hasattr(lisa, "age"))


print("\n=== 类型判断 ===")

print(type(bart).__name__)
print(isinstance(bart, Student))
```

## 🔍 师兄给你逐行拆

### `class Student` —— 定义一个类

```python
class Student:
    school = "Springfield School"
```

**这行在干嘛？**

`class Student:` 定义了一个学生类。类名通常用大驼峰命名法，也就是 `Student`、`OrderItem`、`UserProfile` 这种写法。

`school` 写在类里面、方法外面，叫类属性。所有实例默认都能访问它。

**为什么类属性适合放学校名？**

因为这里的学校名对所有学生都一样。共同数据放类属性，每个学生自己的名字和分数放实例属性。

---

### `__init__()` —— 实例初始化

```python
def __init__(self, name, score):
    self.name = name
    self.score = score
```

**这行在干嘛？**

当你写：

```python
bart = Student("Bart Simpson", 59)
```

Python 会创建一个新的 `Student` 实例，然后自动调用 `__init__()`，把 `"Bart Simpson"` 和 `59` 填进去。

`self.name` 和 `self.score` 是实例属性，每个实例都有自己的一份。

**容易踩的坑**

`__init__` 前后是两个下划线，不是 `_init_`，也不是 `init`。写错了 Python 不会自动调用它。

---

### `self` 是谁？

```python
def print_score(self):
    print(f"{self.name}: {self.score}")
```

**这行在干嘛？**

`self` 表示当前实例。谁调用这个方法，`self` 就是谁。

```python
bart.print_score()
```

等价于：

```python
Student.print_score(bart)
```

所以方法定义时第一个参数必须写 `self`，但调用时不需要手动传。

**生活类比**

`print_score()` 像学生证打印机。Bart 来打印，就打印 Bart 的名字和分数；Lisa 来打印，就打印 Lisa 的。

---

### 方法：把行为放进类里

```python
def get_grade(self):
    if self.score >= 90:
        return "A"
    if self.score >= 60:
        return "B"
    return "C"
```

**这行在干嘛？**

`get_grade()` 根据当前实例的 `score` 返回等级。它不是孤零零地处理一个数字，而是和学生对象绑定在一起。

**为什么这是面向对象？**

因为数据和行为放在一起：

- 数据：`name`、`score`
- 行为：`print_score()`、`get_grade()`、`update_score()`

这样调用时更像一句自然语言：

```python
bart.get_grade()
```

---

### 实例属性和类属性

```python
print(bart.name)
print(bart.school)
print(lisa.school)
Student.school = "Python School"
print(bart.school)
print(lisa.school)
```

**这行在干嘛？**

`bart.name` 是实例属性，只属于 Bart。

`school` 是类属性，Bart 和 Lisa 默认都从 `Student` 类上读取它。修改 `Student.school` 后，两个实例看到的学校名都会变。

**容易踩的坑**

如果你写：

```python
bart.school = "Bart School"
```

这会给 Bart 单独创建一个实例属性 `school`，遮住类属性。第 33 关会专门讲实例属性和类属性的细节。

---

### 动态绑定属性

```python
bart.age = 10
print(bart.age)
print(hasattr(lisa, "age"))
```

**这行在干嘛？**

Python 允许你在实例创建之后，随手给它加新属性。Bart 多了一个 `age`，但 Lisa 没有。

**为什么不建议滥用？**

太自由会让对象结构变乱。今天某些学生有 `age`，某些没有，后面代码一访问就可能报错。

如果一个属性是学生对象稳定需要的，最好在 `__init__()` 里统一定义。

---

### 类型判断

```python
print(type(bart).__name__)
print(isinstance(bart, Student))
```

**这行在干嘛？**

`type(bart).__name__` 可以看到实例的类型名是 `Student`。

`isinstance(bart, Student)` 判断 Bart 是不是 `Student` 类的实例，结果是 `True`。

## 🏃 跑一下试试

```bash
$ python classes-and-instances.py
=== 定义类和创建实例 ===
Bart Simpson: 59
Lisa Simpson: 87
Bart Simpson 的等级: C
Lisa Simpson 的等级: B

=== self 是实例自身 ===
Bart Simpson: 59
Bart Simpson: 75
B

=== 实例属性和类属性 ===
Bart Simpson
Springfield School
Springfield School
Python School
Python School

=== 动态绑定实例属性 ===
10
False

=== 类型判断 ===
Student
True
```

## 💡 师兄的碎碎念

- 类名通常用大驼峰，函数和变量通常用小写下划线。
- `__init__()` 负责初始化实例，不负责创建实例本身。
- 方法第一个参数约定写 `self`，表示当前实例。
- 实例属性放每个对象自己的数据，类属性放所有对象共享的数据。
- Python 能动态加属性，但教程后面会讲 `__slots__` 和 `@property` 来约束对象结构。

## 🎓 这一关的知识点清单

- **class**：定义类，类是创建对象的模板。
- **实例**：根据类创建出来的具体对象。
- **__init__()**：初始化实例属性的特殊方法。
- **self**：当前实例，方法调用时由 Python 自动传入。
- **实例属性**：绑定在某个实例上的数据，比如 `self.name`。
- **类属性**：绑定在类上的数据，被所有实例共享。
- **方法**：定义在类里的函数，用来操作实例数据。

## ➡️ 下一关

类和实例搞定后，下一关看访问限制：如何把对象内部数据藏起来，通过方法控制读写 👉 [下一关：访问限制 →](../30-access-restriction/)


