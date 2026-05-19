# 调用 Python 内置函数

# abs()：绝对值
print(abs(-10))       # 10
print(abs(3.14))      # 3.14

# max() / min()：最大值 / 最小值
print(max(1, 2, 3))   # 3
print(min(-1, 0, 1))  # -1
print(max([5, 2, 8])) # 8（也能传列表）

# 类型转换函数
print(int('123'))      # 123
print(int(12.9))       # 12（截断，不是四舍五入）
print(float('12.5'))   # 12.5
print(str(123))        # '123'
print(bool(1))         # True
print(bool(''))        # False
print(bool(0))         # False

# hex()：整数转十六进制字符串
print(hex(255))        # '0xff'
print(hex(1000))       # '0x3e8'

# len()：长度
print(len('hello'))    # 5
print(len([1, 2, 3]))  # 3

# sorted()：排序（返回新列表）
print(sorted([3, 1, 4, 1, 5]))    # [1, 1, 3, 4, 5]
print(sorted([3, 1, 4], reverse=True))  # [4, 3, 1]

# isinstance()：判断类型
print(isinstance(123, int))         # True
print(isinstance('hello', str))     # True
print(isinstance([1, 2], list))     # True
print(isinstance(123, (int, float)))  # True（判断是否属于多种类型之一）

# 参数类型错误时的报错
# abs('hello')  # TypeError: bad operand type for abs(): 'str'
