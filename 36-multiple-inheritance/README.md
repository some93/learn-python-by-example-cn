# 第 36 关：多重继承（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解多重继承的概念
- 掌握 Mixin 设计模式
- 了解 MRO（方法解析顺序）
- 知道何时使用多重继承

## 🤔 先想一个问题

你设计一个游戏角色系统：有会跑的、会飞的、会游泳的。一只鸭子既会飞又会游泳，怎么办？给鸭子同时「装上」飞行模块和游泳模块！这就是**多重继承和 Mixin**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 多重继承

# 单继承
class Animal:
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Parrot(Bird):
    pass

# 需要给动物加上"能跑"、"能飞"的功能
# 用 Mixin 模式：通过多重继承组合功能

class RunnableMixin:
    def run(self):
        print(f"{self.__class__.__name__} is running...")

class FlyableMixin:
    def fly(self):
        print(f"{self.__class__.__name__} is flying...")

class SwimmableMixin:
    def swim(self):
        print(f"{self.__class__.__name__} is swimming...")

# 多重继承：同时继承多个类
class Dog(Mammal, RunnableMixin):
    pass

class Parrot(Bird, FlyableMixin):
    pass

class Duck(Bird, FlyableMixin, SwimmableMixin):
    pass

# 使用
dog = Dog()
dog.run()     # Dog is running...

parrot = Parrot()
parrot.fly()  # Parrot is flying...

duck = Duck()
duck.fly()    # Duck is flying...
duck.swim()   # Duck is swimming...

# MRO（方法解析顺序）
print(Duck.__mro__)

# Python 标准库的 Mixin 例子
# socketserver 模块中：
# class TCPServer(...)
# class ThreadingMixin:
#     ...
# class ThreadingTCPServer(ThreadingMixin, TCPServer):
#     pass
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- Mixin 类名通常以 `Mixin` 结尾，表示它是「混入」功能的
- Mixin 类只提供特定功能，不应该单独实例化
- 多重继承时把主类放前面，Mixin 放后面
- `__mro__` 可以查看方法解析顺序
- Python 标准库大量使用 Mixin，比如 `socketserver.ThreadingMixin`

## 🏃 跑一下试试

```bash
cd 36-multiple-inheritance
python multiple-inheritance.py
```

## 💡 师兄的碎碎念

- Mixin 类名通常以 `Mixin` 结尾，表示它是「混入」功能的
- Mixin 类只提供特定功能，不应该单独实例化
- 多重继承时把主类放前面，Mixin 放后面
- `__mro__` 可以查看方法解析顺序
- Python 标准库大量使用 Mixin，比如 `socketserver.ThreadingMixin`

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `class A(B, C)` | 多重继承语法 |
| `Mixin 模式` | 用小类混入功能，而不是深层继承 |
| `MRO` | 方法解析顺序，决定同名方法调用哪个 |
| `__mro__` | 查看类的方法解析顺序 |
| `ThreadingMixin` | 标准库中 Mixin 的经典例子 |

## ➡️ 下一关

下一关我们学习 [定制类](../37-custom-classes/README.md)，继续加油！
