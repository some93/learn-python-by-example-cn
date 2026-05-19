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
