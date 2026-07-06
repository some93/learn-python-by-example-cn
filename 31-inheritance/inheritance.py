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
dog.run()
cat.run()


print("\n=== super() 调用父类方法 ===")


class Tortoise(Animal):
    def __init__(self, name, speed):
        # super() 调用父类 __init__，避免重复初始化 name。
        super().__init__(name)
        self.speed = speed

    def run(self):
        print(f"{self.name} is running slowly at {self.speed} m/s...")


tortoise = Tortoise("龟仙人", 0.2)
tortoise.run()


print("\n=== isinstance 和 issubclass ===")

# 子类实例同时也是父类实例。
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(issubclass(Dog, Animal))
print(issubclass(Dog, object))


print("\n=== 多态 ===")


def run_twice(animal):
    # 只关心对象有没有 run()，不关心它具体是什么类。
    animal.run()
    animal.run()


run_twice(Dog("小黑"))
run_twice(Cat("小花"))
run_twice(Tortoise("慢慢", 0.1))


print("\n=== 鸭子类型 ===")


class Timer:
    def run(self):
        # Timer 没有继承 Animal，但有 run()，也能被 run_twice 使用。
        print("Timer is ticking...")


run_twice(Timer())
