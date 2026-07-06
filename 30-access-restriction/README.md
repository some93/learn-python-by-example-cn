# 第 30 关：访问限制（师兄带你学 Python）

## 🎯 这一关你会学到

- 为什么要封装对象内部数据
- 单下划线 `_name`、双下划线 `__name`、前后双下划线 `__name__` 的区别
- 如何通过 getter/setter 控制读写
- Python 的“私有”本质是名字改编，不是绝对禁止访问
- 为什么“能访问”不等于“应该访问”

## 🤔 先想一个问题

学生分数不能随便乱填。你当然可以把 `score` 直接暴露出去，让任何人写：

```python
student.score = 9999
```

但这样系统迟早乱套。更靠谱的做法是：分数藏在对象内部，外面只能通过指定方法修改，方法里负责校验。

这就是封装：**把内部细节藏起来，把安全入口留出来**。

## 📖 看代码

```python
# 访问限制


print("=== 私有属性和公开方法 ===")


class Student:
    def __init__(self, name, score):
        # 双下划线开头会触发名字改编，外部不能直接用 __name 访问。
        self.__name = name
        self.__score = score

        # 单下划线只是约定私有，语法上仍然能访问。
        self._school = "Springfield School"

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        # 通过 setter 统一校验，避免外部随便写入非法值。
        if not 0 <= score <= 100:
            raise ValueError("分数必须在 0-100 之间")
        self.__score = score

    def print_info(self):
        print(f"{self.__name}: {self.__score}")


bart = Student("Bart", 59)
bart.print_info()
print(bart.get_name())
print(bart.get_score())

bart.set_score(80)
bart.print_info()


print("\n=== setter 负责校验 ===")

try:
    bart.set_score(120)
except ValueError as error:
    print(error)


print("\n=== 不能直接访问双下划线属性 ===")

try:
    # 外部没有 bart.__name 这个属性名。
    print(bart.__name)
except AttributeError as error:
    print(type(error).__name__)


print("\n=== 名字改编：能访问，但不该访问 ===")

# Python 会把 __name 改成 _类名__name，目的是避免意外访问。
print(bart._Student__name)
print(bart._Student__score)


print("\n=== 三种下划线写法 ===")

print(bart._school)
print(hasattr(bart, "__name"))
print(hasattr(bart, "_Student__name"))
# __init__ 这种首尾双下划线是特殊方法，不属于私有属性。
print(Student.__init__.__name__)
```

## 🔍 师兄给你逐行拆

### `self.__name` —— 双下划线属性

```python
class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self._school = "Springfield School"
```

**这行在干嘛？**

`__name` 和 `__score` 是双下划线开头的属性。Python 会对它们做名字改编，外部不能直接用 `bart.__name` 访问。

`_school` 是单下划线开头，表示约定私有：外部能访问，但不建议当作公开 API 使用。

**为什么要这样做？**

你不希望外部代码随便改学生分数。把分数藏起来，再提供方法控制修改，就能加校验逻辑。

---

### getter/setter —— 留出安全入口

```python
def get_score(self):
    return self.__score

def set_score(self, score):
    if not 0 <= score <= 100:
        raise ValueError("分数必须在 0-100 之间")
    self.__score = score
```

**这行在干嘛？**

`get_score()` 负责读取分数，`set_score()` 负责修改分数。

修改时先检查分数是否在 `0-100` 之间，不合法就抛出 `ValueError`。

**生活类比**

保险箱里的钱不能让客人自己伸手拿。你可以找前台办理，前台会检查身份、金额和规则。getter/setter 就像这个前台。

**容易踩的坑**

Python 后面还有更优雅的 `@property` 写法，可以让你像访问属性一样触发校验。这里先用 getter/setter，是为了把封装思想讲清楚。

---

### 直接访问 `bart.__name` 会失败

```python
try:
    print(bart.__name)
except AttributeError as error:
    print(type(error).__name__)
```

**这行在干嘛？**

外部直接访问 `bart.__name` 会抛出 `AttributeError`，因为 Python 实际上把它改名了。

注意，这不是操作系统级别的安全机制，不是密码锁。它更像 Python 帮你把内部名字藏了一下，防止无意误用。

---

### 名字改编：`_Student__name`

```python
print(bart._Student__name)
print(bart._Student__score)
```

**这行在干嘛？**

双下划线属性会被改编成：

```python
_类名__属性名
```

所以 `__name` 在 `Student` 类里实际变成了 `_Student__name`。

**为什么教程还要演示这个？**

不是让你这么用，而是让你理解：Python 的私有不是绝对不可访问，而是靠名字改编降低误访问概率。

**容易踩的坑**

能访问不代表应该访问。外部代码依赖 `_Student__name`，等类名一改、内部实现一改，你的代码就碎了。

---

### 三种下划线写法别混淆

```python
print(bart._school)
print(hasattr(bart, "__name"))
print(hasattr(bart, "_Student__name"))
print(Student.__init__.__name__)
```

**这行在干嘛？**

这几行对比三种常见命名：

- `_school`：单下划线，约定内部使用；
- `__name`：双下划线开头，触发名字改编；
- `__init__`：前后都有双下划线，是 Python 特殊方法，不是私有属性。

**重点记忆**

`__xxx__` 这种“魔法方法”是 Python 协议的一部分，比如 `__init__`、`__str__`、`__len__`。不要自己随便发明新的 `__xxx__` 名字。

## 🏃 跑一下试试

```bash
$ python access-restriction.py
=== 私有属性和公开方法 ===
Bart: 59
Bart
59
Bart: 80

=== setter 负责校验 ===
分数必须在 0-100 之间

=== 不能直接访问双下划线属性 ===
AttributeError

=== 名字改编：能访问，但不该访问 ===
Bart
80

=== 三种下划线写法 ===
Springfield School
False
True
__init__
```

## 💡 师兄的碎碎念

- `_name` 是约定内部使用，外部能访问但不建议。
- `__name` 会触发名字改编，变成 `_ClassName__name`。
- `__name__` 是特殊方法命名风格，不是私有。
- Python 的访问限制更强调约定和封装，不是绝对安全边界。
- 如果只是普通业务属性，后面第 35 关的 `@property` 通常比手写 getter/setter 更 Pythonic。

## 🎓 这一关的知识点清单

- **封装**：隐藏内部数据，通过方法暴露安全入口。
- **私有属性**：双下划线开头的 `__name` 会触发名字改编。
- **getter/setter**：读取和修改私有属性的方法，可加入校验逻辑。
- **名字改编**：`__name` 会变成 `_ClassName__name`。
- **约定私有**：单下划线 `_name` 表示内部使用。
- **特殊方法**：`__init__` 这类前后双下划线名字是 Python 协议方法，不是私有。

## ➡️ 下一关

封装讲完，面向对象还剩两个大件：继承和多态。下一关看子类如何复用父类，又如何改写自己的行为 👉 [下一关：继承和多态 →](../31-inheritance/)




