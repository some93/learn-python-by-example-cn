# 匿名函数（lambda）

# lambda 语法：lambda 参数: 表达式
f = lambda x: x * x
print(f(5))    # 25

# 等价于
def f2(x):
    return x * x

# lambda 常用于排序的 key 参数
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)

# 配合 map 使用
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# 配合 filter 使用
print(list(filter(lambda x: x % 2 == 1, range(1, 11))))

# lambda 也可以赋值给变量（但不推荐，直接用 def 更清晰）
add = lambda x, y: x + y
print(add(3, 5))   # 8

# lambda 作为返回值
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
print(add5(10))    # 15

# lambda 只能写一个表达式，不能写多条语句
# lambda x: print(x); return x  # SyntaxError!
