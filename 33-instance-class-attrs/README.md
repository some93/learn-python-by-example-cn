# 第 33 关：实例属性和类属性（师兄带你学 Python）

## 🎯 这一关你会学到

- 区分实例属性和类属性
- 理解属性查找顺序（实例 → 类）
- 掌握实例属性「遮蔽」类属性的机制
- 用类属性实现共享数据（如计数器）

## 🤔 先想一个问题

班级里每个同学有自己的名字（实例属性），但大家共享同一个学校名称（类属性）。如果某个同学转学了，他的学校变了，其他同学的学校会跟着变吗？

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 实例属性和类属性

class Student:
    # 类属性：所有实例共享
    school = '清华大学'

    def __init__(self, name):
        # 实例属性：每个实例独立
        self.name = name

s1 = Student('Alice')
s2 = Student('Bob')

# 访问类属性
print(Student.school)    # 清华大学
print(s1.school)         # 清华大学（通过实例也能访问）
print(s2.school)         # 清华大学

# 实例属性互不影响
print(s1.name)    # Alice
print(s2.name)    # Bob

# 注意：实例属性会"遮蔽"同名的类属性
s1.school = '北京大学'   # 这是给 s1 加了一个实例属性！
print(s1.school)         # 北京大学（实例属性）
print(s2.school)         # 清华大学（类属性不受影响）
print(Student.school)    # 清华大学

# 删掉实例属性后，又能看到类属性了
del s1.school
print(s1.school)         # 清华大学

# 用类属性做计数器
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1    # 用类名访问，而不是 self

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)    # 3
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- 类属性写在类里、方法外，所有实例共享
- 实例属性通过 `self.xxx = ...` 定义，每个实例独立
- 给实例赋值同名属性会「遮蔽」类属性，不会修改类属性
- `del` 删除实例属性后，又能看到类属性了
- 修改类属性要用 `ClassName.attr = ...`，别用 `self.attr = ...`

## 🏃 跑一下试试

```bash
cd 33-instance-class-attrs
python instance-class-attrs.py
```

## 💡 师兄的碎碎念

- 类属性写在类里、方法外，所有实例共享
- 实例属性通过 `self.xxx = ...` 定义，每个实例独立
- 给实例赋值同名属性会「遮蔽」类属性，不会修改类属性
- `del` 删除实例属性后，又能看到类属性了
- 修改类属性要用 `ClassName.attr = ...`，别用 `self.attr = ...`

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `类属性` | 定义在类中方法外，所有实例共享 |
| `实例属性` | 通过 self.xxx 定义，每个实例独立 |
| `属性查找顺序` | 先找实例属性，找不到再找类属性 |
| `遮蔽效果` | 实例属性与类属性同名时，实例属性优先 |
| `Counter.count` | 用类属性做共享计数器 |

## ➡️ 下一关

下一关我们学习 [__slots__](../34-slots/README.md)，继续加油！
