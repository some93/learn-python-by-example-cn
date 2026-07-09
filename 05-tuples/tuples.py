# tuple 是有序不可变序列

# 创建元组
t = (1, 2, 3)
print(t)           # (1, 2, 3)
print(t[0])       # 1
print(t[-1])      # 3
print(len(t))     # 3

# 元组不可修改！
# t[0] = 10       # TypeError: 'tuple' object does not support item assignment

# 定义只有一个元素的 tuple —— 必须加逗号！
t1 = (1,)         # 这是 tuple
t2 = (1)          # 这是整数 1，不是 tuple！
print(type(t1))   # <class 'tuple'>
print(type(t2))   # <class 'int'>

# 空元组
t0 = ()
print(t0)         # ()
print(len(t0))    # 0

# tuple 的"可变"陷阱
# tuple 中如果包含 list，list 的内容可以修改
t3 = ('a', 'b', ['X', 'Y'])
print("修改前:", t3)  # 修改前: ('a', 'b', ['X', 'Y'])
t3[2][0] = 'M'    # 修改的是 list 内部，不是 tuple 本身
t3[2][1] = 'N'
print("修改后:", t3)  # 修改后: ('a', 'b', ['M', 'N'])

# 解包（unpacking）
x, y, z = (10, 20, 30)
print(x, y, z)    # 10 20 30

# tuple 可以作为 dict 的 key（因为不可变）
# list 不行
d = {(1, 2): "point A", (3, 4): "point B"}
print(d[(1, 2)])  # point A

# tuple 和 list 的互相转换
lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl)        # (1, 2, 3)

back_to_list = list(tpl)
print(back_to_list)  # [1, 2, 3]
