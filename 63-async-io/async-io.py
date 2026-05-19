# 异步 IO（asyncio）

import asyncio

# 协程（coroutine）：用 async def 定义
async def hello():
    print("Hello!")
    await asyncio.sleep(1)    # 异步等待（不阻塞）
    print("World!")

# 运行协程
asyncio.run(hello())

# 并发执行多个协程
async def fetch_data(name, delay):
    print(f"开始获取 {name}...")
    await asyncio.sleep(delay)    # 模拟 IO 操作
    print(f"{name} 获取完成！")
    return f"{name} 的数据"

async def main():
    # 串行执行：总共 3 秒
    print("--- 串行 ---")
    r1 = await fetch_data("A", 1)
    r2 = await fetch_data("B", 2)
    print(f"结果: {r1}, {r2}")

    # 并发执行：只要 2 秒！
    print("\n--- 并发 ---")
    results = await asyncio.gather(
        fetch_data("X", 1),
        fetch_data("Y", 2),
        fetch_data("Z", 1.5),
    )
    print(f"结果: {results}")

asyncio.run(main())

# Task：手动创建任务
async def with_tasks():
    print("\n--- Tasks ---")
    task1 = asyncio.create_task(fetch_data("任务1", 1))
    task2 = asyncio.create_task(fetch_data("任务2", 2))

    # 两个任务已经开始运行了
    r1 = await task1
    r2 = await task2
    print(f"结果: {r1}, {r2}")

asyncio.run(with_tasks())

# 异步 IO 的核心思想：
# 1. 遇到 IO 操作（网络请求、文件读写）时不等待，切换去做别的
# 2. IO 完成后再切回来继续执行
# 3. 单线程就能处理大量并发 IO
# 4. 适合：Web 服务器、爬虫、聊天服务器等 IO 密集型任务
# 5. 不适合：CPU 密集型计算（用多进程）
