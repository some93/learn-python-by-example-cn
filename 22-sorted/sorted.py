# sorted：排序函数

# 基本排序
print(sorted([36, 5, -12, 9, -21]))       # [-21, -12, 5, 9, 36]

# 按绝对值排序：key 参数
print(sorted([36, 5, -12, 9, -21], key=abs))  # [5, 9, -12, -21, 36]

# 字符串排序（默认按 ASCII）
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# ['Credit', 'Zoo', 'about', 'bob']（大写在前）

# 忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# ['about', 'bob', 'Credit', 'Zoo']

# 反向排序
print(sorted([36, 5, -12, 9, -21], reverse=True))

# 对字典列表排序
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
]
result = sorted(students, key=lambda s: s['score'], reverse=True)
for s in result:
    print(f"{s['name']}: {s['score']}")

# sorted vs sort
# sorted() 返回新列表，原列表不变
# list.sort() 原地排序，返回 None
