# 第 49 关：ThreadLocal（师兄带你学 Python）

## 🎯 这一关你会学到

- 为什么多线程里“全局变量”很容易互相串味
- 如何用 `threading.local()` 保存线程私有数据
- ThreadLocal 和普通局部变量、全局变量的区别
- 为什么在线程池里要主动清理 ThreadLocal

## 🤔 先想一个问题

假设你在写一个 Web 服务：每个请求都有自己的用户、请求编号和数据库连接。很多业务函数都要用这些信息，如果每一层函数都写成：

```python
def query_orders(user, request_id, db):
    ...
```

参数会越传越长。可如果把 `current_user` 做成普通全局变量，两个线程同时处理两个用户，请求上下文就可能互相覆盖。

ThreadLocal 提供了一种折中方案：**对象本身是全局的，但对象里的属性按线程隔离**。`Thread-A` 写入的 `request_context.user`，`Thread-B` 看不见。

## 📖 看代码

```python
import threading
from queue import Queue

# ThreadLocal 适合保存“只属于当前线程”的上下文。
# 它看起来像全局对象，但每个线程读写的属性互不影响。
request_context = threading.local()


def bind_context(user, request_id):
    # 给“当前线程”绑定一份请求上下文。
    request_context.user = user
    request_context.request_id = request_id


def query_orders():
    # 业务函数不用层层传 user/request_id，直接读取当前线程的上下文。
    return f"{request_context.request_id} {request_context.user} -> 正在查询订单"


def handle_request(user, request_id, outbox):
    thread_name = threading.current_thread().name

    # 每个线程都会写入同名属性，但实际保存在线程自己的空间里。
    bind_context(user, request_id)

    try:
        outbox.put((thread_name, query_orders()))
    finally:
        # 线程池会复用线程，真实项目里要及时清理，避免下一个任务读到旧上下文。
        del request_context.user
        del request_context.request_id
        outbox.put((thread_name, f"清理后: {getattr(request_context, 'user', None)}"))


if __name__ == "__main__":
    print("=== 主线程没有绑定上下文 ===")
    # 主线程没有设置 user，所以读取不到子线程里的值。
    print(getattr(request_context, "user", None))

    print("\n=== 每个线程有自己的上下文 ===")
    outbox = Queue()
    threads = [
        threading.Thread(target=handle_request, args=("Alice", "req-001", outbox), name="Thread-A"),
        threading.Thread(target=handle_request, args=("Bob", "req-002", outbox), name="Thread-B"),
    ]

    # 启动两个线程，模拟两个请求同时进入系统。
    for thread in threads:
        thread.start()

    # join 会等待子线程执行完，避免主线程提前打印结果。
    for thread in threads:
        thread.join()

    # Queue 是线程安全的，用它收集线程输出比直接 append 列表更稳妥。
    lines = []
    cleanup_lines = []
    while not outbox.empty():
        thread_name, message = outbox.get()
        target = cleanup_lines if message.startswith("清理后") else lines
        target.append((thread_name, message))

    for thread_name, message in sorted(lines):
        print(f"{thread_name}: {message}")

    print("\n=== 处理完成后清理上下文 ===")
    for thread_name, message in sorted(cleanup_lines):
        print(f"{thread_name} {message}")
```

## 🔍 师兄给你拆开讲

`request_context = threading.local()` 创建了一个线程局部对象。它和普通对象一样可以挂属性，但这些属性不是所有线程共享一份，而是每个线程各有一份。

`bind_context()` 在当前线程里写入 `user` 和 `request_id`。当 `Thread-A` 绑定 `Alice` 时，只影响 `Thread-A` 自己；`Thread-B` 绑定 `Bob` 时，也只影响 `Thread-B` 自己。

`query_orders()` 没有接收任何参数，却能拿到当前请求的信息。这就是 ThreadLocal 常见的使用场景：让日志函数、数据库访问函数、权限检查函数能读取“当前线程上下文”，不用把上下文参数从入口一路传到最深层。

`finally` 里的 `del request_context.user` 很重要。普通短生命周期线程结束后，线程局部数据会跟着释放；但线程池里的线程会被复用，如果不清理，下一个任务可能读到上一个任务留下的数据。

## 🏃 跑一下试试

```bash
cd 49-threadlocal
python threadlocal.py
```

你会看到类似输出：

```text
=== 主线程没有绑定上下文 ===
None

=== 每个线程有自己的上下文 ===
Thread-A: req-001 Alice -> 正在查询订单
Thread-B: req-002 Bob -> 正在查询订单

=== 处理完成后清理上下文 ===
Thread-A 清理后: None
Thread-B 清理后: None
```

## 💡 师兄的提醒

ThreadLocal 不是“万能全局变量”。它适合保存请求上下文、日志追踪 ID、每线程数据库连接这类和当前线程强绑定的数据。

如果你只是函数内部临时计算，用普通局部变量就好；如果你要跨线程共享数据，应该用 `Lock`、`Queue`、数据库或其他并发安全结构；如果你在写 `asyncio` 程序，更常用的是 `contextvars`，因为一个线程里可能同时跑多个协程。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `threading.local()` | 创建线程局部存储对象 |
| 线程隔离 | 每个线程只能看到自己设置的属性 |
| `getattr(obj, name, default)` | 读取可能不存在的属性时给默认值 |
| `del request_context.xxx` | 在线程池场景中清理上下文 |
| 使用边界 | 适合线程上下文，不适合跨线程共享数据 |

## ➡️ 下一关

下一关：[正则表达式](../50-regex/README.md)。




