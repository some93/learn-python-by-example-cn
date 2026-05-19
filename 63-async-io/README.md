# 第 63 关：异步IO（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解异步 IO 的概念
- 用 `async/await` 编写协程
- 用 `asyncio.gather` 并发执行
- 用 `asyncio.create_task` 创建任务

## 🤔 先想一个问题

你的服务器要同时处理 1000 个用户请求，每个请求都要等数据库返回。用多线程？1000 个线程太浪费。用**异步 IO**，单线程就能搞定——等 IO 的时候不傻等，切去处理别的请求。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `async def` 定义协程，`await` 等待异步操作完成
- `asyncio.gather()` 并发运行多个协程，比串行快得多
- `asyncio.run()` 是启动异步程序的入口
- 异步 IO 适合 IO 密集型任务，不适合 CPU 密集型计算
- FastAPI 是基于 asyncio 的现代 Web 框架，性能远超 Flask

## 🏃 跑一下试试

```bash
cd 63-async-io
python async-io.py
```

## 💡 师兄的碎碎念

- `async def` 定义协程，`await` 等待异步操作完成
- `asyncio.gather()` 并发运行多个协程，比串行快得多
- `asyncio.run()` 是启动异步程序的入口
- 异步 IO 适合 IO 密集型任务，不适合 CPU 密集型计算
- FastAPI 是基于 asyncio 的现代 Web 框架，性能远超 Flask

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `async def func()` | 定义协程函数 |
| `await coroutine` | 等待协程完成 |
| `asyncio.run(main())` | 运行异步程序 |
| `asyncio.gather(*coros)` | 并发执行多个协程 |
| `asyncio.create_task(coro)` | 创建异步任务 |
| `asyncio.sleep(n)` | 异步等待（不阻塞） |

## ➡️ 下一关

恭喜你！全部 63 关通关完成！你已经掌握了 Python 从入门到进阶的核心知识。接下来去写项目吧，实战才是最好的老师！
