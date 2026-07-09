# sorted：排序函数


print("=== 基本排序 ===")

numbers = [36, 5, -12, 9, -21]
# sorted() 返回新列表，不会修改原列表。
print(sorted(numbers))  # [-21, -12, 5, 9, 36]
print(numbers)          # [36, 5, -12, 9, -21]


print("\n=== key：自定义排序规则 ===")

# key 指定“按什么值排序”，这里按绝对值排序。
print(sorted(numbers, key=abs))  # [5, 9, -12, -21, 36]

words = ["bob", "about", "Zoo", "Credit"]
print(sorted(words))            # ['Credit', 'Zoo', 'about', 'bob']
# 忽略大小写排序时，可以把每个单词先转成小写再比较。
print(sorted(words, key=str.lower))  # ['about', 'bob', 'Credit', 'Zoo']


print("\n=== reverse：反向排序 ===")

print(sorted(numbers, reverse=True))      # [36, 9, 5, -12, -21]
# key 和 reverse 可以一起使用：先按绝对值排序，再反向。
print(sorted(numbers, key=abs, reverse=True))  # [36, -21, -12, 9, 5]


print("\n=== 对字典列表排序 ===")

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 85},
    {"name": "Diana", "score": 92},
]

# 按分数从高到低排序。
by_score = sorted(students, key=lambda student: student["score"], reverse=True)
for student in by_score:  # Bob: 92 / Diana: 92 / Alice: 85 / Charlie: 85
    print(f"{student['name']}: {student['score']}")

# 元组 key 可以实现多条件排序：先按分数降序，再按姓名升序。
by_score_name = sorted(students, key=lambda student: (-student["score"], student["name"]))
print([student["name"] for student in by_score_name])  # ['Bob', 'Diana', 'Alice', 'Charlie']


print("\n=== key 函数只调用一次 ===")

calls = []


def by_length(word):
    # 记录 key 函数被调用的顺序。
    calls.append(word)
    return len(word)


print(sorted(["pear", "fig", "apple"], key=by_length))  # ['fig', 'pear', 'apple']
print(calls)                                             # ['pear', 'fig', 'apple']


print("\n=== sorted() vs list.sort() ===")

data = [3, 1, 2]
new_data = sorted(data)
print(data)      # [3, 1, 2]
print(new_data)  # [1, 2, 3]

# list.sort() 会原地修改列表，并返回 None。
result = data.sort()
print(data)    # [1, 2, 3]
print(result)  # None
