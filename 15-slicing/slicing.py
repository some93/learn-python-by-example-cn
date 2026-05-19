# 切片操作

# 基本切片 L[start:stop]
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])      # ['Michael', 'Sarah', 'Tracy']（取前3个）
print(L[1:3])      # ['Sarah', 'Tracy']
print(L[:3])       # ['Michael', 'Sarah', 'Tracy']（省略 start = 0）
print(L[-2:])      # ['Bob', 'Jack']（后两个）
print(L[:])        # 完整复制

# 带步长 L[start:stop:step]
L2 = list(range(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L2[::2])     # [0, 2, 4, 6, 8]（每隔一个取一个）
print(L2[1::2])    # [1, 3, 5, 7, 9]（奇数位）
print(L2[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]（反转！）

# 字符串切片（字符串也是序列）
s = 'ABCDEFG'
print(s[:3])       # 'ABC'
print(s[::2])      # 'ACEG'
print(s[::-1])     # 'GFEDCBA'（字符串反转）

# 切片不会越界！（索引越界会报错，切片不会）
print(L[0:100])    # 不报错，取到末尾为止

# 用切片复制列表（浅拷贝）
original = [1, 2, 3]
copy = original[:]
copy[0] = 99
print(f"original: {original}")   # [1, 2, 3]（不受影响）
print(f"copy: {copy}")           # [99, 2, 3]

# tuple 也支持切片，结果还是 tuple
t = (0, 1, 2, 3, 4)
print(t[1:3])      # (1, 2)
