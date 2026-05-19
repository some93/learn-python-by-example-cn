# 迭代

# 遍历 list
for item in [1, 2, 3]:
    print(item)

# 遍历 dict（默认遍历 key）
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(f"{key}: {d[key]}")

# 遍历 value
for value in d.values():
    print(value)

# 同时遍历 key 和 value
for k, v in d.items():
    print(f"{k} => {v}")

# 遍历字符串
for ch in 'Python':
    print(ch, end=" ")
print()

# enumerate：同时获取索引和值
for i, value in enumerate(['A', 'B', 'C']):
    print(f"{i}: {value}")

# 同时遍历多个序列：zip
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 判断对象是否可迭代
from collections.abc import Iterable
print(isinstance('hello', Iterable))   # True
print(isinstance(123, Iterable))       # False
print(isinstance([1, 2], Iterable))    # True
