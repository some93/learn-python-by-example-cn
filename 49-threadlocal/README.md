# 第 49 关：ThreadLocal

## 🎯 这一关你会学到

- `threading.local()` 是什么、解决什么问题
- 为什么不用全局变量保存“当前请求”的上下文
- ThreadLocal 看起来像全局对象，实际每个线程各存各的
- 线程池复用线程时，为什么要及时清理 ThreadLocal

## 🤔 先想一个问题

一个 Web 请求进来，你要在好几层函数里用 `user` 和 `request_id`：处理参数、查订单、写日志。

最直觉的写法是把 `user`、`request_id` 当参数一层层往下传。函数签名越传越胖，加一个字段就得改一串函数。

另一个办法是放进一个全局变量 `current_request`。但服务器是多个线程同时处理不同请求的，A 线程刚写进去，B 线程可能就覆盖了，串号了。

有没有一种东西，看起来像全局变量，每个线程却只能看到自己那份？这就是 **ThreadLocal**。

## 📖 看代码

```python
import threading
from queue import Queue

# ThreadLocal 适合保存“只属于当前线程”的上下文。
# 它看起来像全局对象，但每个线程读写的属性互不影响。
request_context = threading.local()


def bind_context(user, request_id):
    # 给“当前线程”绑定一份请求上下文。
    request_context.user = user
    request_context.request_id = request_id


def query_orders():
    # 业务函数不用层层传 user/request_id，直接读取当前线程的上下文。
    return f"{request_context.request_id} {request_context.user} -> 正在查询订单"


def handle_request(user, request_id, outbox):
    thread_name = threading.current_thread().name

    # 每个线程都会写入同名属性，但实际保存在线程自己的空间里。
    bind_context(user, request_id)

    try:
        outbox.put((thread_name, query_orders()))
    finally:
        # 线程池会复用线程，真实项目里要及时清理，避免下一个任务读到旧上下文。
        del request_context.user
        del request_context.request_id
        outbox.put((thread_name, f"清理后: {getattr(request_context, 'user', None)}"))


if __name__ == "__main__":
    print("=== 主线程没有绑定上下文 ===")
    # 主线程没有设置 user，所以读取不到子线程里的值。
    print(getattr(request_context, "user", None))  # None

    print("\n=== 每个线程有自己的上下文 ===")
    outbox = Queue()
    threads = [
        threading.Thread(target=handle_request, args=("Alice", "req-001", outbox), name="Thread-A"),
        threading.Thread(target=handle_request, args=("Bob", "req-002", outbox), name="Thread-B"),
    ]

    # 启动两个线程，模拟两个请求同时进入系统。
    for thread in threads:
        thread.start()

    # join 会等待子线程执行完，避免主线程提前打印结果。
    for thread in threads:
        thread.join()

    # Queue 是线程安全的，用它收集线程输出比直接 append 列表更稳妥。
    lines = []
    cleanup_lines = []
    while not outbox.empty():
        thread_name, message = outbox.get()
        target = cleanup_lines if message.startswith("清理后") else lines
        target.append((thread_name, message))

    for thread_name, message in sorted(lines):
        print(f"{thread_name}: {message}")

    print("\n=== 处理完成后清理上下文 ===")
    for thread_name, message in sorted(cleanup_lines):
        print(f"{thread_name} {message}")
```

## 🔍 师兄给你逐行拆

### 创建一个 ThreadLocal

```python
request_context = threading.local()
```

**这行在干嘛？**

`threading.local()` 创建一个 ThreadLocal 对象，作为所有线程共享的“壳”。但每个线程对它属性的读写，都存到线程自己的私有空间里，互相看不见。

**为什么这么写？**

它就是上一关“先想一个问题”的答案：要的是“全局变量般的方便访问 + 每线程独立”这两个特性同时成立。

---

### 绑定当前线程的上下文

```python
def bind_context(user, request_id):
    request_context.user = user
    request_context.request_id = request_id
```

**这行在干嘛？**

给 `request_context` 存两个属性：`user` 和 `request_id`。

**为什么这么关键？**

这句在哪个线程里执行，这两个属性就只属于那个线程。`Thread-A` 写 `user="Alice"`，`Thread-B` 同时写 `user="Bob"`，互不干扰——不像普通全局变量会被覆盖。

---

### 业务函数直接读上下文，不再层层传参

```python
def query_orders():
    return f"{request_context.request_id} {request_context.user} -> 正在查询订单"
```

**这行在干嘛？**

`query_orders()` 不接收 `user` 和 `request_id` 参数，而是从 `request_context` 里直接读。

**生活类比**

像每个员工随身挂着一张工牌，上面写着自己的工号和任务编号。谁要查工号，低头看自己那张就行，不用满办公室喊“你工号多少”。

**为什么这么写？**

调用链 `handle_request → query_orders → ...` 里每一层都不用再传 `user/request_id`，函数签名干净，加新字段也不用动旧函数。

---

### 主线程读不到子线程的值

```python
print(getattr(request_context, "user", None))  # None
```

**这行在干嘛？**

主线程没有调过 `bind_context`，所以它自己的 ThreadLocal 空间里没有 `user` 属性，`getattr` 返回默认值 `None`。

**容易踩的坑**

你会不会以为“子线程写了 `user=Alice`，主线程就能读到”？不会。ThreadLocal 的私密性是按线程隔离的，主线程和子线程完全隔开。也正是这个隔离，保证了多线程并发安全。

---

### 用 Queue 收集线程输出

```python
outbox = Queue()
...
outbox.put((thread_name, query_orders()))
```

**这行在干嘛？**

用线程安全的 `Queue` 把每个线程的输出收集起来，最后统一打印。

**为什么这么写？**

多个线程同时 `print` 会交错错乱，难以看清谁说了什么。用 `Queue` 存“线程名 + 消息”，主线程最后按线程名排序输出，结果稳定、可读。这比直接 `append` 到普通列表更稳妥，因为 `Queue` 是线程安全的。

---

### try/finally：线程复用时必须清理

```python
try:
    outbox.put((thread_name, query_orders()))
finally:
    del request_context.user
    del request_context.request_id
    outbox.put((thread_name, f"清理后: {getattr(request_context, 'user', None)}"))
```

**这行在干嘛？**

处理完请求后，无论中途有没有异常，都 `del` 掉 `request_context` 上的两个属性。

**为什么这么关键？**

真实项目里通常用线程池复用线程：同一个 `Thread-A` 刚处理完 Alice 的请求，下一秒就被派去处理 Charlie 的请求。如果不清掉，`query_orders` 里读到的 `request_context.user` 还是上一轮的 `Alice`——这是比数据竞争更隐蔽的坑：程序不报错，但业务串号了。

`finally` 保证即使处理过程中抛异常，清理也照样执行。最后一行用 `getattr(..., None)` 验证清理效果，会打印出 `清理后: None`。

---

### ThreadLocal 不是魔法，它只是“按线程隔离的字典”

底层上，`threading.local()` 给每个线程挂了一份独立的存储。对一个属性赋值，等价于往“当前线程那份存储”里写键值；读取时也从“当前线程那份”取。线程结束时，它那份存储会被回收。

所以它解决的是**“想要全局访问点、又不想被并发污染”**这一类问题，不是用来加速的。

## 🏃 跑一下试试

```bash
$ python threadlocal.py
=== 主线程没有绑定上下文 ===
None

=== 每个线程有自己的上下文 ===
Thread-A: req-001 Alice -> 正在查询订单
Thread-B: req-002 Bob -> 正在查询订单

=== 处理完成后清理上下文 ===
Thread-A 清理后: None
Thread-B 清理后: None
```

线程并发执行，但通过 `Queue` 收集 + 主线程排序，输出顺序是稳定的。注意 `Thread-A` 读到的是 `Alice`，`Thread-B` 读到的是 `Bob`，没有任何串号——这就是 ThreadLocal 起作用了。

## 💡 师兄的碎碎念

- ThreadLocal 解决的是“全局方便访问 + 每线程独立”的矛盾，不是并发加速工具。
- 用了线程池就一定记得清理，否则复用线程会读到上一轮的脏数据。
- 不要把所有状态都塞进 ThreadLocal，它只适合“当前请求/任务”这类上下文；长期状态放专门的对象更清楚。
- Web 框架里常见的 `request g`、数据库连接的 `current_session`，背后常常就是 ThreadLocal（或协程版的 `contextvars`）。
- 协程时代更推荐 `contextvars`：它对 `asyncio` 也生效，ThreadLocal 在协程间隔离会有坑。

## 🎓 这一关的知识点清单

- **threading.local()**：创建一个按线程隔离属性的 ThreadLocal 对象。
- **按线程隔离**：每个线程对同一属性各自读写，互不可见。
- **bind_context 模式**：在进入线程任务时绑定上下文，业务函数直接读取。
- **finally 清理**：处理完就删属性，防止线程池复用导致数据串号。
- **Queue 收集输出**：线程安全的输出收集方式，避免 print 交错、避免普通列表的并发隐患。
- **contextvars**：协程时代 ThreadLocal 的替代品，对 `asyncio` 同样有效。

## ➡️ 下一关

到这儿，线程相关的都讲完了，下一关换个轻松的：用正则表达式从一堆文本里精准提取信息 👉 [下一关：正则表达式 →](../50-regex/)
