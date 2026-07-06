# 定制类


print("=== __str__ 和 __repr__ ===")


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # print(obj) 会优先使用 __str__ 的返回值。
        return f"Student({self.name})"

    # 交互环境、列表展示等场景会使用 __repr__。
    __repr__ = __str__


student = Student("Alice")
print(student)
print([student])


print("\n=== __iter__ 和 __next__ ===")


class Fib:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        # 返回 self 表示这个对象自己就是迭代器。
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.max_value:
            raise StopIteration
        return self.a


print(list(Fib(100)))


print("\n=== __getitem__ 支持下标和切片 ===")


class FibList:
    def __getitem__(self, item):
        # 为了演示下标和切片，先准备一段斐波那契数列。
        values = [1, 1]
        while len(values) <= 20:
            values.append(values[-1] + values[-2])

        if isinstance(item, int):
            # fib[5] 会走这里。
            return values[item]
        if isinstance(item, slice):
            # fib[:6] 会把 slice 对象传进来。
            return values[item]
        raise TypeError("下标必须是整数或切片")


fib = FibList()
print(fib[0])
print(fib[5])
print(fib[:6])
print(fib[2:8:2])


print("\n=== __getattr__ 动态属性 ===")


class Chain:
    def __init__(self, path=""):
        self._path = path

    def __getattr__(self, name):
        # 只有正常属性找不到时，才会调用 __getattr__。
        return Chain(f"{self._path}/{name}")

    def __str__(self):
        return self._path or "/"

    __repr__ = __str__


chain = Chain()
print(chain.api.users.list)
print(chain._path == "")


print("\n=== __call__ 让实例像函数一样调用 ===")


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, step=1):
        # 定义 __call__ 后，实例就能像函数一样被调用。
        self.count += step
        return self.count


counter = Counter()
print(counter())
print(counter())
print(counter(10))
print(callable(counter))
print(callable(Student))
print(callable(student))
