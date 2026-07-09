# 字符串和编码

# 转义字符
print("hello\nworld")       # 输出两行：hello / world
print("hello\tworld")       # hello	world
print("hello\\world")       # hello\world

# r'' 原始字符串：不转义
print(r"hello\nworld")      # hello\nworld

# '''...''' 多行字符串
print('''第一行
第二行
第三行''')              # 输出三行：第一行 / 第二行 / 第三行

# 字符串是不可变的
s = "hello"
# s[0] = 'H'  # TypeError: 'str' object does not support item assignment

# ord() 和 chr()：字符与编码之间的转换
print(ord('A'))     # 65
print(ord('中'))    # 20013
print(chr(65))      # A
print(chr(20013))   # 中

# encode() 和 decode()：字符串与字节之间的转换
print('ABC'.encode('ascii'))       # b'ABC'
print('中文'.encode('utf-8'))       # b'\xe4\xb8\xad\xe6\x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文

# len() 对字符串和字节的区别
print(len('ABC'))                   # 3（字符数）
print(len('中文'))                   # 2（字符数）
print(len('ABC'.encode('ascii')))   # 3（字节数）
print(len('中文'.encode('utf-8')))   # 6（字节数，每个中文3字节）

# 格式化字符串的三种方式

# 方式一：% 操作符（老派写法）
print("Hello, %s. You are %d years old." % ("Alice", 25))  # Hello, Alice. You are 25 years old.

# 方式二：format() 方法
print("Hello, {}. You are {} years old.".format("Bob", 30))  # Hello, Bob. You are 30 years old.

# 方式三：f-string（推荐！Python 3.6+）
name = "Charlie"
age = 35
print(f"Hello, {name}. You are {age} years old.")  # Hello, Charlie. You are 35 years old.
print(f"计算结果: {1 + 2 + 3}")  # 计算结果: 6
print(f"保留两位小数: {3.14159:.2f}")  # 保留两位小数: 3.14
