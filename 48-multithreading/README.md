# 第 48 关：多线程（师兄带你学 Python）

## 🎯 这一关你会学到

- `threading.Thread` 如何创建线程
- `start()` 和 `join()` 的作用
- 多线程共享变量为什么会出现数据竞争
- `Lock` 如何保护临界区
- GIL 下多线程适合什么场景

## 🤔 先想一个问题

多线程像一家店里多个员工同时干活。一个人负责接电话，一个人负责打包，一个人负责查库存，效率确实高。

但如果两个人同时改同一本账本，又没有排队规则，账就可能写乱。

这就是多线程的核心矛盾：共享数据方便，但也危险。

## 📖 看代码

```python
# 多线程（multithreading）

import threading
import time


print("=== 创建线程 ===")


def task(name):
    print(f"{name} 开始")
    # sleep 模拟耗时任务，让线程切换更容易观察。
    time.sleep(0.1)
    print(f"{name} 结束")


# target 指定线程函数，name 方便日志和调试。
thread = threading.Thread(target=task, args=("Worker-1",), name="Worker-1")
thread.start()
# join 等待线程结束。
thread.join()
print(thread.is_alive())  # False


print("\n=== 共享变量的数据竞争 ===")

counter = 0
# Barrier 让两个线程都读完 counter 后再继续写，稳定复现竞争问题。
barrier = threading.Barrier(2)


def unsafe_add_one():
    global counter
    # 两个线程可能读到同一个旧值。
    current = counter
    barrier.wait()
    # 再各自写回 current + 1，导致一次更新丢失。
    counter = current + 1


t1 = threading.Thread(target=unsafe_add_one)
t2 = threading.Thread(target=unsafe_add_one)
t1.start()
t2.start()
t1.join()
t2.join()
print(counter)  # 1


print("\n=== 用 Lock 保护共享变量 ===")

counter = 0
lock = threading.Lock()


def safe_add_one():
    global counter
    # with lock 保证同一时间只有一个线程修改 counter。
    with lock:
        current = counter
        counter = current + 1


t1 = threading.Thread(target=safe_add_one)
t2 = threading.Thread(target=safe_add_one)
t1.start()
t2.start()
t1.join()
t2.join()
print(counter)  # 2


print("\n=== 多线程适合 IO 等待 ===")


def fake_download(name):
    # IO 等待期间线程可以切换去做别的任务。
    time.sleep(0.1)
    print(f"{name} 下载完成")


threads = [
    threading.Thread(target=fake_download, args=("file-a",)),
    threading.Thread(target=fake_download, args=("file-b",)),
]

for item in threads:
    item.start()
for item in threads:
    item.join()

print("全部完成")
```

## 🔍 师兄给你逐行拆

### 创建线程

```python
thread = threading.Thread(target=task, args=("Worker-1",), name="Worker-1")
thread.start()
thread.join()
```

**这行在干嘛？**

`Thread` 创建线程对象。

- `target` 是线程要执行的函数；
- `args` 是传给函数的参数；
- `name` 是线程名字，方便调试；
- `start()` 启动线程；
- `join()` 等线程结束。

`thread.is_alive()` 可以判断线程是否还活着。`join()` 之后当然是 `False`。

---

### 数据竞争：两个线程同时改一个变量

```python
counter = 0
barrier = threading.Barrier(2)

def unsafe_add_one():
    global counter
    current = counter
    barrier.wait()
    counter = current + 1
```

**这行在干嘛？**

两个线程都先读取 `counter`，然后在 `barrier.wait()` 等对方。等两个线程都读完后，再各自写回 `current + 1`。

它们都读到 `0`，所以都写回 `1`。两个线程各加一次，结果却是 `1`，不是 `2`。

**为什么这是 bug？**

`counter += 1` 看起来是一行，但背后包含读取、计算、写回多个步骤。线程切换可能发生在中间。

---

### `Lock`：给临界区上锁

```python
lock = threading.Lock()

def safe_add_one():
    global counter
    with lock:
        current = counter
        counter = current + 1
```

**这行在干嘛？**

`with lock:` 里的代码同一时间只允许一个线程执行。

这段被保护的代码叫临界区。两个线程排队进入临界区，结果就能正确变成 `2`。

**为什么推荐 `with lock`？**

它会自动 acquire 和 release。比手写：

```python
lock.acquire()
try:
    ...
finally:
    lock.release()
```

更短，也更不容易忘记释放锁。

---

### 多线程适合 IO 等待

```python
def fake_download(name):
    time.sleep(0.1)
    print(f"{name} 下载完成")
```

**这行在干嘛？**

`time.sleep()` 模拟网络下载等待。等待期间线程不需要 CPU，可以切到其他线程做事。

这就是 Python 多线程最适合的场景：网络请求、文件读写、数据库查询这类 IO 密集型任务。

---

### GIL 是什么？

Python 的 CPython 解释器有 GIL，全局解释器锁。它让同一时刻通常只有一个线程执行 Python 字节码。

所以多线程不适合用来加速 CPU 密集型任务，比如大量纯 Python 数学计算。那类任务更适合多进程。

但 IO 等待时，线程会释放执行机会，所以多线程仍然很有用。

## 🏃 跑一下试试

```bash
$ python multithreading.py
=== 创建线程 ===
Worker-1 开始
Worker-1 结束
False

=== 共享变量的数据竞争 ===
1

=== 用 Lock 保护共享变量 ===
2

=== 多线程适合 IO 等待 ===
file-a 下载完成
file-b 下载完成
全部完成
```

## 💡 师兄的碎碎念

- `Thread` 比 `Process` 轻量，但线程共享同一进程内存。
- 共享变量只要有读改写，就要考虑锁。
- `with lock:` 是更安全的加锁写法。
- Python 多线程适合 IO 密集型任务，不适合加速纯 Python CPU 密集型任务。
- 锁用多了也可能导致死锁，所以临界区要尽量短。

## 🎓 这一关的知识点清单

- **Thread**：线程对象，运行一个目标函数。
- **start/join**：启动线程和等待线程结束。
- **数据竞争**：多个线程同时读写共享状态导致结果错误。
- **Lock**：互斥锁，保护临界区。
- **Barrier**：让多个线程在某个点互相等待，本章用来稳定演示竞争。
- **GIL**：CPython 的全局解释器锁，影响 CPU 密集型多线程并行。

## ➡️ 下一关

共享变量要加锁，但有些数据本来就应该每个线程各用各的。下一关看 ThreadLocal：看起来像全局变量，实际每个线程都有自己的副本 👉 [下一关：ThreadLocal →](../49-threadlocal/)


