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
