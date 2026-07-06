# map/reduce 高阶函数

from functools import reduce


print("=== map：逐个加工 ===")


def square(x):
    return x * x


# map 返回的是惰性迭代器，不会立刻生成完整列表。
mapped = map(square, [1, 2, 3, 4, 5])
print(type(mapped).__name__)
print(list(mapped))
# map 结果消费完之后，再转 list 就没有内容了。
print(list(mapped))


print("\n=== map 和列表生成式对比 ===")

numbers = [1, 2, 3, 4, 5]
# 这两种写法结果相同；列表生成式通常更直观。
print(list(map(square, numbers)))
print([square(x) for x in numbers])


print("\n=== map 的常见用法 ===")

# 把一组数字统一转换成字符串。
print(list(map(str, [1, 2, 3, 4, 5])))

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
# map 可以同时遍历多个序列，按位置把参数传给函数。
records = map(lambda name, score: f"{name}: {score}", names, scores)
print(list(records))


print("\n=== reduce：累积合并 ===")

# reduce 会把上一次计算结果继续和下一个元素合并。
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(total)

product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)


print("\n=== reduce 的初始值 ===")

# 空序列必须提供初始值，否则 reduce 不知道从哪里开始。
print(reduce(lambda x, y: x + y, [], 0))
try:
    print(reduce(lambda x, y: x + y, []))
except TypeError as error:
    print(type(error).__name__)


print("\n=== map + reduce 组合 ===")


def char_to_int(ch):
    return ord(ch) - ord("0")


def digits_to_int(text):
    # 先把字符映射成数字，再用 reduce 拼成整数。
    return reduce(lambda x, y: x * 10 + y, map(char_to_int, text))


print(digits_to_int("13579"))
