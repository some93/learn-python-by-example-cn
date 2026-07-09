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
