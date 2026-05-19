# 第 29 关：类和实例（师兄带你学 Python）

## 🎯 这一关你会学到

- 面向对象编程基础
- class 关键字定义类
- __init__ 构造方法和 self
- 实例属性和方法

## 🤔 先想一个问题

类就像奶茶店的配方单——写着需要茶底、奶、糖、配料。实例就是做出来的每一杯具体奶茶——都是奶茶，但每杯的糖量、配料可以不同。`__init__` 就是「下单」时填的选项。

## 📖 看代码

```python
# 类和实例

# 定义类
class Student:
    def __init__(self, name, score):
        self.name = name      # 实例属性
        self.score = score

    def print_score(self):
        print(f"{self.name}: {self.score}")

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# 创建实例
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()
print(f"{bart.name} 的等级: {bart.get_grade()}")

# 可以自由给实例绑定属性
bart.age = 10
print(bart.age)

# 类也是对象
print(type(bart))       # <class '__main__.Student'>
print(isinstance(bart, Student))  # True
```

## 🔍 师兄给你逐行拆

面向对象编程（OOP）把数据和操作数据的方法打包在一起。类是模板，实例是根据模板创建的具体对象。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python classes-and-instances.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **class ClassName: 定义类**
- **__init__(self, ...) 构造方法**
- **self 代表实例自身**
- **实例属性 self.xxx 和方法**

## 🎓 这一关的知识点清单

- **面向对象编程基础**
- **class 关键字定义类**
- **__init__ 构造方法和 self**
- **实例属性和方法**

## ➡️ 下一关

本关搞定！接下来学 访问限制 👉 [下一关：访问限制 →](../30-access-restriction/)
