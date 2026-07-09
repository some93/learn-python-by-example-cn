# 装饰器（Decorator）

import functools


print("=== 最基本的装饰器 ===")


def log(func):
    # wrapper 会包住原函数，在调用前后插入额外逻辑。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}()")
        # 装饰器要把原函数的返回值继续返回出去。
        return func(*args, **kwargs)

    return wrapper


# @log 等价于 say_hello = log(say_hello)。
@log
def say_hello():
    print("Hello!")


say_hello()                # 调用 say_hello() / Hello!
print(say_hello.__name__)  # say_hello


print("\n=== @ 语法糖的本质 ===")


def greet(name):
    print(f"Hello, {name}!")


# 手动改写函数变量，可以看清 @ 语法糖的本质。
greet = log(greet)
greet("Alice")  # 调用 greet() / Hello, Alice!


print("\n=== 装饰器必须返回原函数结果 ===")


@log
def add(a, b):
    return a + b


print(add(3, 5))  # 先输出：调用 add()，再输出：8


print("\n=== 带参数的装饰器 ===")


def log_with_prefix(prefix):
    # 带参数的装饰器需要多包一层，用来接收装饰器自己的参数。
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] 调用 {func.__name__}()")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_with_prefix("DEBUG")
def fetch_data(url):
    return f"数据来自 {url}"


print(fetch_data("https://example.com"))  # 先输出：[DEBUG] 调用 fetch_data()，再输出：数据来自 https://example.com


print("\n=== 统计调用次数的装饰器 ===")


def count_calls(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # count 在外层函数里，修改它需要 nonlocal。
        nonlocal count
        count += 1
        print(f"{func.__name__} 第 {count} 次调用")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def double(x):
    return x * 2


print(double(10))  # 先输出：double 第 1 次调用，再输出：20
print(double(20))  # 先输出：double 第 2 次调用，再输出：40
