# 装饰器（Decorator）

import functools
import time

# 最基本的装饰器：打印日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper

@log
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# 调用 say_hello()
# Hello!

# @log 等价于 say_hello = log(say_hello)

# 带参数的装饰器
def log_with_prefix(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] 调用 {func.__name__}()")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_prefix("DEBUG")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 计时装饰器
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时 {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(0.1)
    return "done"

print(slow_func())

# functools.wraps 保留原函数信息
print(say_hello.__name__)   # say_hello（不是 wrapper）
