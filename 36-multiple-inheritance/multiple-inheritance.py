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
