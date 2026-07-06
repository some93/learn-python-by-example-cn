# contextlib 上下文管理工具

from contextlib import ExitStack, closing, contextmanager, redirect_stdout, suppress
from io import StringIO


print("=== 手写上下文管理器 ===")


class Resource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # __enter__ 的返回值会绑定给 as 后面的变量。
        print(f"打开 {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # __exit__ 无论 with 内部是否异常都会执行。
        print(f"关闭 {self.name}")
        return False


with Resource("文件") as resource:
    print(f"使用 {resource.name}")


print("\n=== @contextmanager 简化写法 ===")


@contextmanager
def managed_resource(name):
    print(f"打开 {name}")
    try:
        # yield 之前相当于 __enter__，yield 的值会交给 as 变量。
        yield name
    finally:
        # finally 里的代码相当于 __exit__，负责清理资源。
        print(f"关闭 {name}")


with managed_resource("数据库连接") as name:
    print(f"使用 {name}")


print("\n=== suppress 忽略指定异常 ===")

with suppress(ValueError):
    # 只忽略指定异常，适合“失败也没关系”的小范围代码。
    int("not-a-number")

print("程序继续执行")


print("\n=== closing 自动调用 close() ===")


class Connection:
    def __init__(self):
        print("连接已建立")

    def close(self):
        print("连接已关闭")


with closing(Connection()) as connection:
    print(type(connection).__name__)


print("\n=== redirect_stdout 捕获输出 ===")

buffer = StringIO()

# redirect_stdout 临时把 print 输出重定向到 file-like object。
with redirect_stdout(buffer):
    print("第一行")
    print("第二行")

print(buffer.getvalue().splitlines())


print("\n=== ExitStack 管理多个资源 ===")

with ExitStack() as stack:
    # enter_context 可以动态进入多个上下文管理器。
    first = stack.enter_context(managed_resource("缓存"))
    second = stack.enter_context(managed_resource("日志"))
    print(f"使用 {first} 和 {second}")

# ExitStack 退出时会按后进先出的顺序清理资源。
print("全部资源已释放")
