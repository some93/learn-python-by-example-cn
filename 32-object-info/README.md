# 第 32 关：获取对象信息

## 🎯 这一关你会学到

- `type()` 获取对象的精确类型
- `isinstance()` 判断类型，并识别继承关系
- `types` 模块如何判断函数类型
- `dir()` 查看对象有哪些属性和方法
- `hasattr()`、`getattr()`、`setattr()` 动态操作属性

## 🤔 先想一个问题

你收到一个快递包裹，但盒子上没写是什么。你可以看快递标签，也可以拆开看看里面有哪些东西。

Python 里拿到一个对象也一样：想知道它是什么类型、能做什么、有没有某个属性，就要用这一关的工具。

## 📖 看代码

```python
# 获取对象信息

import types


print("=== type() 获取精确类型 ===")

# type() 适合检查对象的精确类型。
print(type(123).__name__)  # int
print(type("hello").__name__)  # str
print(type([1, 2, 3]).__name__)  # list
print(type(abs).__name__)  # builtin_function_or_method
print(type(123) == int)  # True
print(type("hi") == str)  # True


print("\n=== 判断函数类型 ===")


def fn():
    return "普通函数"


# types 模块提供了常见函数类型的常量。
print(type(fn) == types.FunctionType)  # True
print(type(abs) == types.BuiltinFunctionType)  # True
print(type(lambda x: x) == types.LambdaType)  # True


print("\n=== isinstance() 能识别继承链 ===")


class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()
# isinstance 会沿着继承链判断。
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
# type(dog) == Animal 只判断精确类型，所以这里是 False。
print(type(dog) == Animal)  # False
print(isinstance([1], (list, tuple)))  # True


print("\n=== dir() 查看对象能力 ===")

names = dir("hello")
# dir() 返回对象能访问的属性和方法名。
print("upper" in names)  # True
print("startswith" in names)  # True
print("__len__" in names)  # True


print("\n=== hasattr/getattr/setattr ===")


class MyObject:
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, "x"))  # True
print(hasattr(obj, "y"))  # False

# setattr 可以在运行时给对象添加属性。
setattr(obj, "y", 19)
print(hasattr(obj, "y"))  # True
print(getattr(obj, "y"))  # 19
# getattr 的第三个参数是默认值，属性不存在时不会报错。
print(getattr(obj, "missing", 404))  # 404

# 方法也是属性，getattr 取出来后可以调用。
method = getattr(obj, "power")
print(method())  # 81

setattr(obj, "name", "demo")
print(obj.name)  # demo
```

## 🔍 师兄给你逐行拆

### `type()` —— 看精确类型

```python
print(type(123).__name__)
print(type("hello").__name__)
print(type([1, 2, 3]).__name__)
print(type(abs).__name__)
print(type(123) == int)
```

**这行在干嘛？**

`type(obj)` 返回对象的精确类型。这里为了让输出更短，用 `.__name__` 打印类型名：

```python
int
str
list
builtin_function_or_method
```

**什么时候用？**

当你确实需要知道“这个对象的精确类型”时，可以用 `type()`。

但业务代码里判断类型，通常更推荐 `isinstance()`，因为它能识别继承关系。

---

### `types` 模块 —— 判断函数类型

```python
import types


def fn():
    return "普通函数"


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
```

**这行在干嘛？**

普通函数、内置函数、lambda 函数的类型并不完全一样。`types` 模块提供了这些类型常量，方便你做精确判断。

**现实提醒**

大多数业务代码不需要这样判断函数类型。更常见的做法是判断对象能不能被调用：

```python
callable(obj)
```

不过这一关先把 `types` 这个工具认识一下。

---

### `isinstance()` —— 判断类型，顺便看继承链

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(type(dog) == Animal)
```

**这行在干嘛？**

`dog` 是 `Dog` 实例，所以 `isinstance(dog, Dog)` 是 `True`。

`Dog` 继承自 `Animal`，所以 `isinstance(dog, Animal)` 也是 `True`。

但 `type(dog) == Animal` 是 `False`，因为 `dog` 的精确类型是 `Dog`，不是 `Animal`。

**为什么推荐 `isinstance()`？**

因为面向对象里经常会有继承。你要判断“这个对象是不是某类或其子类的实例”，`isinstance()` 更符合直觉。

---

### `dir()` —— 看对象有哪些名字

```python
names = dir("hello")
print("upper" in names)
print("startswith" in names)
print("__len__" in names)
```

**这行在干嘛？**

`dir(obj)` 会列出对象能访问的属性和方法名。字符串有 `.upper()`、`.startswith()`，也有 `__len__` 这种特殊方法。

**为什么不直接打印整个 `dir("hello")`？**

因为输出太长，新手看了容易迷路。真实调试时可以直接打印；教程里只检查几个关键名字。

**容易踩的坑**

`dir()` 只是告诉你“名字存在”，不告诉你怎么用。具体用法还要看文档或用 `help()`。

---

### `hasattr/getattr/setattr` —— 动态操作属性

```python
obj = MyObject()
print(hasattr(obj, "x"))
print(hasattr(obj, "y"))

setattr(obj, "y", 19)
print(getattr(obj, "y"))
print(getattr(obj, "missing", 404))
```

**这行在干嘛？**

- `hasattr(obj, "x")`：判断对象有没有属性 `x`；
- `getattr(obj, "y")`：读取属性 `y`；
- `setattr(obj, "y", 19)`：设置属性 `y = 19`；
- `getattr(obj, "missing", 404)`：属性不存在时返回默认值 `404`。

**为什么要用字符串属性名？**

当属性名来自配置、用户输入、网络数据时，你没法提前写死 `obj.x`。这时动态属性操作就有用。

---

### 动态获取方法并调用

```python
method = getattr(obj, "power")
print(method())
```

**这行在干嘛？**

方法也是对象的属性。`getattr(obj, "power")` 拿到的是绑定方法，赋值给 `method` 后可以直接调用。

这里 `power()` 返回 `self.x * self.x`，也就是 `81`。

**容易踩的坑**

动态操作属性很灵活，但过度使用会让代码难读。能直接写 `obj.power()` 时，就别绕一圈写 `getattr(obj, "power")()`。

## 🏃 跑一下试试

```bash
$ python object-info.py
=== type() 获取精确类型 ===
int
str
list
builtin_function_or_method
True
True

=== 判断函数类型 ===
True
True
True

=== isinstance() 能识别继承链 ===
True
True
False
True

=== dir() 查看对象能力 ===
True
True
True

=== hasattr/getattr/setattr ===
True
False
True
19
404
81
demo
```

## 💡 师兄的碎碎念

- `type()` 看精确类型，`isinstance()` 看是否属于某类或其子类。
- 判断多种类型可以写 `isinstance(obj, (list, tuple))`。
- `dir()` 能列出对象的属性和方法名，但不等于文档。
- `getattr(obj, name, default)` 加默认值可以避免属性不存在时报错。
- 动态属性操作适合框架、插件、配置驱动代码，普通业务里别滥用。

## 🎓 这一关的知识点清单

- **type()**：获取对象精确类型。
- **types 模块**：提供函数、内置函数、lambda 等类型常量。
- **isinstance()**：判断对象是否是某类型或其子类实例。
- **dir()**：列出对象可访问的属性和方法名。
- **hasattr()**：判断对象是否有某个属性。
- **getattr()**：按名字获取属性，可提供默认值。
- **setattr()**：按名字设置属性。

## ➡️ 下一关

能查看对象信息后，下一关继续拆对象内部：实例属性和类属性到底谁覆盖谁、谁共享谁 👉 [下一关：实例属性和类属性 →](../33-instance-class-attrs/)


