# contextlib

from contextlib import contextmanager, closing

# 回顾：with 语句需要上下文管理器（__enter__ + __exit__）
class MyResource:
    def __enter__(self):
        print("打开资源")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭资源")
        return False    # 不吞掉异常

with MyResource() as r:
    print("使用资源")

# 用 @contextmanager 简化！
@contextmanager
def my_resource():
    print("打开资源")
    try:
        yield "资源对象"    # yield 之前是 __enter__
    finally:
        print("关闭资源")    # yield 之后是 __exit__

with my_resource() as r:
    print(f"使用: {r}")

# 实用例子：计时器
import time

@contextmanager
def timer(name):
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"{name} 耗时: {elapsed:.3f}s")

with timer("计算"):
    total = sum(range(1000000))
    print(f"结果: {total}")

# 实用例子：临时修改工作目录
import os

@contextmanager
def change_dir(path):
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

# closing()：为没有 __exit__ 的对象加上 close() 调用
class Connection:
    def __init__(self):
        print("连接已建立")

    def close(self):
        print("连接已关闭")

with closing(Connection()) as conn:
    print("使用连接")
# 自动调用 conn.close()
