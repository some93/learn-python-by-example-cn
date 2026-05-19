# ThreadLocal

import threading

# 问题：多线程中每个线程想有自己的"局部变量"
# 方法1：传参数（麻烦）
# 方法2：用全局 dict（需要加锁）
# 方法3：用 threading.local（最优雅！）

# 创建 ThreadLocal 对象
local_data = threading.local()

def process_student():
    # 每个线程可以独立设置和读取 local_data 的属性
    name = local_data.name
    print(f"线程 {threading.current_thread().name}: Hello, {name}!")

def thread_func(name):
    # 绑定线程局部变量
    local_data.name = name
    process_student()

# 不同线程设置不同的值，互不干扰
t1 = threading.Thread(target=thread_func, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=thread_func, args=('Bob',), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal 的本质：
# 一个全局对象，但每个线程只能访问自己设置的值
# 不需要加锁，不需要传参数，简洁又安全

# 没有 ThreadLocal 时的笨办法
students = {}

def old_way(name):
    tid = threading.current_thread().name
    students[tid] = name    # 需要锁！
    print(f"{tid}: {students[tid]}")

# 用 ThreadLocal 后的优雅写法：直接 local_data.xxx 就行
