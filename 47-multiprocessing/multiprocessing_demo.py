# 多进程（multiprocessing）

import os
from multiprocessing import Process


def child_task(name):
    # 子进程会执行这个函数；flush=True 让输出更及时。
    print(f"子进程 {name} 收到任务", flush=True)


def main():
    print("=== 当前进程 ===", flush=True)
    # getpid() 返回当前进程 ID。
    print(os.getpid() > 0, flush=True)

    print("\n=== Process 创建子进程 ===", flush=True)
    # target 指定子进程要执行的函数，args 传入函数参数。
    process = Process(target=child_task, args=("worker",))
    process.start()
    # join 等待子进程结束，避免主进程提前退出。
    process.join()
    print(process.exitcode, flush=True)

    print("\n=== 主进程继续执行 ===", flush=True)
    print("子进程已结束", flush=True)


if __name__ == "__main__":
    # Windows 下创建子进程必须把启动逻辑放在这个保护里。
    main()
