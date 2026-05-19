# 第 48 关：多线程（师兄带你学 Python）

## 🎯 这一关你会学到

- 用 `threading.Thread` 创建线程
- 理解多线程共享变量的问题
- 用 `Lock` 解决数据竞争
- 了解 Python 的 GIL

## 🤔 先想一个问题

多线程比多进程轻量，但有个大坑：多个线程同时修改同一个变量，数据会乱掉。这就像两个人同时往一个本子上写字，最后写出来的东西谁都看不懂。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# 多线程（multithreading）

import threading
import time

# 创建线程
def task(name):
    print(f"线程 {name} 开始，ID: {threading.current_thread().name}")
    time.sleep(1)
    print(f"线程 {name} 结束")

t = threading.Thread(target=task, args=('Worker-1',), name='Worker-1')
t.start()
t.join()

# 多线程共享变量的问题
balance = 0

def change_it(n):
    global balance
    for _ in range(1000000):
        balance += n
        balance -= n

t1 = threading.Thread(target=change_it, args=(5,))
t2 = threading.Thread(target=change_it, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"balance = {balance}")    # 可能不是 0！

# 用 Lock 解决
lock = threading.Lock()
balance = 0

def safe_change_it(n):
    global balance
    for _ in range(1000000):
        lock.acquire()
        try:
            balance += n
            balance -= n
        finally:
            lock.release()

t1 = threading.Thread(target=safe_change_it, args=(5,))
t2 = threading.Thread(target=safe_change_it, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"balance (with lock) = {balance}")    # 一定是 0

# Python 的 GIL（全局解释器锁）
# Python 的线程无法利用多核 CPU！
# 计算密集型任务用多进程，IO 密集型任务用多线程

# 更简洁的 lock 用法：with 语句
lock = threading.Lock()

def better_change(n):
    global balance
    for _ in range(100):
        with lock:    # 自动 acquire 和 release
            balance += n
            balance -= n
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- Python 有 GIL（全局解释器锁），多线程无法利用多核 CPU
- 多线程适合 IO 密集型任务（网络请求、文件读写）
- 共享变量一定要加 `Lock`，否则数据会错乱
- `with lock:` 比手动 `acquire/release` 更安全
- 计算密集型任务请用 `multiprocessing` 多进程

## 🏃 跑一下试试

```bash
cd 48-multithreading
python multithreading.py
```

## 💡 师兄的碎碎念

- Python 有 GIL（全局解释器锁），多线程无法利用多核 CPU
- 多线程适合 IO 密集型任务（网络请求、文件读写）
- 共享变量一定要加 `Lock`，否则数据会错乱
- `with lock:` 比手动 `acquire/release` 更安全
- 计算密集型任务请用 `multiprocessing` 多进程

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `Thread(target, args)` | 创建线程 |
| `t.start() / t.join()` | 启动/等待线程 |
| `threading.Lock()` | 创建互斥锁 |
| `with lock:` | 安全的加锁方式 |
| `GIL` | 全局解释器锁，限制多线程并行计算 |

## ➡️ 下一关

下一关我们学习 [ThreadLocal](../49-threadlocal/README.md)，继续加油！
