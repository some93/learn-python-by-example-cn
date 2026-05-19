# list 是有序可变集合

# 创建列表
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))    # 3

# 索引访问：正索引从 0 开始，负索引从 -1 开始
print(classmates[0])      # Michael（第一个）
print(classmates[-1])     # Tracy（最后一个）

# 追加元素
classmates.append('Adam')
print(classmates)

# 插入到指定位置
classmates.insert(1, 'Jack')
print(classmates)

# 删除末尾元素
classmates.pop()
print(classmates)

# 删除指定位置元素
classmates.pop(1)
print(classmates)

# 替换元素（直接赋值）
classmates[1] = 'Sarah'
print(classmates)

# list 可以包含不同类型的元素
mixed = ['Apple', 123, True, None, [1, 2, 3]]
print(mixed)

# 嵌套列表（二维列表）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])    # 6（第2行第3列）

# 空列表
empty = []
print(len(empty))      # 0

# 列表排序
nums = [3, 1, 4, 1, 5, 9]
nums.sort()
print(nums)            # [1, 1, 3, 4, 5, 9]

# in 判断元素是否存在
print('Michael' in classmates)  # True
print('Tom' in classmates)      # False
