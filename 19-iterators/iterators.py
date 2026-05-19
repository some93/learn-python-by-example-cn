# 迭代器（Iterator）

from collections.abc import Iterable, Iterator

# 可迭代对象 vs 迭代器
# 可迭代对象（Iterable）：能用 for 遍历的对象
# 迭代器（Iterator）：能用 next() 逐个取值的对象

# list、dict、str 是 Iterable，但不是 Iterator
print(isinstance([], Iterable))      # True
print(isinstance([], Iterator))      # False

# iter() 把 Iterable 转成 Iterator
it = iter([1, 2, 3])
print(isinstance(it, Iterator))     # True
print(next(it))    # 1
print(next(it))    # 2
print(next(it))    # 3
# print(next(it))  # StopIteration!

# for 循环的本质
# for x in [1, 2, 3]:  等价于：
it = iter([1, 2, 3])
while True:
    try:
        x = next(it)
        print(x, end=" ")
    except StopIteration:
        break
print()

# 生成器天生就是 Iterator
g = (x for x in range(3))
print(isinstance(g, Iterator))      # True

# 自定义迭代器类
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num, end=" ")
print()
