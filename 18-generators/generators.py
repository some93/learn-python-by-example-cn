# 生成器（Generator）


print("=== 列表 vs 生成器表达式 ===")

# 列表会一次性把所有结果算出来并放进内存。
squares_list = [x * x for x in range(5)]

# 生成器表达式只保存计算规则，需要时才产出下一个值。
squares_gen = (x * x for x in range(5))

print(squares_list)               # [0, 1, 4, 9, 16]
print(type(squares_gen).__name__) # generator
# next() 每调用一次，生成器就向前走一步。
print(next(squares_gen))          # 0
print(next(squares_gen))          # 1
print(list(squares_gen))          # [4, 9, 16]


print("\n=== 生成器只能消费一次 ===")

numbers = (x for x in range(3))
# 第一次 list() 会把生成器里的值全部取完。
print(list(numbers))  # [0, 1, 2]
# 第二次再取时，生成器已经空了。
print(list(numbers))  # []


print("\n=== StopIteration ===")

one_item = (x for x in [10])
print(next(one_item))  # 10
try:
    # 生成器没有更多值时，会抛出 StopIteration。
    print(next(one_item))
except StopIteration:
    print("生成器已经取完")


print("\n=== yield 定义生成器函数 ===")


def fib(max_count):
    n, a, b = 0, 0, 1
    while n < max_count:
        # yield 会返回一个值，同时暂停函数状态。
        yield b
        a, b = b, a + b
        n += 1


print(list(fib(10)))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


print("\n=== yield 的暂停和恢复 ===")


def count_up_to(n):
    print("开始生成")
    i = 1
    while i <= n:
        print(f"  即将 yield {i}")
        # 外层 for 收到这个值后，函数会停在这里。
        yield i
        # 下一次取值时，从 yield 后面继续执行。
        print(f"  yield {i} 之后继续")
        i += 1
    print("生成结束")


for value in count_up_to(3):  # 依次收到：1 / 2 / 3
    print(f"收到: {value}")
