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
print(thread.is_alive())


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
print(counter)


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
print(counter)


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
