# 第 36 关：多重继承（师兄带你学 Python）

## 🎯 这一关你会学到

- `class A(B, C)` 的多重继承语法
- Mixin 如何把小功能组合到类上
- MRO（方法解析顺序）如何决定同名方法用谁
- 为什么继承顺序会影响行为
- 什么时候适合用多重继承，什么时候应该谨慎

## 🤔 先想一个问题

你做一个游戏角色系统：有些角色会跑，有些会飞，有些会游泳。

鸭子既会飞又会游泳。如果只靠单继承，你可能要设计一堆奇怪的父类：`FlyingSwimmingBird`、`RunningSwimmingAnimal`，越写越乱。

Mixin 的思路是：把“会飞”“会游泳”做成小功能模块，需要什么就混入什么。

## 📖 看代码

```python
# 多重继承


print("=== Mixin 组合能力 ===")


class Animal:
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixin:
    def run(self):
        # Mixin 通常只提供一小块能力，不负责完整对象建模。
        print(f"{self.__class__.__name__} is running...")


class FlyableMixin:
    def fly(self):
        print(f"{self.__class__.__name__} is flying...")


class SwimmableMixin:
    def swim(self):
        print(f"{self.__class__.__name__} is swimming...")


class Dog(Mammal, RunnableMixin):
    # Dog 是哺乳动物，同时混入“会跑”的能力。
    pass


class Parrot(Bird, FlyableMixin):
    pass


class Duck(Bird, FlyableMixin, SwimmableMixin):
    # Duck 组合了飞行和游泳两个 Mixin。
    pass


Dog().run()
Parrot().fly()
duck = Duck()
duck.fly()
duck.swim()


print("\n=== MRO 方法解析顺序 ===")

# __mro__ 表示方法查找顺序，多重继承时尤其重要。
print([cls.__name__ for cls in Duck.__mro__])


class A:
    def hello(self):
        print("hello from A")


class B(A):
    def hello(self):
        print("hello from B")


class C(A):
    def hello(self):
        print("hello from C")


class D(B, C):
    # D 同时继承 B 和 C，hello 会按 MRO 从左到右查找。
    pass


d = D()
d.hello()
print([cls.__name__ for cls in D.__mro__])


print("\n=== 改变继承顺序会改变查找顺序 ===")


class E(C, B):
    # 继承顺序换了，MRO 也会变化。
    pass


e = E()
e.hello()
print([cls.__name__ for cls in E.__mro__])
```

## 🔍 师兄给你逐行拆

### Mixin：把能力拆成小模块

```python
class RunnableMixin:
    def run(self):
        print(f"{self.__class__.__name__} is running...")


class FlyableMixin:
    def fly(self):
        print(f"{self.__class__.__name__} is flying...")


class SwimmableMixin:
    def swim(self):
        print(f"{self.__class__.__name__} is swimming...")
```

**这行在干嘛？**

这些类不是完整业务对象，而是一小块能力：

- `RunnableMixin` 提供 `run()`；
- `FlyableMixin` 提供 `fly()`；
- `SwimmableMixin` 提供 `swim()`。

**为什么名字带 Mixin？**

这是约定：告诉读代码的人，这个类主要用来“混入能力”，通常不单独实例化。

---

### 多重继承：同时拿到多种能力

```python
class Duck(Bird, FlyableMixin, SwimmableMixin):
    pass
```

**这行在干嘛？**

`Duck` 继承了 `Bird`，同时混入了 `FlyableMixin` 和 `SwimmableMixin`，所以它既有鸟类身份，又能调用 `fly()` 和 `swim()`。

**为什么不把所有方法都写进 Duck？**

因为这些能力可能被很多类复用。比如飞机也会飞，鱼会游泳，狗会跑。Mixin 能避免复制粘贴。

---

### `__mro__` —— Python 到底按什么顺序找方法？

```python
print([cls.__name__ for cls in Duck.__mro__])
```

**这行在干嘛？**

`__mro__` 是 Method Resolution Order，方法解析顺序。它告诉你：当调用 `duck.some_method()` 时，Python 会按什么顺序查找方法。

`Duck` 的 MRO 是：

```python
['Duck', 'Bird', 'Animal', 'FlyableMixin', 'SwimmableMixin', 'object']
```

如果多个父类里有同名方法，MRO 决定谁先被找到。

---

### 同名方法冲突：继承顺序会影响结果

```python
class A:
    def hello(self):
        print("hello from A")


class B(A):
    def hello(self):
        print("hello from B")


class C(A):
    def hello(self):
        print("hello from C")


class D(B, C):
    pass
```

**这行在干嘛？**

`B` 和 `C` 都有 `hello()`。`D(B, C)` 自己没有 `hello()`，所以 Python 按 MRO 查找。

`D` 的 MRO 是：

```python
['D', 'B', 'C', 'A', 'object']
```

所以 `d.hello()` 找到的是 `B.hello()`。

---

### 改变继承顺序，结果也变

```python
class E(C, B):
    pass
```

**这行在干嘛？**

`E(C, B)` 把 `C` 放在 `B` 前面，所以 MRO 变成：

```python
['E', 'C', 'B', 'A', 'object']
```

于是 `e.hello()` 调用的是 `C.hello()`。

**容易踩的坑**

多重继承最怕多个父类提供同名方法，却没有明确设计好谁优先。Mixin 最好提供独立、小而明确的方法，减少冲突。

## 🏃 跑一下试试

```bash
$ python multiple-inheritance.py
=== Mixin 组合能力 ===
Dog is running...
Parrot is flying...
Duck is flying...
Duck is swimming...

=== MRO 方法解析顺序 ===
['Duck', 'Bird', 'Animal', 'FlyableMixin', 'SwimmableMixin', 'object']
hello from B
['D', 'B', 'C', 'A', 'object']

=== 改变继承顺序会改变查找顺序 ===
hello from C
['E', 'C', 'B', 'A', 'object']
```

## 💡 师兄的碎碎念

- 多重继承语法是 `class Child(Parent1, Parent2):`。
- Mixin 应该小而专注，只提供一块能力，不承载复杂继承层级。
- 继承顺序会影响 MRO，从而影响同名方法调用结果。
- Mixin 命名通常以 `Mixin` 结尾，让用途更清楚。
- 如果父类之间关系复杂、状态很多，优先考虑组合而不是多重继承。

## 🎓 这一关的知识点清单

- **多重继承**：一个类同时继承多个父类。
- **Mixin**：用于混入小功能的类，常用于横向能力组合。
- **MRO**：方法解析顺序，决定同名方法查找路径。
- **__mro__**：类的 MRO 元组，可用来调试继承关系。
- **继承顺序**：父类顺序不同，MRO 和行为可能不同。
- **组合优先**：多重继承强大但复杂，复杂业务中常常优先考虑组合。

## ➡️ 下一关

多重继承讲完，下一关看定制类：通过 `__str__`、`__len__`、`__getitem__` 等特殊方法，让你的对象像内置类型一样好用 👉 [下一关：定制类 →](../37-custom-classes/)


