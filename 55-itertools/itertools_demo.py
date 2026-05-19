# itertools

import itertools

# count：无限计数器
for i in itertools.count(1):
    if i > 5:
        break
    print(i, end=' ')    # 1 2 3 4 5
print()

# cycle：无限循环
n = 0
for c in itertools.cycle('ABC'):
    if n >= 6:
        break
    print(c, end=' ')    # A B C A B C
    n += 1
print()

# repeat：重复
for x in itertools.repeat('Hi', 3):
    print(x, end=' ')    # Hi Hi Hi
print()

# chain：串联多个迭代器
for x in itertools.chain('AB', 'CD', 'EF'):
    print(x, end=' ')    # A B C D E F
print()

# groupby：相邻相同元素分组
for key, group in itertools.groupby('AAABBBCCA'):
    print(f"{key}: {list(group)}")
# A: ['A', 'A', 'A']
# B: ['B', 'B', 'B']
# C: ['C', 'C']
# A: ['A']

# 忽略大小写分组
for key, group in itertools.groupby('AaaBBbcCc', lambda c: c.upper()):
    print(f"{key}: {list(group)}")

# product：笛卡尔积
print(list(itertools.product('AB', '12')))
# [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

# permutations：排列
print(list(itertools.permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations：组合
print(list(itertools.combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# islice：切片无限迭代器
print(list(itertools.islice(itertools.count(10), 5)))
# [10, 11, 12, 13, 14]

# accumulate：累积
print(list(itertools.accumulate([1, 2, 3, 4, 5])))
# [1, 3, 6, 10, 15]
