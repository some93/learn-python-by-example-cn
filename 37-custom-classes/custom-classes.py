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
