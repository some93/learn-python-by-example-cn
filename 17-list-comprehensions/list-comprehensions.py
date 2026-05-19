# 列表生成式（List Comprehension）

# 基本用法：生成 1-10 的平方
squares = [x * x for x in range(1, 11)]
print(squares)

# 带条件过滤：只取偶数的平方
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)

# 双层循环
pairs = [m + n for m in 'ABC' for n in 'XYZ']
print(pairs)

# 遍历目录列表
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(f"当前目录文件数: {len(files)}")

# 使用两个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
result = [f"{k}={v}" for k, v in d.items()]
print(result)

# 全部转小写
L = ['Hello', 'World', 'IBM', 'Apple']
lower = [s.lower() for s in L]
print(lower)

# if...else 在列表生成式中的位置
# 前置 if...else（表达式位置）：没有 filter，每个元素都产出
result = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(result)   # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
