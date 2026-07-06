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
    print(getattr(request_context, "user", None))

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
