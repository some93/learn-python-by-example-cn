# 第 32 关：获取对象信息（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `type()` 获取对象类型
- 用 `isinstance()` 判断类型（推荐）
- 用 `dir()` 列出对象的所有属性和方法
- 用 `hasattr/getattr/setattr` 动态操作属性

## 🤔 先想一个问题

你收到一个快递包裹，但上面没写是什么东西。你怎么知道里面是啥？可以看标签（type）、问快递员（isinstance）、或者直接拆开看有啥（dir）。Python 里拿到一个对象，怎么「看」它有什么？

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 获取对象信息

# type() 获取类型
print(type(123))           # <class 'int'>
print(type('hello'))       # <class 'str'>
print(type([1, 2, 3]))    # <class 'list'>
print(type(abs))           # <class 'builtin_function_or_method'>

# type() 判断类型
print(type(123) == int)    # True
print(type('hi') == str)   # True

# 判断函数类型需要 types 模块
import types

def fn():
    pass

print(type(fn) == types.FunctionType)           # True
print(type(abs) == types.BuiltinFunctionType)    # True
print(type(lambda x: x) == types.LambdaType)    # True

# isinstance() 判断类型（推荐！）
print(isinstance(123, int))          # True
print(isinstance('hi', str))         # True
print(isinstance([1], (list, tuple)))  # 可以判断多种类型

class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True（能识别继承链）

# dir() 获取对象所有属性和方法
print(dir('hello'))    # 列出 str 的所有方法

# hasattr / getattr / setattr 操作属性
class MyObj:
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObj()
print(hasattr(obj, 'x'))        # True
print(hasattr(obj, 'y'))        # False
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))        # True
print(getattr(obj, 'y'))        # 19

# getattr 可以设默认值，避免报错
print(getattr(obj, 'z', 404))   # 404

# 获取方法
fn = getattr(obj, 'power')
print(fn())    # 81
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `isinstance()` 比 `type()` 好用，因为它能识别继承关系
- `getattr(obj, 'x', default)` 加默认值可以避免 AttributeError
- `dir()` 列出的带 `__xxx__` 的是特殊方法，Python 内部用的
- 动态属性操作很灵活，但别滥用——代码可读性比灵活性重要
- 判断函数类型需要 `import types`，然后用 `types.FunctionType`

## 🏃 跑一下试试

```bash
cd 32-object-info
python object-info.py
```

## 💡 师兄的碎碎念

- `isinstance()` 比 `type()` 好用，因为它能识别继承关系
- `getattr(obj, 'x', default)` 加默认值可以避免 AttributeError
- `dir()` 列出的带 `__xxx__` 的是特殊方法，Python 内部用的
- 动态属性操作很灵活，但别滥用——代码可读性比灵活性重要
- 判断函数类型需要 `import types`，然后用 `types.FunctionType`

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `type(obj)` | 获取对象的精确类型 |
| `isinstance(obj, cls)` | 判断对象是否是某类型（含继承） |
| `dir(obj)` | 列出对象所有属性和方法 |
| `hasattr(obj, 'x')` | 判断对象是否有某属性 |
| `getattr(obj, 'x', default)` | 获取属性值，可设默认值 |
| `setattr(obj, 'x', val)` | 动态设置属性值 |

## ➡️ 下一关

下一关我们学习 [实例属性和类属性](../33-instance-class-attrs/README.md)，继续加油！
