# 第 47 关：多进程（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `Process` 创建子进程
- 用 `Pool` 批量创建进程
- 用 `Queue` 实现进程间通信
- 理解多进程的适用场景

## 🤔 先想一个问题

你的电脑有 8 个 CPU 核心，但 Python 程序默认只用 1 个。想让计算密集型任务跑满所有核心？用**多进程**！

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 多进程（multiprocessing）

import os
import multiprocessing
import time

# 获取当前进程 ID
print(f"主进程 PID: {os.getpid()}")

# 用 Process 创建子进程
def child_task(name):
    print(f"子进程 {name} 运行中，PID: {os.getpid()}, 父进程: {os.getppid()}")
    time.sleep(1)
    print(f"子进程 {name} 结束")

if __name__ == '__main__':
    print("--- Process ---")
    p = multiprocessing.Process(target=child_task, args=('test',))
    p.start()
    p.join()    # 等待子进程结束
    print("主进程结束")

    # 用 Pool 批量创建进程
    print("\n--- Pool ---")
    def task(n):
        print(f"任务 {n} 运行中，PID: {os.getpid()}")
        time.sleep(0.5)
        return n * n

    with multiprocessing.Pool(4) as pool:
        results = pool.map(task, range(5))
    print(f"结果: {results}")

    # 进程间通信：Queue
    print("\n--- Queue ---")
    def writer(q):
        for i in range(5):
            q.put(f"消息 {i}")
            time.sleep(0.1)

    def reader(q):
        while True:
            msg = q.get()
            if msg == 'STOP':
                break
            print(f"收到: {msg}")

    q = multiprocessing.Queue()
    pw = multiprocessing.Process(target=writer, args=(q,))
    pr = multiprocessing.Process(target=reader, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    q.put('STOP')
    pr.join()
    print("通信结束")
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `multiprocessing` 模块在 Windows 上必须在 `if __name__ == '__main__'` 里用
- `Pool(4)` 创建 4 个进程的进程池，`pool.map()` 自动分配任务
- 进程间不共享内存，通信用 `Queue` 或 `Pipe`
- 计算密集型任务用多进程，IO 密集型用多线程或异步
- 每个子进程都有独立的 PID，可以用 `os.getpid()` 查看

## 🏃 跑一下试试

```bash
cd 47-multiprocessing
python multiprocessing_demo.py
```

## 💡 师兄的碎碎念

- `multiprocessing` 模块在 Windows 上必须在 `if __name__ == '__main__'` 里用
- `Pool(4)` 创建 4 个进程的进程池，`pool.map()` 自动分配任务
- 进程间不共享内存，通信用 `Queue` 或 `Pipe`
- 计算密集型任务用多进程，IO 密集型用多线程或异步
- 每个子进程都有独立的 PID，可以用 `os.getpid()` 查看

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `Process(target, args)` | 创建子进程 |
| `p.start() / p.join()` | 启动/等待子进程 |
| `Pool(n)` | 创建 n 个进程的进程池 |
| `pool.map(func, iterable)` | 并行执行任务 |
| `Queue` | 进程间安全通信的队列 |

## ➡️ 下一关

下一关我们学习 [多线程](../48-multithreading/README.md)，继续加油！
