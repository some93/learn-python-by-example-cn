# set 是无序不重复元素集合

# 创建 set
s = {1, 2, 3, 1, 2}     # 自动去重
print(s)                  # {1, 2, 3}

# 用 set() 从列表创建
s2 = set([4, 5, 5, 6])
print(s2)                 # {4, 5, 6}

# 添加和删除元素
s.add(4)
print(s)                  # {1, 2, 3, 4}
s.remove(2)
print(s)                  # {1, 3, 4}

# 集合运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)     # 交集: {3, 4}
print(a | b)     # 并集: {1, 2, 3, 4, 5, 6}
print(a - b)     # 差集: {1, 2}
print(a ^ b)     # 对称差集: {1, 2, 5, 6}

# in 判断元素是否存在
print(3 in a)    # True
print(9 in a)    # False

# 用 set 去重
lst = [1, 1, 2, 2, 3, 3, 4]
unique = list(set(lst))
print(unique)    # [1, 2, 3, 4]（顺序可能不同）

# set 不能包含可变元素
# s3 = {[1, 2]}  # TypeError: unhashable type: 'list'
s3 = {(1, 2), (3, 4)}  # tuple 可以
print(s3)

# 遍历 set
for item in a:
    print(item, end=" ")
print()
