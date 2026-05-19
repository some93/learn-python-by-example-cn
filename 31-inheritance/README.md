# 第 31 关：继承和多态（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解类的继承机制
- 掌握方法重写（Override）
- 理解多态的概念和优势
- 了解 Python 的鸭子类型

## 🤔 先想一个问题

你开了一家宠物店，有狗、猫、乌龟。每种动物都会「跑」，但跑的方式不一样。你会给每种动物单独写一套代码吗？还是让它们共享一个「动物」模板，各自改改就行？这就是**继承和多态**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- Python 所有类都默认继承 `object`，不写也是
- 方法重写就是子类重新定义父类的同名方法
- Python 是鸭子类型：不在乎你是不是 Animal 的子类，只要你有 `run()` 方法就行
- 多态的好处：写通用代码，不用关心具体类型，新增子类不用改老代码
- `isinstance()` 能识别继承链，`type()` 只看精确类型

## 🏃 跑一下试试

```bash
cd 31-inheritance
python inheritance.py
```

## 💡 师兄的碎碎念

- Python 所有类都默认继承 `object`，不写也是
- 方法重写就是子类重新定义父类的同名方法
- Python 是鸭子类型：不在乎你是不是 Animal 的子类，只要你有 `run()` 方法就行
- 多态的好处：写通用代码，不用关心具体类型，新增子类不用改老代码
- `isinstance()` 能识别继承链，`type()` 只看精确类型

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `class Dog(Animal)` | 继承语法，Dog 继承 Animal |
| `def run(self)` | 子类重写父类方法 |
| `isinstance(dog, Animal)` | 判断继承关系，返回 True |
| `issubclass(Dog, Animal)` | 判断类的继承关系 |
| `鸭子类型` | 不要求继承，只要有同名方法就能用 |

## ➡️ 下一关

下一关我们学习 [获取对象信息](../32-object-info/README.md)，继续加油！
