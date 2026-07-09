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
