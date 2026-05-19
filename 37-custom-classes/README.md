# 第 37 关：定制类（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `__str__` / `__repr__` 自定义打印
- 用 `__iter__` / `__next__` 让对象可迭代
- 用 `__getitem__` 支持下标访问
- 用 `__getattr__` 动态返回属性
- 用 `__call__` 让实例可以像函数一样调用

## 🤔 先想一个问题

你打印一个自己写的类，屏幕上显示 `<__main__.Student object at 0x...>`，完全看不懂。能不能让它显示 `Student(Alice)` 这种人话？Python 提供了一堆「魔法方法」让你定制类的行为。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 定制类

# __str__ 和 __repr__：自定义打印输出
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student({self.name})"

    __repr__ = __str__   # 调试时也用同样的输出

print(Student('Alice'))    # Student(Alice)

# __iter__ 和 __next__：让对象可以 for 循环
class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n, end=' ')   # 1 1 2 3 5 8 13 21 34 55 89
print()

# __getitem__：让对象支持下标访问
class Fib2:
    def __getitem__(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

f = Fib2()
print(f[0])    # 1
print(f[5])    # 8
print(f[10])   # 89

# __getattr__：动态返回属性
class Chain:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, name):
        return Chain(f"{self._path}/{name}")

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().api.users.list)    # /api/users/list

# __call__：让实例可以像函数一样调用
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print(c())    # 1
print(c())    # 2
print(c())    # 3
print(callable(c))    # True
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `__str__` 是给用户看的（print），`__repr__` 是给开发者看的（调试）
- 偷懒可以 `__repr__ = __str__`
- `__iter__` + `__next__` 让对象能用 `for` 循环
- `__getattr__` 只在属性不存在时才调用，已有的属性不受影响
- `callable(obj)` 可以判断对象是否实现了 `__call__`

## 🏃 跑一下试试

```bash
cd 37-custom-classes
python custom-classes.py
```

## 💡 师兄的碎碎念

- `__str__` 是给用户看的（print），`__repr__` 是给开发者看的（调试）
- 偷懒可以 `__repr__ = __str__`
- `__iter__` + `__next__` 让对象能用 `for` 循环
- `__getattr__` 只在属性不存在时才调用，已有的属性不受影响
- `callable(obj)` 可以判断对象是否实现了 `__call__`

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `__str__` | 自定义 print() 输出 |
| `__repr__` | 自定义调试输出 |
| `__iter__ + __next__` | 让对象可以 for 循环遍历 |
| `__getitem__` | 让对象支持 obj[n] 下标访问 |
| `__getattr__` | 属性不存在时动态返回 |
| `__call__` | 让实例可以像函数一样调用 obj() |

## ➡️ 下一关

下一关我们学习 [枚举类](../38-enum/README.md)，继续加油！
