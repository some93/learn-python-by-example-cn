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
