# 第 35 关：@property（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解直接暴露属性的问题
- 用 `@property` 把方法变成属性访问
- 实现属性的读写控制和参数检查
- 实现只读属性

## 🤔 先想一个问题

你在网上买东西，评分只能打 1-5 分。但如果系统没做检查，有人打了 9999 分怎么办？你需要一种方式：看起来像直接赋值，背后偷偷做检查。这就是 `@property`。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# @property

# 直接暴露属性没有参数检查
class BadStudent:
    pass

s = BadStudent()
s.score = 9999   # 没有检查，可以随便设

# 用 getter/setter 方法能检查，但调用不方便
class OldStudent:
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须在 0-100 之间')
        self._score = value

# 用 @property 两全其美！
class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须在 0-100 之间')
        self._score = value

s = Student()
s.score = 88      # 像属性一样赋值，实际调用 setter
print(s.score)     # 像属性一样读取，实际调用 getter

# s.score = 9999  # ValueError!

# 只读属性：只定义 getter，不定义 setter
class Person:
    def __init__(self, birth_year):
        self._birth_year = birth_year

    @property
    def birth_year(self):
        return self._birth_year

    @property
    def age(self):
        import datetime
        return datetime.datetime.now().year - self._birth_year

p = Person(2000)
print(p.age)          # 根据当前年份计算
# p.age = 30          # AttributeError! 只读属性
print(p.birth_year)   # 2000
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `@property` 把 getter 方法变成属性访问，`@xxx.setter` 定义写入逻辑
- 只定义 `@property` 不定义 setter，就是只读属性
- `@property` 比手写 `get_xxx()` / `set_xxx()` 方法优雅得多
- 内部用 `_xxx`（单下划线）存储实际值，避免和属性名冲突
- 可以用 `@property` 实现计算属性（如根据生日算年龄）

## 🏃 跑一下试试

```bash
cd 35-property
python property.py
```

## 💡 师兄的碎碎念

- `@property` 把 getter 方法变成属性访问，`@xxx.setter` 定义写入逻辑
- 只定义 `@property` 不定义 setter，就是只读属性
- `@property` 比手写 `get_xxx()` / `set_xxx()` 方法优雅得多
- 内部用 `_xxx`（单下划线）存储实际值，避免和属性名冲突
- 可以用 `@property` 实现计算属性（如根据生日算年龄）

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `@property` | 把方法变成属性的 getter |
| `@xxx.setter` | 定义属性的 setter，实现写入检查 |
| `只读属性` | 只定义 @property 不定义 setter |
| `计算属性` | getter 中动态计算返回值 |
| `_xxx` | 约定的内部存储属性名 |

## ➡️ 下一关

下一关我们学习 [多重继承](../36-multiple-inheritance/README.md)，继续加油！
