# 迭代器（Iterator）

from collections.abc import Iterable, Iterator


print("=== Iterable vs Iterator ===")

numbers = [1, 2, 3]

# 列表可以被 for 遍历，所以它是 Iterable。
print(isinstance(numbers, Iterable))
# 但列表本身不是 Iterator，因为它没有记录“当前走到哪里”。
print(isinstance(numbers, Iterator))

# iter() 会把可迭代对象转换成迭代器。
it = iter(numbers)
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))


print("\n=== iter() 和 next() ===")

# next() 每调用一次，就从迭代器里取出下一个元素。
print(next(it))
print(next(it))
print(next(it))
try:
    # 迭代器耗尽后，再取会抛出 StopIteration。
    print(next(it))
except StopIteration:
    print("没有更多元素了")


print("\n=== for 循环的本质 ===")

it = iter([1, 2, 3])
while True:
    try:
        # for 循环内部本质上就是反复调用 next()。
        value = next(it)
        print(value, end=" ")
    except StopIteration:
        break
print()


print("\n=== 生成器天生就是 Iterator ===")

g = (x * x for x in range(3))
print(isinstance(g, Iterator))
print(list(g))
# 生成器也是一次性的，消费完之后再次遍历为空。
print(list(g))


print("\n=== 自定义一次性迭代器 ===")


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # 一次性迭代器通常返回 self。
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


countdown = Countdown(3)
print(list(countdown))
print(list(countdown))


print("\n=== 自定义可重复遍历的对象 ===")


class Team:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        # 每次返回一个新的列表迭代器，所以 Team 可以重复遍历。
        return iter(self.members)


team = Team(["小王", "小李", "小张"])
print(list(team))
print(list(team))
