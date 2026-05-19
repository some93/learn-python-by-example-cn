# 返回函数（闭包）

# 函数作为返回值
def lazy_sum(*args):
    def calc():
        total = 0
        for n in args:
            total += n
        return total
    return calc       # 返回的是函数，不是结果

f = lazy_sum(1, 3, 5, 7, 9)
print(f)              # <function lazy_sum.<locals>.calc at 0x...>
print(f())            # 25（调用时才真正计算）

# 每次调用返回一个新的函数
f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
print(f1 == f2)       # False（不同的函数对象）

# 闭包陷阱：循环变量被捕获
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())   # 9 9 9（全是9！不是1 4 9）

# 修复：用参数绑定当前值
def count_fixed():
    fs = []
    for i in range(1, 4):
        def f(i=i):       # 用默认参数绑定
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count_fixed()
print(f1(), f2(), f3())   # 1 4 9（正确！）

# nonlocal：在闭包中修改外层变量
def counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c = counter()
print(c())   # 1
print(c())   # 2
print(c())   # 3
