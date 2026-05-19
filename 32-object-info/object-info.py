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
