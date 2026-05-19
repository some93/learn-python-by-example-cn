# 第 30 关：访问限制（师兄带你学 Python）

## 🎯 这一关你会学到

- 封装和访问控制
- __双下划线表示私有属性
- 通过 getter/setter 方法访问
- Python 的私有是名字改编不是真正不可访问

## 🤔 先想一个问题

私有属性像酒店保险箱——住客不能直接打开，必须通过前台操作。但 Python 的保险箱有个后门（名字改编为 _ClassName__xxx），只是君子不走后门。

## 📖 看代码

```python
# 访问限制

class Student:
    def __init__(self, name, score):
        self.__name = name      # 双下划线开头：私有属性
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('分数必须在 0-100 之间')

    def print_info(self):
        print(f"{self.__name}: {self.__score}")

bart = Student('Bart', 59)
bart.print_info()

# 不能直接访问私有属性
# print(bart.__name)  # AttributeError!

# 通过 getter/setter 访问
print(bart.get_name())
bart.set_score(80)
bart.print_info()

# Python 的"私有"是名字改编，不是真正的访问控制
# 实际上可以通过 _类名__属性名 访问（但不要这样做！）
print(bart._Student__name)    # Bart（能访问但别这么干）

# 单下划线 _xxx：约定私有，外部可以访问但不建议
# 双下划线 __xxx：名字改编为 _ClassName__xxx
# __xxx__：特殊变量（如 __init__），不是私有的
```

## 🔍 师兄给你逐行拆

Python 用双下划线前缀 __xxx 实现属性的访问限制——外部不能直接访问，必须通过方法来读写。这是封装的基础。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python access-restriction.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **__xxx 双下划线：私有属性（名字改编）**
- **_xxx 单下划线：约定私有（可访问）**
- **getter/setter 方法控制访问**
- **__xxx__ 双下划线包围：特殊变量（非私有）**

## 🎓 这一关的知识点清单

- **封装和访问控制**
- **__双下划线表示私有属性**
- **通过 getter/setter 方法访问**
- **Python 的私有是名字改编不是真正不可访问**

## ➡️ 下一关

本关搞定！接下来学 继承和多态 👉 [下一关：继承和多态 →](../31-inheritance/)
