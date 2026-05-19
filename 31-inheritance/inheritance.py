# 继承和多态

# 定义基类
class Animal:
    def run(self):
        print("Animal is running...")

# 继承 Animal
class Dog(Animal):
    def run(self):
        print("Dog is running...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

# 创建实例
dog = Dog()
cat = Cat()
dog.run()    # Dog is running...
cat.run()    # Cat is running...

# 子类也是父类的实例
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True

# 多态：不同子类调用同一方法，行为不同
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())    # Dog is running... × 2
run_twice(Cat())    # Cat is running... × 2

# 新增一个子类，run_twice 不用改！
class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly...")

run_twice(Tortoise())

# Python 的鸭子类型：不要求继承，只要有 run 方法就行
class Timer:
    def run(self):
        print("Timer is ticking...")

run_twice(Timer())  # 也能跑！

# 判断继承关系
print(issubclass(Dog, Animal))   # True
print(issubclass(Dog, object))   # True（所有类都继承自 object）
