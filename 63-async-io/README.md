# 第 63 关：异步 IO（师兄带你学 Python）

## 🎯 这一关你会学到

- `async def` 定义的是什么
- `await` 为什么能让出执行权
- `asyncio.run()` 为什么是异步程序入口
- 串行等待和 `asyncio.gather()` 并发等待的区别
- `asyncio.create_task()` 如何手动创建任务
- `asyncio.wait_for()` 如何控制超时
- `gather(return_exceptions=True)` 如何收集异常

## 🤔 先想一个问题

一个接口要等数据库，一个爬虫要等网页响应，一个聊天服务器要等客户端消息。等待 IO 的时候，CPU 其实没什么事可做。

异步 IO 的核心思想是：**遇到等待就把执行权让出去，先处理别的任务；等 IO 好了，再切回来继续执行**。

它适合 IO 密集型任务，不适合让 CPU 密集型计算自动变快。

## 📖 看代码

```python
# 异步 IO（asyncio）

import asyncio


async def say_hello():
    # asyncio.sleep 是异步等待，不会阻塞事件循环。
    await asyncio.sleep(0.01)
    return "Hello, asyncio"


async def fetch_data(name, delay):
    # 这个函数模拟一次网络/数据库 IO。
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 完成")
    return f"{name} 的数据"


async def fail_later():
    await asyncio.sleep(0.01)
    raise ValueError("模拟失败")


async def main():
    print("=== 协程对象和 await ===")
    # 调用 async 函数只会得到 coroutine，还没有真正跑函数体。
    coroutine = say_hello()
    print(type(coroutine).__name__)  # coroutine
    print(await coroutine)  # Hello, asyncio

    print("\n=== 串行执行 ===")
    # 串行 await 会等前一个完成后，再开始下一个。
    first = await fetch_data("A", 0.03)  # A 开始 / A 完成
    second = await fetch_data("B", 0.03)  # B 开始 / B 完成
    print([first, second])  # ['A 的数据', 'B 的数据']

    print("\n=== gather 并发执行 ===")
    # gather 会并发调度多个协程，但返回结果保持传入顺序。
    results = await asyncio.gather(
        fetch_data("X", 0.03),
        fetch_data("Y", 0.06),
        fetch_data("Z", 0.04),
    )  # X 开始 / Y 开始 / Z 开始 / X 完成 / Z 完成 / Y 完成（开始顺序通常如此，调度细节可能不同）
    print(results)  # ['X 的数据', 'Y 的数据', 'Z 的数据']

    print("\n=== create_task 手动创建任务 ===")
    task1 = asyncio.create_task(fetch_data("任务1", 0.03))
    task2 = asyncio.create_task(fetch_data("任务2", 0.03))

    # create_task 后任务已经交给事件循环调度，await 只是等待结果。
    print(task1.done(), task2.done())  # False False
    task_results = await asyncio.gather(task1, task2)  # 任务1 开始 / 任务2 开始 / 任务1 完成 / 任务2 完成（顺序可能不同）
    print(task_results)  # ['任务1 的数据', '任务2 的数据']

    print("\n=== wait_for 超时控制 ===")
    try:
        # 超时后，wait_for 会取消内部任务并抛 TimeoutError。
        await asyncio.wait_for(fetch_data("慢任务", 0.2), timeout=0.05)  # 慢任务 开始
    except asyncio.TimeoutError as error:
        print(type(error).__name__)  # TimeoutError

    print("\n=== gather 收集异常 ===")
    # return_exceptions=True 让异常作为结果返回，适合批量任务汇总。
    mixed = await asyncio.gather(
        fetch_data("正常任务", 0.01),
        fail_later(),
        return_exceptions=True,
    )  # 正常任务 开始 / 正常任务 完成
    print([type(item).__name__ if isinstance(item, Exception) else item for item in mixed])  # ['正常任务 的数据', 'ValueError']


if __name__ == "__main__":
    # asyncio.run 是异步程序的入口，负责创建和关闭事件循环。
    asyncio.run(main())
```

## 🔍 师兄给你拆开讲

调用 `async def` 函数不会立刻执行函数体，而是返回一个 coroutine 对象。只有 `await coroutine` 或交给事件循环调度，它才会真正运行。

`await` 的意思不是“阻塞线程傻等”，而是“当前协程暂停，把控制权交还给事件循环”。事件循环可以去运行其他已经准备好的协程。

串行写法：

```python
first = await fetch_data("A", 0.03)
second = await fetch_data("B", 0.03)
```

会等 A 完成后才开始 B。

`asyncio.gather()` 会同时调度多个协程，结果顺序仍然按传入顺序返回，不按完成先后返回。

`create_task()` 会把协程包装成任务并立即交给事件循环调度。它适合你想先启动任务，后面再等待结果的场景。

`wait_for()` 给一个异步操作加超时，超时后抛 `asyncio.TimeoutError`。网络请求、队列等待、远程调用都应该考虑超时。

默认情况下，`gather()` 中任何一个任务抛异常，整体会抛异常。设置 `return_exceptions=True` 后，异常会作为结果返回，适合批量任务“有的成功、有的失败”的场景。

## 🏃 跑一下试试

```bash
cd 63-async-io
python async-io.py
```

输出：

```text
=== 协程对象和 await ===
coroutine
Hello, asyncio

=== 串行执行 ===
A 开始
A 完成
B 开始
B 完成
['A 的数据', 'B 的数据']

=== gather 并发执行 ===
X 开始
Y 开始
Z 开始
X 完成
Z 完成
Y 完成
['X 的数据', 'Y 的数据', 'Z 的数据']

=== create_task 手动创建任务 ===
False False
任务1 开始
任务2 开始
任务1 完成
任务2 完成
['任务1 的数据', '任务2 的数据']

=== wait_for 超时控制 ===
慢任务 开始
TimeoutError

=== gather 收集异常 ===
正常任务 开始
正常任务 完成
['正常任务 的数据', 'ValueError']
```

## 💡 师兄的提醒

异步 IO 不等于多线程。大多数 asyncio 程序仍然运行在单线程事件循环里，只是在等待 IO 时切换任务。

不要在协程里直接调用耗时的阻塞函数，比如 `time.sleep()`、同步网络请求、大量 CPU 计算。它们会卡住整个事件循环。等待用 `await asyncio.sleep()`，HTTP 客户端用异步库，CPU 密集型任务考虑多进程或线程池。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `async def` | 定义协程函数 |
| coroutine | 调用协程函数得到的协程对象 |
| `await` | 等待异步操作并让出执行权 |
| `asyncio.run()` | 启动异步程序入口 |
| `asyncio.sleep()` | 异步等待 |
| `asyncio.gather()` | 并发等待多个协程 |
| `asyncio.create_task()` | 创建并调度任务 |
| `asyncio.wait_for()` | 给协程加超时 |
| `return_exceptions=True` | 把异常作为结果收集 |
| IO 密集型 | 异步 IO 适合的主要场景 |

## ➡️ 下一步

63 关到这里全部结束。接下来建议找一个小项目练手，比如命令行记账工具、待办事项 Web API、文件整理脚本或简单爬虫。教程知识要变成能力，最终还是要靠项目把它串起来。

