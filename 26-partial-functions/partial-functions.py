# 偏函数（Partial Function）

import functools

# int() 默认按十进制转换
print(int('12345'))        # 12345

# int() 可以指定进制
print(int('12345', base=8))    # 5349（八进制）
print(int('12345', base=16))   # 74565（十六进制）

# 如果经常需要转二进制，每次写 base=2 很麻烦
# 用 functools.partial 创建偏函数
int2 = functools.partial(int, base=2)

print(int2('1000000'))    # 64
print(int2('1010101'))    # 85

# partial 的本质：固定函数的某些参数
# int2('1010101') 等价于 int('1010101', base=2)

# 也可以固定位置参数
max10 = functools.partial(max, 10)
print(max10(5, 6, 7))    # 10（等价于 max(10, 5, 6, 7)）

# 自己实现 partial 的效果
def int16(s):
    return int(s, base=16)

print(int16('ff'))    # 255
