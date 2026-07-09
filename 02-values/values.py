# Python 的基本数据类型和变量

# 整数：没有大小限制！
a = 100
b = -8080
c = 0xff00        # 十六进制
print(a, b, c)    # 100 -8080 65280

# 浮点数：有精度限制
d = 1.23
e = 1.23e9        # 科学计数法，1.23 × 10^9
f = 0.1 + 0.2     # 经典精度问题
print(d, e, f)    # 1.23 1230000000.0 0.30000000000000004

# 字符串：单引号或双引号都行
s1 = 'hello'
s2 = "world"
print(s1, s2)     # hello world

# 布尔值：True 和 False（注意大写）
t = True
f = False
print(t, f)       # True False
print(t and f)    # False
print(t or f)     # True
print(not t)      # False

# None：表示"什么都没有"
n = None
print(n)          # None

# 变量赋值：动态类型，不需要声明
x = 10          # x 现在是 int
print(type(x))    # <class 'int'>
x = "hello"     # x 现在变成了 str，完全合法！
print(type(x))    # <class 'str'>

# 多重赋值
a, b, c = 1, 2, 3
print(a, b, c)    # 1 2 3

# 交换变量值（Python 的优雅写法）
a, b = b, a
print(a, b)     # 2, 1

# 常量：约定用全大写，但 Python 没有真正的常量机制
PI = 3.14159265
MAX_SIZE = 100
print(PI, MAX_SIZE)  # 3.14159265 100

# type() 查看类型
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>
