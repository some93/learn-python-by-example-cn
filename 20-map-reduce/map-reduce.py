# map/reduce 高阶函数

# map：把函数作用到每个元素上
def f(x):
    return x * x

result = map(f, [1, 2, 3, 4, 5])
print(list(result))    # [1, 4, 9, 16, 25]

# 用 lambda 更简洁
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# 把整数列表转字符串列表
print(list(map(str, [1, 2, 3, 4, 5])))  # ['1', '2', '3', '4', '5']

# reduce：把序列累积计算
from functools import reduce

# 求和：1 + 2 + 3 + 4 + 5
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(total)   # 15

# 把 [1, 3, 5, 7] 变成 1357
num = reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7])
print(num)     # 1357

# 组合使用 map 和 reduce
# 把字符串 '13579' 变成整数 13579
def char_to_int(c):
    return ord(c) - ord('0')

result = reduce(lambda x, y: x * 10 + y, map(char_to_int, '13579'))
print(result)  # 13579
