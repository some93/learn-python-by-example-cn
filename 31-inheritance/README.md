# 第 31 关：继承和多态

## 🎯 这一关你会学到

- `class Dog(Animal)` 的继承语法
- 子类如何重写父类方法
- `super()` 如何调用父类初始化逻辑
- `isinstance()` 和 `issubclass()` 如何判断继承关系
- 多态和鸭子类型在 Python 里的意义

## 🤔 先想一个问题

你开了一家宠物店，有狗、猫、乌龟。它们都是动物，都有名字，也都会“动起来”，但动的方式不同。

如果每种动物都从零写一遍，会很重复。更自然的做法是先定义一个通用的 `Animal`，再让 `Dog`、`Cat`、`Tortoise` 继承它，各自改写自己的行为。

这就是继承和多态：**共用一套基础能力，同时允许不同子类表现出不同动作**。

## 📖 看代码

```python
# 继承和多态


print("=== 继承和方法重写 ===")


class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        # 父类提供通用行为，子类可以继承或重写。
        print(f"{self.name} is running...")


class Dog(Animal):
    def run(self):
        # 子类定义同名方法，会覆盖父类方法。
        print(f"{self.name} is running fast...")


class Cat(Animal):
    def run(self):
        print(f"{self.name} is walking quietly...")


dog = Dog("旺财")
cat = Cat("咪咪")
dog.run()  # 旺财 is running fast...
cat.run()  # 咪咪 is walking quietly...


print("\n=== super() 调用父类方法 ===")


class Tortoise(Animal):
    def __init__(self, name, speed):
        # super() 调用父类 __init__，避免重复初始化 name。
        super().__init__(name)
        self.speed = speed

    def run(self):
        print(f"{self.name} is running slowly at {self.speed} m/s...")


tortoise = Tortoise("龟仙人", 0.2)
tortoise.run()  # 龟仙人 is running slowly at 0.2 m/s...


print("\n=== isinstance 和 issubclass ===")

# 子类实例同时也是父类实例。
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, Cat))  # False
print(issubclass(Dog, Animal))  # True
print(issubclass(Dog, object))  # True


print("\n=== 多态 ===")


def run_twice(animal):
    # 只关心对象有没有 run()，不关心它具体是什么类。
    animal.run()
    animal.run()


run_twice(Dog("小黑"))  # 小黑 is running fast... / 小黑 is running fast...
run_twice(Cat("小花"))  # 小花 is walking quietly... / 小花 is walking quietly...
run_twice(Tortoise("慢慢", 0.1))  # 慢慢 is running slowly at 0.1 m/s... / 慢慢 is running slowly at 0.1 m/s...


print("\n=== 鸭子类型 ===")


class Timer:
    def run(self):
        # Timer 没有继承 Animal，但有 run()，也能被 run_twice 使用。
        print("Timer is ticking...")


run_twice(Timer())  # Timer is ticking... / Timer is ticking...
```

## 🔍 师兄给你逐行拆

### `class Dog(Animal)` —— 子类继承父类

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} is running...")


class Dog(Animal):
    def run(self):
        print(f"{self.name} is running fast...")
```

**这行在干嘛？**

`Animal` 是父类，也叫基类。`Dog(Animal)` 表示 `Dog` 继承 `Animal`。

`Dog` 没有自己写 `__init__()`，所以会继承 `Animal.__init__()`。因此你可以写：

```python
dog = Dog("旺财")
```

`旺财` 会被保存到 `self.name`。

**为什么要继承？**

因为 `name` 这种通用属性，动物都有。放在父类里，子类就不用重复写。

---

### 方法重写：同名方法，子类说了算

```python
class Dog(Animal):
    def run(self):
        print(f"{self.name} is running fast...")


class Cat(Animal):
    def run(self):
        print(f"{self.name} is walking quietly...")
```

**这行在干嘛？**

`Animal` 里已经有 `run()`，但 `Dog` 和 `Cat` 又定义了自己的 `run()`。这叫方法重写，也叫 override。

调用：

```python
dog.run()
cat.run()
```

Python 会优先找子类自己的方法，所以狗和猫的输出不同。

**生活类比**

父类规定“动物会移动”，但狗说“我跑得快”，猫说“我走得轻”。动作名都叫 `run()`，具体表现由子类决定。

---

### `super()` —— 复用父类初始化

```python
class Tortoise(Animal):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed
```

**这行在干嘛？**

`Tortoise` 需要 `name`，还额外需要 `speed`。名字初始化逻辑父类已经写好了，所以用：

```python
super().__init__(name)
```

调用父类的 `__init__()`，再给自己增加 `speed`。

**为什么不用手写 `self.name = name`？**

简单例子里手写也行，但真实父类初始化可能做很多事。用 `super()` 能复用父类逻辑，减少重复，也方便父类以后修改。

---

### `isinstance()` 和 `issubclass()`

```python
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(issubclass(Dog, Animal))
print(issubclass(Dog, object))
```

**这行在干嘛？**

`isinstance(dog, Dog)` 是 `True`，因为 `dog` 是 `Dog` 实例。

`isinstance(dog, Animal)` 也是 `True`，因为 `Dog` 继承自 `Animal`。

`isinstance(dog, Cat)` 是 `False`，狗不是猫。

`issubclass(Dog, Animal)` 判断类和类之间的继承关系。

`issubclass(Dog, object)` 是 `True`，因为 Python 3 里所有类最终都继承自 `object`。

---

### 多态：同一个调用，不同表现

```python
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog("小黑"))
run_twice(Cat("小花"))
run_twice(Tortoise("慢慢", 0.1))
```

**这行在干嘛？**

`run_twice()` 不关心传进来的是狗、猫还是乌龟，只要求它有 `run()` 方法。

同样调用 `animal.run()`，不同对象执行不同版本的 `run()`。这就是多态。

**多态有什么好处？**

新增一个子类，比如 `Tortoise`，不用改 `run_twice()`。只要新类提供 `run()`，原来的通用函数就能继续用。

这就是“对扩展开放，对修改关闭”的味道。

---

### 鸭子类型：不继承也能用

```python
class Timer:
    def run(self):
        print("Timer is ticking...")


run_twice(Timer())
```

**这行在干嘛？**

`Timer` 没有继承 `Animal`，但它有 `run()` 方法，所以 `run_twice(Timer())` 也能正常执行。

**为什么？**

Python 更看重对象“能不能做这件事”，而不是“你是不是某个类型”。

这就是鸭子类型：如果一个东西走起来像鸭子、叫起来像鸭子，那就先当鸭子用。

**容易踩的坑**

鸭子类型很灵活，但也要求你写清楚函数期待的对象协议。比如 `run_twice()` 期待传入对象有 `run()` 方法。如果没有，就会在运行时报 `AttributeError`。

## 🏃 跑一下试试

```bash
$ python inheritance.py
=== 继承和方法重写 ===
旺财 is running fast...
咪咪 is walking quietly...

=== super() 调用父类方法 ===
龟仙人 is running slowly at 0.2 m/s...

=== isinstance 和 issubclass ===
True
True
False
True
True

=== 多态 ===
小黑 is running fast...
小黑 is running fast...
小花 is walking quietly...
小花 is walking quietly...
慢慢 is running slowly at 0.1 m/s...
慢慢 is running slowly at 0.1 m/s...

=== 鸭子类型 ===
Timer is ticking...
Timer is ticking...
```

## 💡 师兄的碎碎念

- 继承适合表达“is-a”关系：Dog is an Animal。
- 子类可以继承父类属性和方法，也可以重写父类方法。
- 子类扩展父类初始化时，常用 `super().__init__(...)` 复用父类逻辑。
- `isinstance()` 会考虑继承链，`type(obj) is Class` 只判断精确类型。
- Python 的多态常常和鸭子类型一起出现：不强制继承，只关心对象有没有需要的方法。

## 🎓 这一关的知识点清单

- **继承**：`class Dog(Animal)` 表示 Dog 继承 Animal。
- **父类/子类**：父类提供通用能力，子类复用并扩展。
- **方法重写**：子类定义和父类同名的方法，调用时优先使用子类版本。
- **super()**：调用父类方法，常用于子类初始化时复用父类逻辑。
- **多态**：同一个方法调用，在不同对象上表现出不同行为。
- **鸭子类型**：不要求继承某个类，只要对象提供所需方法即可。

## ➡️ 下一关

继承和多态搞定后，下一关看看 Python 如何检查对象：类型、属性、方法，以及 `dir()`、`getattr()` 这些工具 👉 [下一关：获取对象信息 →](../32-object-info/)


