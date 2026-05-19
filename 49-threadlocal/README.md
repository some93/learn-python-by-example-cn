# 第 49 关：ThreadLocal（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解多线程中传递局部变量的问题
- 用 `threading.local()` 创建线程局部变量
- 理解 ThreadLocal 的工作原理

## 🤔 先想一个问题

多线程中，每个线程想有自己的「私有变量」，但又不想层层传参。有没有一种全局变量，每个线程只能看到自己的值？这就是 **ThreadLocal**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `threading.local()` 创建的对象，每个线程独立拥有自己的属性值
- 不需要加锁，不需要传参数，最优雅的线程局部存储
- 常用场景：数据库连接、请求上下文、用户会话信息
- Flask 框架的 `request` 对象底层就是用 ThreadLocal 实现的

## 🏃 跑一下试试

```bash
cd 49-threadlocal
python threadlocal.py
```

## 💡 师兄的碎碎念

- `threading.local()` 创建的对象，每个线程独立拥有自己的属性值
- 不需要加锁，不需要传参数，最优雅的线程局部存储
- 常用场景：数据库连接、请求上下文、用户会话信息
- Flask 框架的 `request` 对象底层就是用 ThreadLocal 实现的

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `threading.local()` | 创建线程局部存储对象 |
| `local_data.xxx = ...` | 设置线程局部变量 |
| `线程隔离` | 每个线程只能看到自己设置的值 |

## ➡️ 下一关

下一关我们学习 [正则表达式](../50-regex/README.md)，继续加油！
