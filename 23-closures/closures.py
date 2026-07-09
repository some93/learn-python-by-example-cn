# 返回函数（闭包）


print("=== 函数可以作为返回值 ===")


def lazy_sum(*args):
    # calc 引用了外层函数的 args，这就形成了闭包。
    def calc():
        total = 0
        for n in args:
            total += n
        return total

    return calc


f = lazy_sum(1, 3, 5, 7, 9)
# 此时还没有真正求和，f 是一个等待调用的函数。
print(type(f).__name__)          # function
print(f.__name__)                # calc
print(f())                       # 25
# __closure__ 可以看到函数是否捕获了外层变量。
print(f.__closure__ is not None) # True
print(len(f.__closure__))        # 1


print("\n=== 每次调用都会返回新函数 ===")

f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
# 参数一样，也会生成两个不同的函数对象。
print(f1 == f2)  # False
print(f1())      # 6
print(f2())      # 6


print("\n=== 循环变量陷阱 ===")


def count_bad():
    funcs = []
    for i in range(1, 4):
        def square():
            # 这里的 i 是外层变量，调用时已经变成循环结束后的 3。
            return i * i

        funcs.append(square)
    return funcs


print([func() for func in count_bad()])  # [9, 9, 9]


print("\n=== 修复循环变量陷阱 ===")


def count_fixed():
    funcs = []
    for i in range(1, 4):
        def square(i=i):
            # 用默认参数把当前 i 的值固定下来。
            return i * i

        funcs.append(square)
    return funcs


print([func() for func in count_fixed()])  # [1, 4, 9]


print("\n=== nonlocal 修改外层变量 ===")


def counter(start=0):
    n = start

    def inc(step=1):
        # nonlocal 表示修改外层函数里的 n，而不是新建局部变量。
        nonlocal n
        n += step
        return n

    return inc


c = counter()
print(c())    # 1
print(c())    # 2
print(c(10))  # 12

c2 = counter(100)
print(c2())   # 101
