# 第 58 关：TCP 编程（师兄带你学 Python）

## 🎯 这一关你会学到

- TCP 为什么叫面向连接的可靠传输
- 服务端的 `bind → listen → accept → recv/send` 流程
- 客户端的 `connect → send/recv` 流程
- 为什么网络传输要处理 `bytes`
- 为什么 TCP 是字节流，需要自己定义消息边界
- `send()` 和 `sendall()` 的差别

## 🤔 先想一个问题

TCP 像打电话：先拨号建立连接，对方接通后才能说话。只要连接正常，数据会按顺序送达。

但 TCP 不是“发一条消息，收一条消息”的协议。它只提供连续字节流。你要告诉程序：一条消息到哪里结束。示例里用换行符 `\n` 当消息边界。

## 📖 看代码

```python
# TCP 编程

import socket
import threading
from queue import Queue


def recv_line(conn):
    """读取到换行符为止，演示 TCP 字节流需要自己定义消息边界。"""
    chunks = []
    while True:
        chunk = conn.recv(1024)
        if not chunk:
            break
        chunks.append(chunk)
        if b"\n" in chunk:
            break
    return b"".join(chunks).decode("utf-8").strip()


def tcp_server(port_queue, server_logs):
    # SOCK_STREAM 表示 TCP；with 会在退出时自动关闭 socket。
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 端口传 0 表示让系统分配空闲端口。
        server.bind(("127.0.0.1", 0))
        server.listen(1)

        port = server.getsockname()[1]
        port_queue.put(port)

        conn, _addr = server.accept()
        with conn:
            message = recv_line(conn)
            server_logs.put(f"服务器收到: {message}")

            # sendall 会尽力把全部字节发送出去，比 send 更适合教学示例。
            conn.sendall(f"ACK: {message}\n".encode("utf-8"))
            server_logs.put("服务器已回复")


def tcp_client(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # connect 建立 TCP 连接，连接成功后才能 send/recv。
        client.connect(("127.0.0.1", port))

        # TCP 传输的是 bytes，字符串要先 encode。
        client.sendall("Hello, TCP Server!\n".encode("utf-8"))

        # recv 读到的也是 bytes，需要 decode 回字符串。
        return recv_line(client)


if __name__ == "__main__":
    port_queue = Queue()
    server_logs = Queue()

    server_thread = threading.Thread(target=tcp_server, args=(port_queue, server_logs))
    server_thread.start()

    # 等服务器把端口号放进队列，确保客户端不会抢跑。
    port = port_queue.get()

    print("=== TCP 客户端连接服务器 ===")
    response = tcp_client(port)
    print(f"客户端收到: {response}")

    server_thread.join()

    print("\n=== TCP 服务器处理结果 ===")
    while not server_logs.empty():
        print(server_logs.get())

    print("\n通信完成")
```

## 🔍 师兄给你拆开讲

`socket.socket(socket.AF_INET, socket.SOCK_STREAM)` 创建 IPv4 TCP socket。`SOCK_STREAM` 的意思就是流式套接字，对应 TCP。

服务端先 `bind()` 绑定地址，再 `listen()` 开始监听，然后 `accept()` 等客户端连接。`accept()` 返回一个新的 `conn`，后续读写都用这个连接对象，不再直接用监听 socket。

客户端用 `connect()` 连接服务端。连接成功后，双方都可以 `sendall()` 和 `recv()`。

网络里传的是 `bytes`，所以字符串要 `.encode("utf-8")`，收到字节后再 `.decode("utf-8")`。

`recv(1024)` 不是“收一条消息”，而是“最多收 1024 个字节”。一条业务消息可能被拆成多次收到，也可能多条消息粘在一起。真实协议通常会用换行符、固定长度头、长度前缀等方式定义消息边界。

示例用端口 `0` 让系统自动分配空闲端口，比固定写死 `9999` 更不容易和本机其他程序冲突。

## 🏃 跑一下试试

```bash
cd 58-tcp-programming
python tcp-programming.py
```

输出：

```text
=== TCP 客户端连接服务器 ===
客户端收到: ACK: Hello, TCP Server!

=== TCP 服务器处理结果 ===
服务器收到: Hello, TCP Server!
服务器已回复

通信完成
```

## 💡 师兄的提醒

直接写 socket 能帮你理解网络底层，但真实 Web 服务通常会用框架和服务器，比如 Flask/FastAPI/Django + Gunicorn/Uvicorn。框架帮你处理了连接管理、HTTP 协议解析、并发、超时等细节。

写 TCP 程序时要特别注意：超时、异常关闭、消息边界、编码、并发连接、资源释放。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `AF_INET` | IPv4 地址族 |
| `SOCK_STREAM` | TCP 流式套接字 |
| `bind()` | 服务端绑定地址和端口 |
| `listen()` | 开始监听连接 |
| `accept()` | 接受客户端连接 |
| `connect()` | 客户端连接服务端 |
| `sendall()` | 尽量发送完整字节数据 |
| `recv()` | 从连接读取字节 |
| 消息边界 | TCP 字节流需要应用层自己定义 |

## ➡️ 下一关

下一关：[UDP 编程](../59-udp-programming/README.md)。
