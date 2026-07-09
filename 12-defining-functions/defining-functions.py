# 定义函数

# 用 def 关键字定义函数
def greet(name):
    print(f"Hello, {name}!")

greet("World")  # Hello, World!

# 带返回值的函数
def add(a, b):
    return a + b

result = add(1, 2)
print(f"1 + 2 = {result}")  # 1 + 2 = 3

# 没有 return 时，函数返回 None
def do_nothing():
    pass    # pass 是占位符，表示"什么都不做"

print(do_nothing())   # None

# 返回多个值（其实是返回 tuple）
def move(x, y, step):
    new_x = x + step
    new_y = y + step
    return new_x, new_y

x, y = move(100, 200, 50)
print(f"新坐标: ({x}, {y})")  # 新坐标: (150, 250)

# 参数类型检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-9))      # 9
print(my_abs(3.14))    # 3.14
# my_abs('hello')      # TypeError: 参数类型错误

# 函数可以有文档字符串
def power(x, n):
    """计算 x 的 n 次方"""
    return x ** n

print(power(2, 10))    # 1024
print(power.__doc__)   # 计算 x 的 n 次方
