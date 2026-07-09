# 第 47 关：多进程

## 🎯 这一关你会学到

- `multiprocessing.Process` 如何创建子进程
- `start()` 和 `join()` 的作用
- `Pool` 如何批量执行任务
- `Queue` 如何做进程间通信
- 为什么 Windows 下必须写 `if __name__ == "__main__"`

## 🤔 先想一个问题

你的电脑有多个 CPU 核心，但一个普通 Python 程序默认只有一个主进程在跑。

如果任务是计算密集型，比如大量图片处理、压缩、加密、数学计算，想更好利用多核 CPU，就可以考虑多进程。

多进程像开多家分店：每家店有自己的收银台和库存，互不共享内存；要沟通，就得通过队列、管道这类通道。

## 📖 看代码

```python
# 多进程（multiprocessing）

import os
from multiprocessing import Process


def child_task(name):
    # 子进程会执行这个函数；flush=True 让输出更及时。
    print(f"子进程 {name} 收到任务", flush=True)


def main():
    print("=== 当前进程 ===", flush=True)
    # getpid() 返回当前进程 ID。
    print(os.getpid() > 0, flush=True)  # True

    print("\n=== Process 创建子进程 ===", flush=True)
    # target 指定子进程要执行的函数，args 传入函数参数。
    process = Process(target=child_task, args=("worker",))
    process.start()
    # join 等待子进程结束，避免主进程提前退出。
    process.join()
    print(process.exitcode, flush=True)  # 0

    print("\n=== 主进程继续执行 ===", flush=True)
    print("子进程已结束", flush=True)


if __name__ == "__main__":
    # Windows 下创建子进程必须把启动逻辑放在这个保护里。
    main()
```

## 🔍 师兄给你逐行拆

### 顶层函数很重要

```python
def child_task(name):
    print(f"子进程 {name} 收到任务")
```

**这行在干嘛？**

这是子进程要执行的任务函数。

**为什么放在文件顶层？**

在 Windows 上，多进程启动新进程时需要重新导入当前模块。目标函数通常必须能被 pickle 找到。嵌套函数、lambda 往往会出问题。

所以多进程任务函数尽量写在模块顶层。

---

### `Process`：手动创建一个子进程

```python
process = multiprocessing.Process(target=child_task, args=("worker",))
process.start()
process.join()
print(process.exitcode)
```

**这行在干嘛？**

`Process` 创建子进程对象。

- `target`：子进程要运行的函数；
- `args`：传给函数的位置参数；
- `start()`：真正启动子进程；
- `join()`：主进程等待子进程结束；
- `exitcode`：退出码，`0` 通常表示正常结束。

**生活类比**

你派一个同学去取快递，`start()` 是让他出发，`join()` 是你在原地等他回来。

---

### `Pool`：批量分发任务

```python
from multiprocessing import Pool

with Pool(2) as pool:
    results = pool.map(square, [1, 2, 3, 4])
print(results)
```

**这行在干嘛？**

`Pool(2)` 创建一个有 2 个工作进程的进程池。

`pool.map(square, [1, 2, 3, 4])` 把任务分发给进程池，结果按输入顺序返回：

```python
[1, 4, 9, 16]
```

**为什么用 Pool？**

当你有一批相似任务时，不想手动创建一堆 `Process`，进程池更方便。

---

### `Queue`：进程间通信

```python
from multiprocessing import Process, Queue

queue = Queue()
reader_process = Process(target=reader, args=(queue,))
writer_process = Process(target=writer, args=(queue,))
```

**这行在干嘛？**

进程之间默认不共享普通变量。要传消息，可以用 `multiprocessing.Queue`。

`writer()` 往队列里放消息，`reader()` 从队列里取消息。

`STOP` 是结束信号，告诉 reader 没有更多消息了。

**为什么示例代码没有直接跑 Pool 和 Queue？**

有些受限教学环境会禁止创建 multiprocessing 的管道或进程池，导致 `Pool` / `Queue` 报权限错误。为了保证本关代码能稳定运行，`.py` 文件只演示最基础的 `Process`；`Pool` 和 `Queue` 的标准写法放在 README 里讲。

---

### Windows 入口保护

```python
if __name__ == "__main__":
    main()
```

**这行在干嘛？**

Windows 下多进程会重新导入当前模块。如果没有入口保护，导入时又创建新进程，新进程再导入，再创建，可能无限套娃。

所以多进程代码必须放进：

```python
if __name__ == "__main__":
```

这不是可选礼仪，是 Windows 多进程的基本要求。

## 🏃 跑一下试试

```bash
$ python multiprocessing_demo.py
=== 当前进程 ===
True

=== Process 创建子进程 ===
子进程 worker 收到任务
0

=== 主进程继续执行 ===
子进程已结束
```

## 💡 师兄的碎碎念

- 多进程适合计算密集型任务，多线程更适合 IO 密集型任务。
- Windows 下使用 `multiprocessing` 必须加 `if __name__ == "__main__"`。
- 多进程任务函数尽量写在模块顶层，别用嵌套函数或 lambda。
- 进程之间不共享普通内存，通信要用 `Queue`、`Pipe` 或共享内存工具。
- `Pool.map()` 会保持结果顺序和输入顺序一致。

## 🎓 这一关的知识点清单

- **Process**：创建一个子进程。
- **start/join**：启动进程和等待进程结束。
- **exitcode**：子进程退出码。
- **Pool**：进程池，批量执行任务。
- **Queue**：进程间安全传递消息。
- **入口保护**：Windows 多进程必须使用 `if __name__ == "__main__"`。

## ➡️ 下一关

多进程是多家分店，多线程则是一家店里多个员工。下一关看多线程、共享变量和锁 👉 [下一关：多线程 →](../48-multithreading/)


