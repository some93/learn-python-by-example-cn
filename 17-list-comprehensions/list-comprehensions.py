# 列表生成式（List Comprehension）


print("=== 普通 for 循环生成列表 ===")

# 先用普通循环写一遍，方便和列表生成式对比。
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)  # [1, 4, 9, 16, 25]


print("\n=== 列表生成式生成列表 ===")

# 列表生成式把“创建空列表、循环、append”压缩成一行。
squares = [x * x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


print("\n=== 带条件过滤 ===")

# if 放在 for 后面时，表示只保留满足条件的元素。
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]


print("\n=== if...else 表达式 ===")

# if...else 放在 for 前面时，表示对每个元素做二选一转换。
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']

# 也可以在保留元素数量不变的情况下改造每个值。
signed_numbers = [x if x % 2 == 0 else -x for x in range(1, 6)]
print(signed_numbers)  # [-1, 2, -3, 4, -5]


print("\n=== 双层循环 ===")

# 双层 for 的执行顺序和普通嵌套循环一致：左边的 for 是外层。
pairs = [letter + number for letter in "AB" for number in "12"]
print(pairs)  # ['A1', 'A2', 'B1', 'B2']

matrix = [[1, 2, 3], [4, 5, 6]]
# 常见用途：把二维列表压平成一维列表。
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]


print("\n=== 遍历字典和处理字符串 ===")

scores = {"小王": 85, "小李": 92, "小张": 78}
# 遍历字典时通常用 items() 同时拿到 key 和 value。
score_items = [f"{name}={score}" for name, score in scores.items()]
print(score_items)  # ['小王=85', '小李=92', '小张=78']

words = ["Hello", "World", 18, "Python", None]
# 先用 isinstance 过滤出字符串，再调用字符串方法，避免类型错误。
lower_words = [word.lower() for word in words if isinstance(word, str)]
print(lower_words)  # ['hello', 'world', 'python']
